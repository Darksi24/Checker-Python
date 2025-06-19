# /cmds/stripe auth.py
from aiogram import Router, types
from aiogram.filters import Command
from apis.authst import stripe
from utils.prefixs import CustomCommand

router = Router()

@router.message(CustomCommand("auth"))
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

    respue = await msg.answer("🔄 Procesando...")

    # Llamar a la API
    resultado = stripe(username, numero, mes, ano, cvv)

    await respue.edit_text(resultado, parse_mode="HTML")
