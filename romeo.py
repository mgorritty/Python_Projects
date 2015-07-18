# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
newline  = ''
word_acc = []
for line in fhand: # lee las lineas en fhand
    line = line.rstrip() # quita lineas en blanco
    newline = newline +' '+ line
    word_list = line.split() # separa la linea en word_list
    for idx in word_list:
        for i in range(len(newline)):            
            
            word_acc.append(idx)
 
# nueva estrategia: volver todo el archivo romeo en lista y
# luego hacer la selección en esa lista total         
            