from flask import Flask, request, render_template, url_for, request

app = Flask(__name__)
menu = [
    {"name": "Set up", "url": "install-flask"},
    {"name": "Set data", "url": "set_data"},
    {"name": "Back network", "url": "contact"}
]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template("index.html", title="Big Title", menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="Big Title", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form["email"])
    return render_template('contact.html', title="Small title", menu=menu)


@app.route("/set_data", methods=["POST", "GET"])
def set_data():
    if request.method == "POST":
        print(request.form["email"])
    return render_template('big_setter.html', title="Маркировка рекламы", menu=menu)

# app.add_url_rule('/', 'index', index)


if __name__ == "__main__":
    app.run(debug=True)
