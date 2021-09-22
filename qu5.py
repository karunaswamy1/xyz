string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
i=0
a=[]
while i<len(string_list):
    x=string_list[i]
    if x not in a:
        a.append(x)
    i=i+1
print(a)