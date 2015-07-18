# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
newline = '' # inicializa acumulador de lineas
word_acc =[] # lista vacia para append
for line in fhand:       # lee las lineas en fhand
    line = line.rstrip() # quita linea final en blanco
    newline = newline +' '+ line # acumula lineas de romeo.txt
romeo_list = newline.split() # convierte string en lista
# ----------------------------
for idx in romeo_list:
    flag = False
    for i in range(len(romeo_list)):
        if idx == romeo_list[i]:
            if flag == False:
                word_acc.append(idx)
                flag = True    
# nueva estrategia: volver todo el archivo romeo en lista y
# luego hacer la selección en esa lista total         
            