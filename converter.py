import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import os
import time
import re
from docx import Document

def extract_text_from_docx_to_txt(docx_path):
    docx_path = docx_path.strip("{}")
    doc = Document(docx_path)
    filename = os.path.basename(docx_path)
    folder_name = os.path.splitext(filename)[0]
    livros_dir = os.path.join(os.getcwd(), "Livros")
    if not os.path.exists(livros_dir):
        os.makedirs(livros_dir)
    
    folder_path = os.path.join(livros_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    chapter_text = []
    chapter_count = 1

    for para in doc.paragraphs:
        if re.match(r'^\d+\.', para.text) or "Chapter" in para.text:
        #if para.text.startswith(para.text.isnumeric()) or "CHAPTER" in para.text:
            if chapter_text:
                save_chapter_to_txt(chapter_text, folder_path, chapter_count)
                chapter_count += 1
                chapter_text = []
        chapter_text.append(para.text)
    
    if chapter_text:
        save_chapter_to_txt(chapter_text, folder_path, chapter_count)

    print(f"Texto extraído e salvo em {chapter_count - 1} arquivos.")


def save_chapter_to_txt(chapter_text, folder_path, chapter_count):
    output_txt = os.path.join(folder_path, f"cap{str(chapter_count).zfill(2)}.txt")
    final_text = "\n\n".join(chapter_text)
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(final_text)
    print(f"Capítulo {chapter_count} salvo em: {output_txt}")


def on_drop(event):
    docx_path = event.data
    extract_text_from_docx_to_txt(docx_path)
    status_label.config(text=f"Arquivo processado com sucesso!")
    time.sleep(3)
    status_label.config(text=f"Status: Aguardando arquivo")

root = TkinterDnD.Tk()
root.title("Conversor de DOCX para TXT")
root.geometry("400x400")
root.configure(bg="#121212")
root.resizable(False, False)

title_label = tk.Label(root, text="Arraste e solte um arquivo .docx aqui", font=("Arial", 14), bg="#121212", fg="#B7B7B7")
title_label.pack(pady=20)

drop_area = tk.Label(root, text="Arraste o arquivo .docx aqui", bg="#202020", width=40, height=10, fg="#B7B7B7", font=("Arial", 12))
drop_area.pack(pady=30)
drop_area.bind("<Enter>", lambda e: drop_area.config(bg="#303030"))
drop_area.bind("<Leave>", lambda e: drop_area.config(bg="#202020"))

status_label = tk.Label(root, text="Status: Aguardando arquivo", bg="#121212", fg="#B7B7B7", font=("Arial", 10))
status_label.pack(pady=20)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
