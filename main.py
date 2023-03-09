from flask import Flask, render_template, url_for
from post import Post
all_posts = Post()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/<post_no>")
def get_post(post_no):
    return render_template("post.html", n=int(post_no)-1, post = all_posts)

if __name__ == "__main__":
    app.run(debug=True)
