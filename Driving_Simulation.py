t=int(input('time'))
d=int(input('distance'))
a=int(input('xlr8(acceleration)'))
v=a*t
for i in range (t+1):
    print('duration:',i,'distance:','*'*(int(((a*(i**2))/2)/10)))
if (a*t**2)/2==d:
    print("the person reached his destination", 'distance reached',int((a*(i**2))/2),"meters")
else:
    print('did not reach destination', 'distance reached',int((a*(i**2))/2),"meters")
if (v>60):
    print("went over speed limit", 'reached',v,'m/s')
else:
    print("not over speed limit", 'reached',v,'m/s')

