import requests
webpage = requests.get("http://192.168.45.252:8888//")
print(webpage.text)

text = webpage.text.split(':')

print(text)