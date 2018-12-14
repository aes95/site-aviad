from flask import Flask, render_template, url_for, request
import os

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
def confirmation():
    if request.method == "GET":
        return "Please submit form instead"
    message = request.form.get("message")
    return render_template("confirmation.html", message=message)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



if __name__ == '__main__':
    app.run()
