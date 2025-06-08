from aiogram import Router, types
from aiogram.filters import Command
import requests

router = Router()

@router.message(Command("st"))
async def st_handler(msg: types.Message):
    args = msg.text.split(" ", maxsplit=1)
    if len(args) < 2:
        return await msg.answer("❌ Formato incorrecto.\nEjemplo: /st 4111111111111111|12|2026|123")

    try:
        numero, mes, ano, cvv = args[1].strip().split("|")
    except ValueError:
        return await msg.answer("❌ Debes enviar los 4 datos separados por `|`", parse_mode="Markdown")

    await msg.answer("🔄 Procesando...")

    # Ahora tu request
    try:
        cookies = { ... }  # aquí pegas tus cookies completas
        headers = { ... }  # y tus headers también

        json_data = {
            'query': '...',
            'variables': {
                'token': '8UA0911501956764B',
                'card': {
                    'cardNumber': numero,
                    'type': 'MASTER_CARD',
                    'expirationDate': f'{mes}/{ano}',
                    'postalCode': '10010',
                    'securityCode': cvv
                },
                'phoneNumber': '19008007828',
                'firstName': 'Luis',
                'lastName': 'Pech',
                'billingAddress': {
                    'givenName': 'Luis',
                    'familyName': 'Pech',
                    'line1': None,
                    'line2': None,
                    'city': None,
                    'state': None,
                    'postalCode': '10010',
                    'country': 'US',
                },
                'email': 'asdimandam@gmail.com',
                'currencyConversionType': 'VENDOR',
            },
            'operationName': None
        }

        response = requests.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=15
        )

        # Mostrar respuesta parcial
        await msg.answer(f"✅ Resultado:\n```{response.text[:400]}```", parse_mode="Markdown")

    except Exception as e:
        await msg.answer(f"❌ Error:\n`{str(e)}`", parse_mode="Markdown")
