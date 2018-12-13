from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")  # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/confirmation", methods=["GET","POST"])
def confirm():
    if request.method == "GET":
        return "Please submit form instead"
    else:
        email = request.form.get("email")
        message = request.form.get("message")
        return render_template("confirmation.html", message=message)



if __name__ == '__main__':
    app.run()
