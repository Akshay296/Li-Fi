f=open("Binary_text.txt","r")
s=f.read()
f.close()

r=int(len(s)/2064)
rx_list=[]
for t in range(r):
    rx_list.append(s[t*2064:(t+1)*2064])
if(len(s)%2064!=0):
    rx_list.append(s[r*2064:])
    
#print(rx_list," ",len(rx_list))
Gen="10001000000100001";
Genl=list(Gen);

f=open("Receive_text.txt","w")
for t in range(len(rx_list)):
    Rx=rx_list[t]
    Rxl=list(Rx)
    LastIndex=len(Rx)-len(Gen)
    for i in range (0,LastIndex):
        if Rxl[i]=='1':
           for j in range (i,i+len(Gen)):
            if(Rxl[j]==Genl[j-i]):
                Rxl[j]='0';
            else:
                Rxl[j]='1';
    Check=''.join(Rxl);
    print(Check," ",len(Check))
    if "1" in Check:
        print("Error")
    else:
        print("No Error")
        f.write(Rx)
f.close()