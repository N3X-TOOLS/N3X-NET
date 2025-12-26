import base64
import urllib.parse

def base64_encode():
    text = input("Text: ")
    print(base64.b64encode(text.encode()).decode())

def base64_decode():
    text = input("Base64: ")
    try:
        print(base64.b64decode(text).decode())
    except:
        print("Ungültig")

def url_encode():
    text = input("Text: ")
    print(urllib.parse.quote(text))

def url_decode():
    text = input("URL Encoded: ")
    print(urllib.parse.unquote(text))
