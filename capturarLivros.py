import os
import json

LIVROS_DIR = "Livros"

def gerar_lista_livros():
    livros = []
    for pasta in os.listdir(LIVROS_DIR):
        caminho_completo = os.path.join(LIVROS_DIR, pasta)
        if os.path.isdir(caminho_completo):
            imagem_path = os.path.join(caminho_completo, "capa.png")
            contador_txt = sum(1 for f in os.listdir(caminho_completo) if f.endswith('.txt'))
            if os.path.exists(imagem_path):
                livros.append({
                    "titulo": pasta,
                    "caminho": pasta,
                    "imagem": imagem_path.replace("\\", "/"),
                    "txt_count": contador_txt
                })

    with open("livros.json", "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)
        
    print("Lista de livros atualizada!")

if __name__ == "__main__":
    gerar_lista_livros()