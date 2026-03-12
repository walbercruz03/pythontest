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

    arquivo = "dados.json"

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = json.load(f)
    else:
        conteudo = []

    conteudo.append(dados)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(conteudo, f, ensure_ascii=False, indent=4)

    return jsonify({"msg": "Dados salvos com sucesso!"})

@app.route('/api/dados', methods=['GET'])
def listar_dados():
    arquivo = "dados.json"
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = json.load(f)
    else:
        conteudo = []
    return jsonify(conteudo)

@app.route('/api/dados', methods=['DELETE'])
def excluir_dados():
    arquivo = "dados.json"
    if os.path.exists(arquivo):
        os.remove(arquivo)
        return jsonify({"msg": "Todos os dados foram excluídos!"})
    else:
        return jsonify({"msg": "Nenhum dado encontrado para excluir."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
