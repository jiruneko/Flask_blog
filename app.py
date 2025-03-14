from flask import Flask, request, url_for, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="ホームページ",
        content="これはFlaskとJinja2を使用したサンプルページです。",
    )


@app.route("/about")
def about():
    return "This is about page."


@app.route("/contact")
def contact():
    return "This is the contact page."


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("submit.html")


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {username}"


@app.route("/post/<int:post_id>/comment/<int:comment_id>")
def show_comment(post_id, comment_id):
    return f"Post ID: {post_id}, Comment ID: {comment_id}"


@app.route("/user/<username>")
def user_profile(username):
    return f"User: {username}"


@app.route("/generate_url")
def generate_url():
    return url_for("user_profile", username="John")


@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist", 404


@app.route("/profile")
def profile():
    user = {"name": "Taro", "age": 30, "location": "Tokyo"}
    return render_template("profile.html", user=user)


@app.route("/posts")
def posts():
    posts = [
        {"title": "Flaskkの使い方", "author": "Alice"},
        {"title": "Jinja2の紹介", "author": "Bob"},
        {"title": "Flaskのルーティング", "author": "Charlie"},
    ]
    return render_template("posts.html", posts=posts)


@app.route("/dashboard")
def dashboard():
    user_logged_in = True
    return render_template("dashboard.html", logged_in=user_logged_in)


def format_datetime(value, format="%Y/%m/%d"):
    return value.strftime(format)


app.jinja_env.filters["datatime"] = format_datetime


@app.route("/time")
def show_time():
    now = datetime.now()
    return render_template("time.html", current_time=now)


if __name__ == "__main__":
    app.run(debug=True)
