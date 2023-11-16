from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'INDIA'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    # Use GPT-3 to generate a response
    prompt = f"Q: {user_input}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100  # You can adjust this based on the desired response length
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
