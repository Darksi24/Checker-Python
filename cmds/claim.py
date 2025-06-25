from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime, timedelta

router = Router()

@router.message(Command("claim"))
async def claim(msg: types.Message):
    args = msg.text.split()
    if len(args) < 2:
        return await msg.answer("Uso correcto: /claim KEY-XXXXX-XXXX")

    key = args[1].strip()
    user = msg.from_user
    username = f"@{user.username}" if user.username else user.full_name


    # Leer códigos válidos
    try:
        with open("codes.txt", "r") as f:
            codigos = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return await msg.answer("❌ No hay códigos disponibles.")

    encontrado = None
    for line in codigos:
        if line.startswith(key + ":"):
            encontrado = line
            break

    if not encontrado:
        return await msg.answer("❌ Código inválido o ya canjeado.")

    # Obtener duración y calcular expiración
    horas = int(encontrado.split(":")[1])
    expire_time = (datetime.utcnow() + timedelta(hours=horas)).timestamp()
    user_id = str(msg.from_user.id)

    # Leer premium.txt, filtrar el usuario si ya existe
    try:
        with open("premium.txt", "r") as f:
            lineas = [line for line in f if not line.startswith(f"{user_id}:")]
    except FileNotFoundError:
        lineas = []

    # Agregar nueva entrada
    lineas.append(f"{user_id}:{int(expire_time)}\n")

    # Guardar archivo actualizado
    with open("premium.txt", "w") as f:
        f.writelines(lineas)

    # Eliminar código usado
    codigos.remove(encontrado)
    with open("codes.txt", "w") as f:
        f.write("\n".join(codigos) + "\n")

    hora_local = datetime.utcfromtimestamp(expire_time).strftime("%d-%m-%y %H:%M:%S")
    await msg.answer(f"✅ Código canjeado.\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌\nPremium activado\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌\n➵ Time: {horas}\n ➵ End: {hora_local}\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌\n By: {username}")