stack=[]
stack2=[]
while len(stack)<10:
    y=int(input())
    stack.append(y)
for i in stack:
    x=i%42
    stack2.append(x)
set(stack2)
print(len(set(stack2)))
