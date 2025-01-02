liste = ["test", "sett","set"]
s_liste = [ sorted(i) for i in liste ]
angram_l= []
for i in range (len(s_liste)):
    #print(i ,f"===>{s_liste[i]}")
    for j in s_liste[i+1:]:
        if s_liste[i]== j:
            angram_l.append([liste[i],liste[s_liste[i+1:].index(j)+i+1]])
            
        #print (j)
"""for i in liste:
    angram_l.append(liste)"""
#print (angram_l)


#=== améliration utilsant les dictionnaires



dic={}
for i in liste: 
    sorted_x = "".join(sorted(i))
    if sorted_x in dic.keys():
        dic[sorted_x].append(i)
    else:
        dic[sorted_x]= [i]

print(dic)

