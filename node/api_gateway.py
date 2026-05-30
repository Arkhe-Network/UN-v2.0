import json
import asyncio
from aiohttp import web
from urllib.parse import urlparse, parse_qs
from typing import Optional

class APIGateway:
    def __init__(self, node_id: str, passport=None):
        self.node_id = node_id
        self.queries_processed = 0
        self.passport = passport
        self.app = web.Application()
        self.app.add_routes([
            web.get('/v1/status', self.handle_status),
            web.get('/v1/oracle/feeds', self.handle_feeds),
            web.get('/v1/identity/passport', self.handle_passport),
            web.get('/v1/dao/verify-voter', self.handle_verify_voter)
        ])
        self.runner = None

    async def start_http_server(self):
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '0.0.0.0', 8080)
        await site.start()
        print("API Gateway server started on http://0.0.0.0:8080")

    async def stop(self):
        if self.runner:
            await self.runner.cleanup()

    async def handle_status(self, request):
        return web.json_response({"status": "ok"})

    async def handle_feeds(self, request):
        return web.json_response({"feeds": []})

    async def handle_passport(self, request):
        address = request.query.get("address")
        if not address:
            return web.Response(status=400, text="Missing address")
        proof = await self.passport.is_human(address)
        return web.json_response({
            "address": proof.address,
            "is_human": proof.is_human,
            "score": proof.score,
            "stamps": proof.stamps,
            "orcid_verified": proof.orcid_verified,
        })

    async def handle_verify_voter(self, request):
        address = request.query.get("address")
        if not address:
            return web.Response(status=400, text="Missing address")
        can_vote = await self.passport.verify_dao_voter(address)
        return web.json_response({"address": address, "can_vote": can_vote})
