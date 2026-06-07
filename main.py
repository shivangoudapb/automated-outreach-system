from dotenv import load_dotenv
import os

load_dotenv()

print("Ocean:", bool(os.getenv("OCEAN_API_KEY")))
print("Prospeo:", bool(os.getenv("PROSPEO_API_KEY")))
print("Brevo:", bool(os.getenv("BREVO_API_KEY")))