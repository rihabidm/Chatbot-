from flask import Flask, request, jsonify, render_template
from chatbot import Chatbot

app = Flask(__name__)

# Configuration
API_KEY = ""
MODEL_NAME = "gemini-1.5-flash"

# Initialisation du chatbot
chatbot = Chatbot(API_KEY, MODEL_NAME)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'Message vide'}), 400
    
    try:
        # Obtient la réponse du chatbot
        response = chatbot.get_response(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
