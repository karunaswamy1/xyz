list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
b=[]
while i<len(list2):
    x=list1[i]
    if x not in b:
        b.append(x)
        i=i+1
print(b)
        
        


    




    

        
        
    
    
    