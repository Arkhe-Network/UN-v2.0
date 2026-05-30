#!/usr/bin/env python3
"""
Passport Gateway Proxy for node/
This imports the canonical implementation from arkhe-substrato-989x-passport-gateway.
"""

import sys
import os

# Add the arkhe-substrato-989x-passport-gateway directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'arkhe-substrato-989x-passport-gateway')))

from passport_gateway import (
    PassportGateway,
    HumanityProof,
    StampCredential,
    VerificationStatus,
    PassportGatewayError
)

if __name__ == "__main__":
    import asyncio
    async def demo_passport_gateway():
        gateway = PassportGateway()
        await gateway.start()

        # Verificar humanidade de alguns endereços
        addresses = ["0xAlice123...", "0xBob456...", "0xSybil999...", "0xArchitect0009..."]
        for addr in addresses:
            proof = await gateway.is_human(addr)
            print(f"{addr[:15]}... → humano: {proof.is_human}, score: {proof.score:.2f}, "
                  f"stamps: {len(proof.stamps)}, ORCID: {proof.orcid_verified}")

        # Verificar permissão para votar na DAO
        print("\nVerificação DAO:")
        for addr in ["0xAlice123...", "0xSybil999..."]:
            can = await gateway.verify_dao_voter(addr)
            print(f"  {addr[:15]}... pode votar: {can}")

        await gateway.stop()

    asyncio.run(demo_passport_gateway())
