from aiogram import Router, types
from aiogram.filters import Command
from apis.authst import stripe 
from utils.prefixs import CustomCommand
# Asegúrate de importar tu función correctamente

router = Router()

@router.message(CustomCommand("mass"))
async def mass_handler(msg: types.Message):
    lines = msg.text.splitlines()

    if len(lines) < 2:
        return await msg.answer("❌ Uso: /mass [tipo]\nLuego coloca las cc en líneas separadas.")

    # Validar nombre de la API
    args = lines[0].split()
    if len(args) < 2 or args[1].lower() != "auth":
        return await msg.answer("❌ no soportada o no indicada.\nUsa: `/mass [tipo]`", parse_mode="Markdown")

    tarjetas = lines[1:]
    if len(tarjetas) > 10:
        return await msg.answer("⚠️ Solo puedes enviar un máximo de 10 ccs por uso.")

    user = msg.from_user
    username = f"@{user.username}" if user.username else user.full_name
    
    tarjetas = [line.strip() for line in lines[1:] if line.strip() and line.count("|") == 3]

    await msg.answer(f"🔄 Procesando {len(tarjetas)} con *mass*...", parse_mode="Markdown")

    resultados = []
    for i, linea in enumerate(tarjetas, 1):
        try:
            numero, mes, ano, cvv = linea.strip().split("|")
            raw = stripe(username, numero, mes, ano, cvv)

            # Extraer líneas específicas del resultado
            cc_line = next((l for l in raw.splitlines() if "CC:" in l), "")
            status_line = next((l for l in raw.splitlines() if "Status:" in l), "")
            response_line = next((l for l in raw.splitlines() if "Response:" in l), "")

            resultado = f"{i}. {cc_line}\n   {status_line}\n   {response_line}"
            resultados.append(resultado)
        except Exception:
            resultados.append(f"{i}. ❌ Error en : `{linea}`")

    final = "\n\n".join(resultados)
    await msg.answer(final[:4096], parse_mode="HTML")
