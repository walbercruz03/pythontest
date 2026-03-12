from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # habilita CORS para permitir chamadas do navegador

@app.route('/api/mensagem', methods=['POST'])
def mensagem():
    # pega os dados enviados pelo frontend
    dados = request.json

    # nome do arquivo
    arquivo = "dados.json"

    # se já existe, carrega o conteúdo
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = json.load(f)
    else:
        conteudo = []

    # adiciona os novos dados
    conteudo.append(dados)

    # salva novamente o arquivo
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(conteudo, f, ensure_ascii=False, indent=4)

    return jsonify({"msg": "Dados salvos com sucesso!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
