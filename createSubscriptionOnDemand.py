import requests

# api-endpoint
URL = "http://34.225.246.6/subscriptionToken.html"
   
# sending get request and saving the response as response object
r = requests.get(url = URL)
  
# printing the output
print(r)

url = "https://api-uat.kushkipagos.com/subscriptions/v1/card/1658748120364000"

payload = "{\n  \"language\": \"es\",\n  \"amount\": {\n    \"subtotalIva\": 15.16,\n    \"subtotalIva0\": 0,\n    \"ice\": 0,\n    \"iva\": 1.82,\n    \"currency\": \"USD\"\n  },\n  \"metadata\": {\n    \"customerId\": \"123\"\n  },\n  \"contactDetails\": {\n    \"documentType\": \"CC\",\n    \"documentNumber\": \"1009283738\",\n    \"email\": \"user@example.com\",\n    \"firstName\": \"John\",\n    \"lastName\": \"Doe\",\n    \"phoneNumber\": \"+593912345678\"\n  },\n  \"orderDetails\": {\n    \"siteDomain\": \"tuebook.com\",\n    \"shippingDetails\": {\n      \"name\": \"John Doe\",\n      \"phone\": \"+593912345678\",\n      \"address\": \"Eloy Alfaro 139 y Catalina Aldaz\",\n      \"city\": \"Quito\",\n      \"region\": \"Pichincha\",\n      \"country\": \"Ecuador\",\n      \"zipCode\": \"170402\"\n    },\n    \"billingDetails\": {\n      \"name\": \"John Doe\",\n      \"phone\": \"+593912345678\",\n      \"address\": \"Eloy Alfaro 139 y Catalina Aldaz\",\n      \"city\": \"Quito\",\n      \"region\": \"Pichincha\",\n      \"country\": \"Ecuador\",\n      \"zipCode\": \"170402\"\n    }\n  },\n  \"productDetails\": {\n    \"product\": [\n      {\n        \"id\": \"198952AB\",\n        \"title\": \"eBook Digital Services\",\n        \"price\": 6990000,\n        \"sku\": \"10101042\",\n        \"quantity\": 1\n      },\n      {\n        \"id\": \"198953AB\",\n        \"title\": \"eBook Virtual Selling\",\n        \"price\": 9990000,\n        \"sku\": \"004834GQ\",\n        \"quantity\": 1\n      }\n    ]\n  },\n  \"fullResponse\": \"v2\"\n}"
headers = {
    'Content-Type': "",
    'Private-Merchant-Id': "064e0baa810a4191bcd23e0c46918f1b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
