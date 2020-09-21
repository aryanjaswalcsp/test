import requests
n = 0
while n < 10:
    url = "http://readoapp.com"
    header = {
        "User-Agent":"NASA"
        }
    data = requests.get(url,headers=header)
    print(data)
    n = n + 1
