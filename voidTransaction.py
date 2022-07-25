import requests

url = "https://api-uat.kushkipagos.com/subscriptions/v1/card/1658748120364000"

headers = {
    'Content-Type': "application/json",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)