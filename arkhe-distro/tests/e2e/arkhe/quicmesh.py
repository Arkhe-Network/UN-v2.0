class QUICMeshClient:
    async def open_channel(self, *args, **kwargs): pass
    async def publish(self, *args, **kwargs): return {"quorum_reached": True, "replicas_ack": 2}
