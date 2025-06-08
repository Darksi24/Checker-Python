from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Awaitable, Dict

EXCEPT_COMMANDS = ["start", "claim", "code"]

class PremiumMiddleware(BaseMiddleware):
    async def __call__(
        self, handler: Callable[[Message, Dict], Awaitable],
        event: Message, data: Dict
    ):
        if event.text and event.text.startswith("/"):
            command = event.text[1:].split()[0]
            if command in EXCEPT_COMMANDS:
                return await handler(event, data)

            try:
                with open("premium.txt", "r") as f:
                    ids = f.read().splitlines()
                if str(event.from_user.id) not in ids:
                    await event.answer("🚫 Este comando es solo para usuarios premium.")
                    return
            except FileNotFoundError:
                pass

        return await handler(event, data)
