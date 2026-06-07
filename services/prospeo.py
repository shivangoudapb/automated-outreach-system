import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ProspeoClient:

    BASE_URL = "https://api.prospeo.io"

    def __init__(self):
        self.api_key = os.getenv("PROSPEO_API_KEY")

        self.headers = {
            "X-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def search_company_by_domain(self, domain):
        url = f"{self.BASE_URL}/search-company"

        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [domain]
                    }
                }
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        return response.json()