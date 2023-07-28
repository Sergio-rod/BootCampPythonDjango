file = open('my_file.txt')


with open('my_file.txt', 'w') as f:
    f.write("now is a rile rewrite")

content = file.read()
print(content)
file.close()