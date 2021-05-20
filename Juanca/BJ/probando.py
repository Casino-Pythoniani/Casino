# a = [["1","1"],["1","1"]]
# b = a [:]
# a[0][0]="2"
# print (b)
# print(a)

# a = ["1"]
# b = a [:]
# a[0]="2"
# print (b)
# print (a)

a = [["1","1"],["1","1"]]
b=[]
for i in range (len(a)):
    c=[]
    c= (a [i])[:]
    b.append(c)
    

a[0][0]="2"
print (b)
print(a)