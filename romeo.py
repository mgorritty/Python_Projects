# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
newline = ''
word_acc = []
for line in fhand: # lee las lineas en fhand
    line = line.rstrip() # quita lineas en blanco
    newline = newline +' '+ line
    word_list = line.split() # separa la linea en word_list
    for idx in word_list:
        if newline.find(idx) != -1:
            word_acc.append(idx)
            
            