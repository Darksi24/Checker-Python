from aiogram import Router, types
from aiogram.filters import Command
from utils.prefixs import CustomCommand
from apis.authstM import stripeM  # tu función resumida
import asyncio

router = Router()

@router.message(CustomCommand("mass"))
async def mass_handler(msg: types.Message):
    args = msg.text.split(maxsplit=2)

    if len(args) < 3:
        return await msg.answer("❌ Uso: /mass auth lista\nSeparar tarjetas por línea.")

    gate = args[1].lower()
    lista = args[2].strip().splitlines()

    if len(lista) > 10:
        return await msg.answer("⚠️ Máximo 10 tarjetas por uso.")

    await msg.answer(f"🔄 Procesando {len(lista)} tarjetas con {gate.title()}...")

    resultados = []

    for i, tarjeta in enumerate(lista):
        try:
            numero, mes, ano, cvv = tarjeta.strip().split("|")
        except ValueError:
            resultados.append(f"{i+1}. ❌ Formato inválido.")
            continue

        # Simulación del proceso
        resultado = await stripe_light(msg.from_user.username or msg.from_user.full_name, numero, mes, ano, cvv)

        resultados.append(f"{i+1}. {resultado}")
        await asyncio.sleep(5)

    await msg.answer("\n\n".join(resultados), parse_mode="HTML")
