from flask import Flask, render_template, request, redirect, url_for

from services.ocean import OceanClient
from services.prospeo import ProspeoClient
from services.brevo import BrevoClient
from utils.email_generator import generate_email

app = Flask(__name__)

ocean = OceanClient()
prospeo = ProspeoClient()
brevo = BrevoClient()

TEST_EMAIL = "bhavihalshivu@gmail.com"


@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    if request.method == "POST":

        domain = request.form.get("domain")

        try:

            ocean_result = ocean.find_lookalike_companies(
                domain,
                size=3
            )

            companies = ocean_result.get(
                "companies",
                []
            )

            for company_data in companies:

                company = company_data.get(
                    "company",
                    {}
                )

                company_name = company.get(
                    "name",
                    "Unknown"
                )

                company_domain = company.get(
                    "domain"
                )

                leads = prospeo.get_leads(
                    company_domain,
                    limit=2
                )

                print("LEADS =", leads)

                for lead in leads:

                    email_content = generate_email(
                        lead,
                        company_name
                    )

                    lead["subject"] = email_content["subject"]
                    lead["body"] = email_content["html"]

                results.append(
                    {
                        "company_name": company_name,
                        "company_domain": company_domain,
                        "leads": leads
                    }
                )

        except Exception as e:

            results.append(
                {
                    "company_name": "Error",
                    "company_domain": "",
                    "leads": [],
                    "error": str(e)
                }
            )

    return render_template(
        "index.html",
        results=results
    )


@app.route("/send-test-email", methods=["POST"])
def send_test_email():

    subject = request.form.get("subject")
    body = request.form.get("body")

    result = brevo.send_email(
        sender_email="pes1202203647@pesu.pes.edu",
        sender_name="Shivangouda Bhavihal",
        recipient_email=TEST_EMAIL,
        recipient_name="Shivangouda",
        subject=subject,
        html_content=body
    )

    print(result)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)