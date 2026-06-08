# Automated Outreach System

## Overview

Automated Outreach System is a lead generation and outreach automation platform that identifies potential target companies, discovers relevant decision makers, generates personalized outreach emails, and sends emails automatically.

The system integrates multiple external services to create a complete outbound outreach workflow.

---

## Problem Statement

Manually identifying target companies, finding relevant contacts, and crafting personalized outreach emails is time-consuming.

This project automates the process by:

1. Finding companies similar to a target company.
2. Discovering decision makers within those companies.
3. Retrieving verified contact information.
4. Generating personalized outreach emails.
5. Sending outreach emails automatically.

---

## Architecture

```text
Target Company Domain
          |
          v
      Ocean.io
          |
          v
 Similar Companies
          |
          v
       Prospeo
          |
          v
 Decision Makers
 + Verified Emails
          |
          v
  Email Generator
          |
          v
        Brevo
          |
          v
   Email Delivery
```

---

## Features

* Lookalike company discovery using Ocean.io
* Decision maker identification using Prospeo
* Email enrichment and verification
* Personalized outreach email generation
* Automated email delivery through Brevo
* Simple Flask-based web interface
* End-to-end outreach workflow

---

## Tech Stack

### Backend

* Python
* Flask

### APIs

* Ocean.io API
* Prospeo API
* Brevo API

### Frontend

* HTML
* CSS
* Jinja2 Templates

---

## Project Structure

```text
automated-outreach-system/
│
├── app.py
├── main.py
│
├── services/
│   ├── ocean.py
│   ├── prospeo.py
│   └── brevo.py
│
├── utils/
│   └── email_generator.py
│
├── templates/
│   └── index.html
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd automated-outreach-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OCEAN_API_KEY=your_ocean_api_key
PROSPEO_API_KEY=your_prospeo_api_key
BREVO_API_KEY=your_brevo_api_key
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Enter a company domain.
2. Generate lookalike companies using Ocean.io.
3. Discover decision makers using Prospeo.
4. Generate personalized outreach emails.
5. Send emails through Brevo.

---

## Development Notes

To avoid sending unintended outreach emails during development and testing, email delivery was routed to a controlled test inbox. The production workflow supports sending emails directly to discovered decision makers.

---

## Future Improvements

* AI-powered email personalization using LLMs
* Multi-step outreach sequences
* Campaign management dashboard
* Lead scoring
* CRM integration
* Email analytics and tracking

---

## Author

Shivangouda Bhavihal
