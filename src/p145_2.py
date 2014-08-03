sum=0

for i in range(1,10):
 	if i%2==0:
  		sum=sum+(20*(30**(i/2)-1))
 	elif i%4==0:
  		sum=sum
 	elif i%4==3:
  		sum=sum+(5*20*((25*20)**(i/4)))

print sum