from flask import Flask, render_template
import os
import json

app = Flask(__name__)


# ==========================
# PÁGINA INICIAL
# ==========================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================
# PÁGINA DA SENHA
# ==========================

@app.route("/senha")
def senha():
    return render_template("senha.html")


# ==========================
# HISTÓRIA
# ==========================

@app.route("/historia")
def historia():

    caminho_conteudo = os.path.join(app.root_path, "conteudo.json")

    try:
        with open(caminho_conteudo, "r", encoding="utf-8") as arquivo:
            conteudo = json.load(arquivo)
    except Exception as erro:
        print("ERRO AO LER conteudo.json:", erro)
        conteudo = {}

    fotos = [
        "WhatsApp Image 2026-09-21 at 15.36.12.jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.13.jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.13 (1).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.13 (2).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.13 (3).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.14.jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.14 (1).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.14 (2).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.14 (3).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.15.jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.15 (1).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.15 (2).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.15 (3).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.16.jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.16 (1).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.16 (2).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.16 (3).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.17 (1).jpeg",
        "WhatsApp Image 2026-09-21 at 15.36.17.jpeg"
    ]

    return render_template(
        "historia.html",
        fotos=fotos,
        conteudo=conteudo
    )


# ==========================
# INICIAR SERVIDOR
# ==========================

if __name__ == "__main__":
    app.run(debug=True)