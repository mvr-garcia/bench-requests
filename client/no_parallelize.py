import requests
import time


def post(data):
    url = "http://0.0.0.0:8000/items/"

    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"Request to {url} returned status code {response.status_code}. Response will be None")
        return None
    return response.json()


sample = {
    "name": "Marcos",
    "description": "Garcia",
    "price": 10,
    "tax": 2
}
data = [sample for _ in range(1000)]

start = time.perf_counter()
for d in data:
    result = post(d)
    print(result)

end = time.perf_counter()
print("Time taken: ", end - start)
