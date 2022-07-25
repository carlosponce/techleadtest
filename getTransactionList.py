import requests

url = "https://api-uat.kushkipagos.com/analytics/v1/transactions-list"

headers = {
    'Content-Type': "/",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("GET", url, headers=headers,params={"from": "2022-07-19T13:39:00.836",  "to": "2022-07-29T13:39:00.836" })

print(response.text)