from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Le serveur fonctionne 🎉"

@app.route("/signalement", methods=["GET", "POST"])
def signalement():
    if request.method == "POST":
        zone = request.form.get("zone")
        description = request.form.get("description")
        print("Signalement reçu :", zone, description)
        return "Merci, le signalement a été envoyé."

    return """
    <h2>Signalement d’anomalie</h2>
    <form method="post">
        <input name="zone" placeholder="Zone" required><br><br>
        <textarea name="description" placeholder="Description" required></textarea><br><br>
        <button type="submit">Envoyer</button>
    </form>
    """

if __name__ == "__main__":
    app.run()
