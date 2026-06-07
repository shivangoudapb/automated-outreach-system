def generate_email(lead, company_name):

    name = lead["name"]
    title = lead["title"]

    first_name = name.split()[0]

    subject = (
        f"Quick question about your work at {company_name}"
    )

    html_content = f"""
    <html>
    <body>

    <p>Hi {first_name},</p>

    <p>
    I came across your profile and noticed that you are currently working as
    <strong>{title}</strong> at <strong>{company_name}</strong>.
    </p>

    <p>
    Given your leadership role, I thought it would be valuable to reach out and introduce myself.
    </p>

    <p>
    I am currently exploring opportunities to connect with professionals leading innovation,
    engineering, operations, and business transformation initiatives.
    </p>

    <p>
    I would love to learn more about your work and explore whether there might be opportunities
    for collaboration or knowledge sharing.
    </p>

    <p>
    Looking forward to hearing from you.
    </p>

    <br>

    <p>
    Best regards,<br>
    Shivangouda Bhavihal
    </p>

    </body>
    </html>
    """

    return {
        "subject": subject,
        "html": html_content
    }