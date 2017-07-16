f=open("text.txt","r")
s=f.read()
binary=[]
for  i in range(len(s)):
    x=ord(s[i])
    b=[];
    for j in range(8):
        if((x&1)==1):
            b=b+['1']
        else:
            b=b+['0']
        x=x>>1
    b.reverse()
    binary=binary+b;
f.close()

l=len(binary)
r=int(l/2048)
bin_list=[]
for i in range(r):
    bin_list.append(binary[2048*i:(2048*(i+1))])
if(l%2048!=0):
    bin_list.append(binary[2048*r:])   
Gen="10001000000100001"
binList=[]
for temp in range(len(bin_list)):
    binar=''.join(bin_list[temp])
    binar=binar+"0000000000000000"
    d=list(Gen);
    t=list(binar);
    LastIndex=len(binar)-len(Gen);
    for i in range (0,LastIndex):
        if t[i]=="1":
           for j in range (i,i+len(Gen)):
               if(t[j]!=d[j-i]):
                   t[j]="1"
               else:
                   t[j]="0"
    t=''.join(t);
    binar=binar[:-16]+t[-16:]
    print(binar," ",len(binar))
    binList+=[binar]

binList=''.join(binList)

f=open("Binary_text.txt","w")
f.write(binList)
f.close()