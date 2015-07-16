# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
idx=0
for line in fhand:
    line = line.rstrip()
    word_list = line.split()
    for i in range len(word_list):
        
        
    #usar word[i] in word
    #porque word es una lista con las palabras
    #uego usar append.
    print word
    print len(word_list)