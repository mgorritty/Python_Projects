# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
words=[]
for line in fhand:
    line = line.rstrip()
    word_list = line.split()
    #words = [word_list[0]]
    for i in range(len(word_list)-1):
        if word_list[i] == word_list[i+1]:
            continue
        else:
            words.append(word_list[i])    
print words