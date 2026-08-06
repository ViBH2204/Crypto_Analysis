import requests

# Test fetching data for Bitcoin, Ethereum, and Tether
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether&vs_currencies=usd&include_24hr_change=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API Connection Successful!\n")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")