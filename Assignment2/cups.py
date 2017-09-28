x=1
y=0
z=0
moves=list(input("moves:").upper())
print(moves)
for i in moves:
    if i == "A":
        x ^= y
        y ^= x
        x ^= y
    elif i == "B":
        y ^= z
        z ^= y
        y ^= z
    elif i == "C":
        z ^= x
        x ^= z
        z ^= x
print(x,y,z)
if x ==1:
    print("1")
elif y == 1 :
    print("2")
elif z == 1:
    print("3")
