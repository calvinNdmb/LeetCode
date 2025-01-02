#========== easy way
num=[1,2,3,4,5,5]
a=[]
for i in num:
    if i not in a:
        a.append(i)
    else:
        print (f"contains duplicate : {i}")
        break

#========== set way

test = set(num)
if list(test)== num:
    print ("no duplicate")
else:
    print ("contains duplicate")

