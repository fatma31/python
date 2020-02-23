f = open(r'C:\Users\CODE\Desktop/lab.txt','r' )
if f.mode == 'r':
    contents = f.read()
    print(contents)