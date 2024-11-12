r=(ord(input())-97)*2+1;m=int(n/2)
for y in range(n):l=["."]*n;f=m-abs(m-y);c=chr(f+97);l[m-f]=c;l[m+f]=c;print(l)
