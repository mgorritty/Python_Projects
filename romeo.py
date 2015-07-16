# Ejercicio Lecture 8 - romeo.txt
# -------------------------------
fhand = open('romeo.txt')
flag = True
a =' '
for line in fhand: # lee las lineas en fhand
    line = line.rstrip() # quita lineas en blanco
    word_list = line.split() # separa la linea en word_list
    if flag:  
        word_list_final = [word_list[0]]
        flag = False
    for idx in word_list:
        if a == 'done':
            break
        for i in range(len(word_list_final)):    
            if idx != word_list_final[i]:
                word_list_final.append(idx)
            print i,idx, word_list_final, word_list_final[i]
            a = raw_input("sigo?")
            if a == 'done':
                break
            
       
        # #words = [word_list[0]]
    # for i in range(len(word_list)-1):
        # for j in range(len(word_list)-1):
            # print i,j, word_list[i], word_list[j+1]
            # if word_list[i] == word_list[j+1]:
                # continue
            # else:
                # words.append(word_list[i])
        # print words    
#print words