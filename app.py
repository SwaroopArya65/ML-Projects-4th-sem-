from flask import Flask, render_template, url_for,request
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

# @app.route('/dashboard', methods =["GET", "POST"])
# def dashboard():
#     if request.method == "POST":
#        # getting input with name = fname in HTML form
#        number_Pregnancies = request.form.get("nop")
#        # getting input with name = lname in HTML form 
#        gluco_selevel = request.form.get("gl") 
#        # getting input with name = lname in HTML form 
#        blood_pressure = request.form.get("bpv") 
#        # getting input with name = lname in HTML form 
#        skin_thickness = request.form.get("stv") 
#        # getting input with name = lname in HTML form 
#        age_person = request.form.get("ap") 
#        # getting input with name = lname in HTML form 
#        insuline_level = request.form.get("il") 
#        # getting input with name = lname in HTML form 
#        bmi_value = request.form.get("bmi") 
#        # getting input with name = lname in HTML form 
#        age_of_person = request.form.get("dp") 
#        return "Your name is "+number_Pregnancies + gluco_selevel + blood_pressure + skin_thickness + age_person + insuline_level + bmi_value + age_of_person
#     return render_template("dashboard.html")



@app.route('/calculate', methods=['POST'])
def calculate():
    # Get form data
    number_Pregnancies = int(request.form['nop'])
    gluco_selevel = int(request.form['gl'])
    blood_pressure = int(request.form['bpv'])
    skin_thickness = int(request.form['stv'])
    age_person = int(request.form['ap'])
    insuline_level = int(request.form['il'])
    bmi_value = int(request.form['bmi'])
    age_of_person = int(request.form['dp'])
    
    # Calculate sum
    total = number_Pregnancies + gluco_selevel + blood_pressure + skin_thickness + age_person + insuline_level + bmi_value + age_of_person
    
    return f"The sum of the numbers is: {total}"

if __name__ == "__main__":
    app.run(debug=True, port=8000)