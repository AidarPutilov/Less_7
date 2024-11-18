import stripe
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создание продукта в страйп. Возвращает ID."""

    product = instance.course or instance.lesson
    stripe_product = stripe.Product.create(name=product)
    return stripe_product.get("id")


def create_stripe_price(amount, product_id):
    """Создание цены в страйп. Возвращает ID."""

    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )
    return price.get("id")


def create_stripe_sessions(price):
    """Создание сессии на оплату в страйп. Возвращает ID сессии и URL платежа."""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
