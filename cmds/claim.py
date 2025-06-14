from aiogram import Router, types

router = Router()

from aiogram.filters import Command

from datetime import datetime, timedelta

@router.message(Command("claim"))
async def claim(msg: types.Message):
    args = msg.text.split()
    if len(args) < 2:
        return await msg.answer("Uso correcto: /claim KEY-XXXXX-XXXX")

    key = args[1].strip()

    with open("codes.txt", "r") as f:
        codigos = [line.strip() for line in f if line.strip()]

    encontrado = None
    for line in codigos:
        if line.startswith(key + ":"):
            encontrado = line
            break

    if not encontrado:
        return await msg.answer("❌ Código inválido o ya canjeado.")

    horas = int(encontrado.split(":")[1])
    expire_time = (datetime.utcnow() + timedelta(hours=horas)).timestamp()

    user_id = str(msg.from_user.id)
    with open("premium.txt", "a") as f:
        f.write(f"{user_id}:{int(expire_time)}\n")

    codigos.remove(encontrado)
    with open("codes.txt", "w") as f:
        f.write("\n".join(codigos) + "\n")

    await msg.answer(f"✅ Código canjeado.\nPremium activado por {horas} horas.")
