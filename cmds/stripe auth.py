# /cmds/stripe auth.py
from aiogram import Router, types
from aiogram.filters import Command
from apis.authst import stripe

router = Router()

@router.message(Command("auth"))
async def stripe_handler(msg: types.Message):
    args = msg.text.split(" ", maxsplit=1)
    if len(args) < 2:
        return await msg.answer("❌ Formato inválido\nUsa: /str numero|mes|año|cvv")

    try:
        numero, mes, ano, cvv = args[1].strip().split("|")
    except ValueError:
        return await msg.answer("❌ Debes enviar 4 datos separados por `|`", parse_mode="Markdown")
    
    user = msg.from_user
    username = f"@{user.username}" if user.username else user.full_name

    await msg.answer("🔄 Procesando...")

    # Llamar a la API
    resultado = stripe(username, numero, mes, ano, cvv)

    await msg.answer(resultado)
