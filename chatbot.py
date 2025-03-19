import nltk
from flask import Flask, request, jsonify

# Ensure required nltk data is available
nltk.download('punkt')

def simple_chatbot(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a chatbot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!"
    }
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm not sure how to respond to that."

# Flask API for chatbot
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = simple_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    print("Starting Chatbot API on http://127.0.0.1:5000/chat")
    app.run(debug=True, use_reloader=False)
