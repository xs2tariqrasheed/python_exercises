# file = open('example.txt', 'a')
file = open('example.txt', 'r')

# file.writelines('The quick brown fox \n')
# file.writelines(['The', 'quick', 'brown'])
file.seek(4)
text = file.read(5)
# text = file.readline(80)
print(text)

file.close()
