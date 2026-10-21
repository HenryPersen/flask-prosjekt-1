from flask import Flask, render_template, request, jsonify

brukernavn = None
passord = None
email = None

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


    

@app.route("/CallLogout", methods=["GET", "POST"])
def CallLogout():

    logout()

    return "2"

def logout():
    global brukernavn
    global passord
    global email
    
    brukernavn = None
    passord = None
    email = None

@app.route("/profil", methods=["GET", "POST"])
def profil():
    global brukernavn
    global passord
    global email
    if brukernavn != None:
        return render_template("profil.html",
                                brukernavn=brukernavn,
                                passord=passord,
                                email=email)
    elif request.method == "POST":
        brukernavn = request.form["brukernavn"]

        passord = request.form["passord"]

        email = request.form["email"]

        return render_template("profil.html",
                               brukernavn=brukernavn,
                               passord=passord,
                               email=email)
    return render_template("registrering.html")

@app.route("/registrering")
def registrering():
    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)