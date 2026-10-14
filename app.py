import requests

response = requests.get("https://example.com", timeout=10)
print(response.status_code)
