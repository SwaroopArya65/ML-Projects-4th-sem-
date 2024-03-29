from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    # return 'Hello, World!'

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

# @app.route('/dashboard')
# def dashboard():
#     return render_template("dashboard.html")

@app.route('/heart')
def heart():
    return render_template("heart.html")

# @app.route('/contact')
# def contact():
#     return render_template("contact.html")

@app.route('/parkinsons')
def parkinsons():
    return render_template("parkinsons.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)