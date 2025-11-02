from typing import Dict, List
from fastapi import WebSocket
import asyncio

class ConnectionManager:
    def __init__(self):
        # map firebase_uid -> websocket
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, uid: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[uid] = websocket

    async def disconnect(self, uid: str):
        try:
            self.active_connections.pop(uid, None)
        except:
            pass

    async def send_personal_message(self, message: dict, uid: str):
        ws = self.active_connections.get(uid)
        if ws:
            await ws.send_json(message)

    async def broadcast(self, message: dict, exclude_uid: str = None):
        for uid, ws in list(self.active_connections.items()):
            if uid == exclude_uid: 
                continue
            try:
                await ws.send_json(message)
            except:
                # ignore failed sockets
                pass

manager = ConnectionManager()
