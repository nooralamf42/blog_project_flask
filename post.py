import requests

response = requests.get("https://api.npoint.io/b48aec3303bb2f803040")
posts= response.json()
class Post:

    def __init__(self):
        self.len_posts = len(posts)
        self.h1 = [posts[n]["title"] for n in range(len(posts))]
        self.h2 = [posts[n]["subtitle"] for n in range(len(posts))]
        self.p = [posts[n]["body"] for n in range(len(posts))]


