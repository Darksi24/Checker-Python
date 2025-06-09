from aiogram import Router, types
from config import OWNER_ID
import random

router = Router()

def generar_codigo():
    return f"KEY-{random.randint(10000, 99999)}-{random.randint(1000, 9999)}"

from aiogram.filters import Command

@router.message(Command("code"))
async def code(msg: types.Message):
    if msg.from_user.id != OWNER_ID:
        return await msg.answer("🚫 No tienes permiso.")
    
    codigo = generar_codigo()
    with open("codes.txt", "a") as f:
        f.write(codigo + "\n")
    
    await msg.answer(f"ミ★ 𝘒𝘦𝘺 𝘸𝘢𝘴 𝘨𝘦𝘯𝘦𝘳𝘢𝘵𝘦𝘥 ★彡\nミ★ 𝘛𝘪𝘮𝘦: 𝘜𝘯𝘥𝘦𝘧𝘪𝘯𝘦𝘥 ★彡\nミ★ 𝘒𝘦𝘺 𝘊𝘰𝘥𝘦 ★彡: `{codigo}`", parse_mode="Markdown")
