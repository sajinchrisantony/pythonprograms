#files
#read,write
# f1=open('abc','r')
# #print(f1)
# for i in f1:
#     print(i)
#r+ reading $ writing , w+ writing and reading
# f=open('abc','w')
# f.write("hai")
# f.write(" everyone")

# f=open('aaaa','w')
# f.write("hello")

#copy content from abc to new file
f1=open('abc','r')
f2=open('abcd','w')
for i in f1:
    f2.write(i)

