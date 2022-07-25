import requests

# api-endpoint
URL = "http://34.225.246.6/subscriptionToken.html"
   
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# printing the output
print(r)

url = "https://api-uat.kushkipagos.com/subscriptions/v1/card/1658748120364000/capture"

payload = "{\n  \"ticketNumber\": \"549442549895561033\",\n  \"amount\": {\n    \"currency\": \"PEN\",\n    \"subtotalIva\": 0,\n    \"iva\": 0,\n    \"subtotalIva0\": 600,\n    \"ice\": 0\n  },\n  \"fullResponse\": \"v2\"\n}"
headers = {
    'Content-Type': "",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
