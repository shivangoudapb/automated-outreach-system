import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "X-KEY": os.getenv("PROSPEO_API_KEY"),
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.prospeo.io/search-suggestions",
    headers=headers,
    json={
        "industry_search": "software"
    }
)

print(response.status_code)
print(response.text)