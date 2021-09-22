string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
i=0
b=[]
while i<len(string_list):
    x=string_list[i]
    if x not in b:
        b.append(x)
    i=i+1
print(b)
    
        
        
    
    
    
    
