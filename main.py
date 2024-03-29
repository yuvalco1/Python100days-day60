from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/3de72d4b72a0eb35e683").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        print(request.form['name'],request.form['email'], request.form['email'],request.form['message'])
        # Can send email here....
        return "<h1> Successfully sent your message </h1>"
    elif request.method == 'GET':
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)