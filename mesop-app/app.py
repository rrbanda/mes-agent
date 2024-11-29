# mesop-app/app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Mesop App is running"}), 200

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    # Example processing logic
    if not data or 'input' not in data:
        return jsonify({"error": "No input provided"}), 400

    input_data = data['input']
    # Simulate processing
    output_data = f"Processed: {input_data}"
    return jsonify({"output": output_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
