from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

class bruker:
    def __init__(self, brukernavn, passord, email):
        self.brukernavn = brukernavn
        self.passord = passord
        self.email = email
        self.spill = []

class spill:
    def __init__(self, navn, rating, bruker, tekst, dato):
        self.navn = navn
        self.rating = rating
        self.bruker = bruker
        self.tekst = tekst
        self.dato = dato

currentuser = None
brukere = [

]
spilllogg = [

]

@app.route("/")
def index():
    return render_template("index.html", spill=spilllogg)


@app.route("/CallLogout", methods=["GET", "POST"])
def CallLogout():

    logout()

    return "2"

def logout():
    global currentuser
    
    currentuser = None

@app.route("/spillregistrering", methods=["GET", "POST"])
def spillregistrering():
    if request.method == "POST":
        nyttspill = spill(
            request.form["spillnavn"],
            request.form["rating"],
            currentuser,
            request.form["kommentar"],
            datetime.datetime.now()
        )
        spilllogg.append(nyttspill)
        currentuser.spill.append(nyttspill)

    return render_template("spillregistrering.html",
                           user=currentuser)


@app.route("/profil", methods=["GET", "POST"])
def profil():
    global currentuser

    if currentuser != None:
        return render_template("profil.html",
                                brukernavn=currentuser.brukernavn,
                                passord=currentuser.passord,
                                email=currentuser.email)
    elif request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]
        email = request.form["email"]
        fantbruker = False
        for user in brukere:
            if user.brukernavn == brukernavn:
                fantbruker = True
                if user.passord == passord:
                    currentuser = user
                    return render_template("profil.html",
                                            brukernavn=currentuser.brukernavn,
                                            passord=currentuser.passord,
                                            email=currentuser.email)
                else:
                    print("Feil Passord")
          
        if fantbruker == False:
            currentuser = bruker(brukernavn, passord, email)

            brukere.append(currentuser)

            return render_template("profil.html",
                               brukernavn=currentuser.brukernavn,
                               passord=currentuser.passord,
                               email=currentuser.email)
    return render_template("profilregistrering.html")

@app.route("/registrering")
def registrering():
    return render_template("registrering.html")

if __name__ == "__main__":
    app.run(debug=True)