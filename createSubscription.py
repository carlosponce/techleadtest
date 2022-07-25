import requests

# api-endpoint
URL = "http://34.225.246.6/subscriptionToken.html"
   
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# printing the output
print(r)

url = "https://api-uat.kushkipagos.com/subscriptions/v1/card"

payload = "{\n  \"token\": \"a25d85adb32244ce93b7c2c944407a38\",\n  \"planName\": \"Premium\",\n  \"periodicity\": \"monthly\",\n  \"contactDetails\": {\n    \"documentType\": \"CC\",\n    \"documentNumber\": \"1009283738\",\n    \"email\": \"user@example.com\",\n    \"firstName\": \"John\",\n    \"lastName\": \"Doe\",\n    \"phoneNumber\": \"+593912345678\"\n  },\n  \"amount\": {\n    \"subtotalIva\": 1,\n    \"subtotalIva0\": 0,\n    \"ice\": 0,\n    \"iva\": 0.14,\n    \"currency\": \"USD\"\n  },\n  \"startDate\": \"2022-05-25\",\n  \"metadata\": {\n    \"plan\": {\n      \"fitness\": {\n        \"cardio\": \"include\",\n        \"rumba\": \"include\",\n        \"pool\": \"include\"\n      }\n    }\n  }\n}"
      
headers = {
    'Content-Type': "",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)