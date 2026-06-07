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

    def search_decision_makers(self, company_domain):

        url = f"{self.BASE_URL}/search-person"

        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [company_domain]
                    }
                },
                "person_seniority": {
                    "include": [
                        "C-Suite",
                        "Vice President",
                        "Director"
                    ]
                }
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        result = response.json()

        print("\n" + "=" * 80)
        print("PROSPEO SEARCH RESPONSE")
        print("=" * 80)
        print(result)
        print("=" * 80)

        return result

    def enrich_person(self, person_id):

        url = f"{self.BASE_URL}/enrich-person"

        payload = {
            "only_verified_email": True,
            "data": {
                "person_id": person_id
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        return response.json()

    def get_leads(self, company_domain, limit=5):

        print(f"\nSearching Prospeo for: {company_domain}")

        search_result = self.search_decision_makers(
            company_domain
        )

        leads = []

        people = search_result.get(
            "results",
            []
        )

        print(f"People returned: {len(people)}")

        for person_data in people[:limit]:

            person = person_data.get(
                "person",
                {}
            )

            person_id = person.get(
                "person_id"
            )

            print(f"Enriching person: {person_id}")

            enrich_result = self.enrich_person(
                person_id
            )

            if enrich_result.get("error"):
                print("Enrichment failed")
                continue

            enriched_person = enrich_result.get(
                "person",
                {}
            )

            email_info = enriched_person.get(
                "email",
                {}
            )

            lead = {
                "name": enriched_person.get(
                    "full_name"
                ),
                "title": enriched_person.get(
                    "current_job_title"
                ),
                "email": email_info.get(
                    "email"
                ),
                "linkedin": enriched_person.get(
                    "linkedin_url"
                )
            }

            print("Lead found:")
            print(lead)

            leads.append(lead)

        print(f"Final leads count: {len(leads)}")

        return leads