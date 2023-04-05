from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure the OpenAI API
openai.api_key = "enter-your-api-key"

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.json['prompt']

    # Send the text prompt to the OpenAI API
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0,
    )

    # Extract the generated text and return it as JSON
    generated_text = response.choices[0].text.strip()
    return jsonify({"generated_text": generated_text})

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from the frontend
@app.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    header["Access-Control-Allow-Headers"] = "Content-Type"
    header["Access-Control-Allow-Methods"] = "POST"
    return response

if __name__ == '__main__':
    app.run(debug=True)