from services.ocean import OceanClient
from services.prospeo import ProspeoClient
from services.brevo import BrevoClient
from utils.email_generator import generate_email


TEST_EMAIL = "bhavihalshivu@gmail.com"


def main():

    ocean = OceanClient()
    prospeo = ProspeoClient()
    brevo = BrevoClient()

    print("\nFinding lookalike companies...\n")

    ocean_result = ocean.find_lookalike_companies(
        "microsoft.com",
        size=1
    )

    companies = ocean_result.get("companies", [])

    if not companies:
        print("No companies found.")
        return

    company_data = companies[0]
    company = company_data.get("company", {})

    company_name = company.get("name")
    company_domain = company.get("domain")

    print(f"Company Found: {company_name}")
    print(f"Domain: {company_domain}")

    print("\nFinding leads...\n")

    leads = prospeo.get_leads(
        company_domain,
        limit=1
    )

    if not leads:
        print("No leads found.")
        return

    lead = leads[0]

    print(f"Lead Found: {lead['name']}")
    print(f"Email Found: {lead['email']}")

    print("\nGenerating email...\n")

    email_content = generate_email(
        lead,
        company_name
    )

    print("Subject:")
    print(email_content["subject"])

    # DEVELOPMENT MODE
    # Sends email to yourself

    recipient_email = TEST_EMAIL
    recipient_name = "Shivangouda"

    # DEMO MODE
    # Uncomment these 2 lines and comment the 2 above

    # recipient_email = lead["email"]
    # recipient_name = lead["name"]

    print(f"\nSending email to: {recipient_email}\n")

    result = brevo.send_email(
        sender_email="pes1202203647@pesu.pes.edu",
        sender_name="Shivangouda Bhavihal",
        recipient_email=recipient_email,
        recipient_name=recipient_name,
        subject=email_content["subject"],
        html_content=email_content["html"]
    )

    print("\nBrevo Response:")
    print(result)


if __name__ == "__main__":
    main()