import requests
import json

website = requests.get('http://postman-echo.com/get')

website_text = website.text

info = json.loads(website_text)

headers_info = info["headers"]

print(headers_info['user-agent']) # Output: python-requests/...
