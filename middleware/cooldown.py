from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Awaitable
from datetime import datetime, timedelta

# Diccionario en memoria: user_id -> última vez que usó el comando
cooldowns: Dict[int, datetime] = {}

# Personaliza aquí
COOLDOWN_SECONDS = 60
EXCEPT_COMMANDS = ["start", "cmds", "code", "claim"]

class CooldownMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict], Awaitable],
        event: Message,
        data: Dict
    ):
        if not isinstance(event, Message) or not event.text:
            return await handler(event, data)

        if event.text.startswith(("/", ".", "!", "$", "?")):
            command = event.text[1:].split()[0].lower()
            user_id = event.from_user.id

            if command in EXCEPT_COMMANDS:
                return await handler(event, data)

            now = datetime.utcnow()
            last_used = cooldowns.get(user_id)

            if last_used and now < last_used + timedelta(seconds=COOLDOWN_SECONDS):
                remaining = int((last_used + timedelta(seconds=COOLDOWN_SECONDS) - now).total_seconds())
                await event.answer(f"⏳ Espera {remaining}s para volver a usar este comando.")
                return

            # Actualizar cooldown
            cooldowns[user_id] = now

        return await handler(event, data)
