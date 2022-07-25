import requests

# api-endpoint
URL = "http://34.225.246.6/subscriptionToken.html"
   
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# printing the output
print(r)

url = "https://api-uat.kushkipagos.com/subscriptions/v1/card/search/1658748120364000"

headers = {
    'Content-Type': "application/json",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
