import serial
import time
import requests

webpage = requests.get("http://192.168.45.252:8888/")

text = "bbbb:0101:0001:1110:1011:0101:0110".split(':')
s = '{'
for t in text[1:]:
    s += '{'
    for tt in t:
        s += "'" + tt + "',"
    s = s[:-1] + '},'
s = s[:-1] + '}'
print(s)