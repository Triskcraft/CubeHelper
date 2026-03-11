import asyncio

from .loader import load
from mcdis_rcon.classes import McDisClient

class mdaddon():
    def __init__(self, client: McDisClient):
        """Inicializa el addon con el cliente de McDisClient"""
        self.client = client
        asyncio.create_task(load(client))