# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
word_acc =[] # lista vacia para append
for line in fhand:       # lee las lineas en fhand
    line = line.rstrip() # quita linea final en blanco
    romeo_list = line.split() # convierte string en lista
# ----------------------------
    for idx in romeo_list:
        if idx in word_acc:
            continue
        word_acc.append(idx)
word_acc.sort()
print word_acc
            
#Create blank list
#Open file
#Read file one line at a time
#Break the line into words
#Step through the list of words one item at a time
#Does the current word already exist in the list you created at the top of your program?
#If not then add it to the list.
#Once your out of all the loops sort the list
#print the list                               
                    
#cheeses = ['Cheddar', 'Edam', 'Gouda']
#>>> 'Edam' in cheeses
#True
#>>> 'Brie' in cheeses
#False                    