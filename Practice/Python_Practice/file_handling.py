f = open('data.txt','r')

# Read every line entire line
data = f.readlines()

# print the data
print(data)

# Close the file
f.close()