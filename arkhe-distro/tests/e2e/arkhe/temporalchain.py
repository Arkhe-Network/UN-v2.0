class TemporalChainClient:
    async def commit_event(self, *args, **kwargs): return {"status": "ANCHORED_L2", "l2_tx_hash": "a"}
