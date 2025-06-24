import os
import importlib
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN  # Si prefieres puedes dejar el token directamente
from config import OWNER_ID

from middleware.premium_guard import PremiumMiddleware
from middleware.cooldown import CooldownMiddleware



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.message.middleware(PremiumMiddleware())
dp.message.middleware(CooldownMiddleware())
# Cargar routers de /cmds
for file in os.listdir("cmds"):
    if file.endswith(".py"):
        mod = importlib.import_module(f"cmds.{file[:-3]}")
        dp.include_router(mod.router)

async def main():
    print("🤖 Bot Aiogram modular listo")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
