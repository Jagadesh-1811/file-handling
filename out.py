inp=input('enter some data')

with open ('outp.txt','w') as f:
    print(f.write(inp+'\n'))
with open ('outp.txt','r') as f:
    print(f.read())
with open ('outp.txt','a') as f:
    print(f.write('Learning file handling in python'))
with open ('outp.txt','r') as f:
    print(f.read())