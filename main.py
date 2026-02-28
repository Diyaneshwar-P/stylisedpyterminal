rows=int(input("Enter number of rows: "))
for i in range(rows):
    print(" "*(rows-i)+" *"*i)
print(' '*(i-2)+'{} rows'.format(rows))
for i in range(rows):
    print(" "*(i+1)+" *"*(rows-i-1))