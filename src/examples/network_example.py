from src.utils import network_helpers


def basic_get():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = network_helpers.get(url)
    print(response.json())


def get_with_params():
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": 1}
    response = network_helpers.get(url, params=params)
    print(response.json())


def basic_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "My new post",
        "body": "This is the content of my new post.",
        "userId": 1,
    }
    response = network_helpers.post(url, json=data)
    print(response.json())


def post_with_headers():
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    data = {
        "title": "My new post with headers",
        "body": "This is the content of my new post with headers.",
        "userId": 1,
    }
    response = network_helpers.post(url, headers=headers, json=data)
    print(response.json())
