import stripe
from forex_python.converter import CurrencyRates
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


def convert_rub_to_usd(amount):
    """Конвертация валюты."""
    # c = CurrencyRates()
    # rate = c.get_rate("RUB", "USD")
    rate = 98
    print(rate)
    return int(amount / rate)


def create_stripe_price(amount):
    """Создание цены в страйп."""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Payment"},
    )


def create_stripe_sessions(price):
    """Создание сессии на оплату в страйпе."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
