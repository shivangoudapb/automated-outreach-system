import os
import requests
from dotenv import load_dotenv

load_dotenv()


class BrevoClient:

    BASE_URL = "https://api.brevo.com/v3/smtp/email"

    def __init__(self):

        self.api_key = os.getenv("BREVO_API_KEY")

        self.headers = {
            "accept": "application/json",
            "api-key": self.api_key,
            "content-type": "application/json"
        }

    def send_email(
        self,
        sender_email,
        sender_name,
        recipient_email,
        recipient_name,
        subject,
        html_content
    ):

        payload = {
            "sender": {
                "name": sender_name,
                "email": sender_email
            },
            "to": [
                {
                    "email": recipient_email,
                    "name": recipient_name
                }
            ],
            "subject": subject,
            "htmlContent": html_content
        }

        response = requests.post(
            self.BASE_URL,
            headers=self.headers,
            json=payload
        )

        return response.json()