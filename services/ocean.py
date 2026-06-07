import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OceanClient:

    BASE_URL = "https://api.ocean.io"

    def __init__(self):

        self.api_key = os.getenv("OCEAN_API_KEY")

        self.headers = {
            "X-Api-Token": self.api_key,
            "Content-Type": "application/json"
        }

    def find_lookalike_companies(self, domain, size=3):

        url = f"{self.BASE_URL}/v3/search/companies"

        payload = {
            "size": size,
            "companiesFilters": {
                "lookalikeDomains": [
                    domain
                ]
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        return response.json()