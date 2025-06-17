from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict
from datetime import datetime

EXCEPT_COMMANDS = ["cmds", "start", "claim", "code"]
PREFIX = ("/", ".", "!", "?", "$")

class PremiumMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict], Awaitable],
        event: Message,
        data: Dict
    ):
        if event.text and event.text.startswith(PREFIX):
            command = event.text[1:].split()[0]
            if command in EXCEPT_COMMANDS:
                return await handler(event, data)

            try:
                with open("premium.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split(":")
                        if len(parts) == 2 and parts[0] == str(event.from_user.id):
                            expire_ts = int(parts[1])
                            if datetime.utcnow().timestamp() < expire_ts:
                                return await handler(event, data)
                            else:
                                await event.answer("⚠️ Tu acceso premium ha expirado.")
                                return
                # No encontró el ID
                await event.answer("🚫 Este comando es solo para usuarios premium.")
                return
            except FileNotFoundError:
                await event.answer("🚫 Este comando es solo para usuarios premium.")
                return

        return await handler(event, data)
