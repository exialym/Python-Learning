f = open('data.txt', 'w')
f.write("balalala")
f.close()
f = open('data.txt')
print(f.read())
