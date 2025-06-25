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

    args = msg.text.split()
    if len(args) < 2:
        return await msg.answer("Uso: /code <duración en horas>")

    try:
        horas = int(args[1])
    except ValueError:
        return await msg.answer("❌ La duración debe ser un número de horas.")

    codigo = generar_codigo()
    with open("codes.txt", "a") as f:
        f.write(f"{codigo}:{horas}\n")  # Guardamos en horas

    await msg.answer(
        f"〔 Key was generated ❳ \n"
        f"╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌\n"
        f"━\n"
        f"➵ Time: {horas} horas\n"
        f"━\n"
        f"➵ Use: `/claim {codigo}`\n"
        f"╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌", parse_mode="Markdown"
    )
