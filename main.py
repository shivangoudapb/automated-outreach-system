from services.prospeo import ProspeoClient


client = ProspeoClient()

result = client.search_company_by_domain(
    "microsoft.com"
)

print(result)