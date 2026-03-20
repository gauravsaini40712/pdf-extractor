from flask import Flask, request, jsonify
from extract import extract_text
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "PDF Extractor API Running 🚀"

@app.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    file_path = "temp.pdf"
    file.save(file_path)

    text = extract_text(file_path)

    os.remove(file_path)

    return jsonify({
        "status": "success",
        "text": text
    })

if __name__ == "__main__":
    app.run()
