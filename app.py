from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here (optional for GPT)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return "Hello! I am a simple AI chatbot."

# Chatbot logic: receives user input and sends back a response
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Optionally integrate OpenAI GPT to handle the conversation
    response_message = get_ai_response(user_message)
    
    return jsonify({'response': response_message})

def get_ai_response(user_message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "gpt-3.5-turbo" or similar for newer models
            prompt=f'User: {user_message}\nAI:',
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        ai_message = response.choices[0].text.strip()
        return ai_message
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
