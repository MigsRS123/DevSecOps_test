from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Test App</title></head>
    <body>
        <h1>Test Application for Security Scan</h1>
        <a href="/login?username=admin">Login</a>
        <form action="/search" method="GET">
            <input type="text" name="q" value="test">
            <input type="submit" value="Search">
        </form>
        <form action="/comment" method="POST">
            <input type="text" name="comment" value="Hello">
            <input type="submit" value="Comment">
        </form>
    </body>
    </html>
    """

@app.route("/login")
def login():
    username = request.args.get('username', '')
    return f"<p>Logged in as: {username}</p>"

@app.route("/search")
def search():
    query = request.args.get('q', '')
    return f"<p>Search results for: {query}</p>"

@app.route("/comment", methods=['POST'])
def comment():
    comment_text = request.form.get('comment', '')
    return render_template_string(f"<p>Comment: {comment_text}</p>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)