import requests
coun_code=input("Enter country code:")
pin_code=input("Enter pin code:")
response = requests.get(f'https://api.zippopotam.us/{coun_code}/{pin_code}')
js_response = response.json()
print(f'Country: {js_response["country"]}')
repository = js_response['places'][0]
print(f'Place Name: {repository["place name"]}')
print(f'State: {repository["state"]}')
