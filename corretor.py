import re
import os

def fix_line_breaks(text):
    aux = text.split("\n")[:4]
    #aux2 = text.split("\n")[24:27]
    lines = text.split("\n")[4:]
    fixed_lines = []
    for i in range(len(lines)):
        if i > 0 and not lines[i - 2].strip().endswith(('.', '"', '”', "*")):
            fixed_lines[-1] += '' + lines[i].strip()
        else:
            fixed_lines.append(lines[i].strip())
    certo = "\n\n".join(fixed_lines)
    return "\n".join(aux) + "\n" + certo # + "\n".join(aux2)

if __name__ == "__main__":
    i=0
    caps=[]
    while i<324:
        if i<9:
            caps.append(f'cap0{i+1}.txt')
        else:
            caps.append(f'cap{i+1}.txt')
        i+=1
        
    input_dir = output_dir = "C:\\Users\\edupo\\Desktop\\Pessoal\\Programas\\Biblioteca\\Livros\\Super Powereds - Year 4"

    for c in range(i):
        input_file = os.path.join(input_dir, caps[c])
        output_file = os.path.join(output_dir, caps[c])
        
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        fixed_content = fix_line_breaks(content)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(fixed_content)
        
    print(f"Correção concluída! O arquivo corrigido foi salvo em {output_file}")