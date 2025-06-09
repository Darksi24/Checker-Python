from aiogram import Router, types

router = Router()

from aiogram.filters import Command

@router.message(Command("claim"))
async def claim(msg: types.Message):
    args = msg.text.split()
    if len(args) < 2:
        return await msg.answer("Uso correcto: /claim KEY-XXXXX-XXXX")

    key = args[1].strip()

    with open("codes.txt", "r") as f:
        codigos = [line.strip() for line in f if line.strip()]

    if key not in codigos:
        return await msg.answer("❌ Código inválido o ya canjeado.")

    # Añadir a premium.txt
    user_id = str(msg.from_user.id)
    with open("premium.txt", "a+") as f:
        f.seek(0)
        if user_id not in f.read():
            f.write(user_id + "\n")

    # Eliminar la key usada
    codigos.remove(key)
    with open("codes.txt", "w") as f:
        f.write("\n".join(codigos) + "\n")

    await msg.answer(" ¡Código canjeado! Ahora tienes acceso.")
