#i=1,π=0
#while 1: π+=4/(i*2-1)*(i%2*2-1);i+=1;print(π)
import math as m
i=1
while 1:
    print(i*m.sin(m.pi/i))
    i+=1

#import math
#print(math.radians(180))

