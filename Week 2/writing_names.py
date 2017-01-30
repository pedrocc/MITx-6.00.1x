

nameHandle = open('kids', 'w')

for i in range(2):
    nameHandle.write(input("qual o nome que deseja dar? "))
    nameHandle.write("\n")
nameHandle.close()

nameHandle = open('kids', 'r')
for i in nameHandle:
    print(i)
nameHandle.close()