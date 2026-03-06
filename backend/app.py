from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/mensagem')
def mensagem():
    return jsonify({"msg": "Olá, Walber! Backend em Python funcionando."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
