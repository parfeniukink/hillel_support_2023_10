import string
import uuid
from django.core.mail import send_mail
from .models import User


def create_activation_key(email: str) -> uuid.UUID:
    return uuid.uuid3(namespace=uuid.uuid4(), name=email)


def create_activation_link(activation_key: uuid.UUID) -> str:
    return f"https://frontend.com/users/activate/{activation_key}"


def create_random_email() -> str:
    domain = "gmail.com"
    email_value = "".join(string.ascii_lowercase for _ in range(10))

    return f"{email_value}@{domain}"


def send_user_activation_email(email: str) -> None:
    """Generate a new activation link and send it via email."""

    activation_key: uuid.UUID = create_activation_key(email)
    activation_link: str = create_activation_link(activation_key)

    # IO-bound
    for _ in range(1000):
        send_mail(
            subject="User activation",
            message=f"Please activate your account: {activation_link}",
            from_email="admin@admin.com",
            recipient_list=[create_random_email()],
            fail_silently=False,
        )
