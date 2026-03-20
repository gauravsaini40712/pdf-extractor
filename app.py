  print("API HIT")

    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files['file']
    file_path = "temp.pdf"
    file.save(file_path)

    print("File saved")

    text = extract_text(file_path)
    print("DEBUG TEXT:", text[:200])  # 👈 add this
    os.remove(file_path)

    return jsonify({
        "status": "success",
        "text": text
    })

if __name__ == "__main__":
    app.run( host="0.0.0.0",   # ✅ IMPORTANT
        port=int(os.environ.get("PORT", 5000))  # ✅ IMPORTANT
           )
