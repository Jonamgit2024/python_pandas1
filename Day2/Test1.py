

# a file named "geek", will be opened with the reading mode.
with open('Test1.txt', 'w') as f1:
    f1.write("Hello World")
    f1.close()

f=open('Test1.txt', 'r')
# This will print every line one by one in the file
for each in f:
    print (each)
