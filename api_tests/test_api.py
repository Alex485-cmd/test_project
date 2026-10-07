import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_status_code():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200

def test_get_single_post():
    r = requests.get(f"{BASE_URL}/posts/1")
    post = r.json()
    assert post["id"] == 1
    assert "title" in post
