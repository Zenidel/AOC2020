# file handling 

# 1) without using with statement 
#file = open('file_path', 'w') 
#file.write('hello world !') 
#file.close() 

# 2) without using with statement 
#file = open('file_path', 'w') 
#try: 
#	file.write('hello world') 
#finally: 
#	file.close() 

# using with statement 
#with open('file_path', 'w') as file: 
#	file.write('hello world !') 
###############################################

with open('inputday1.txt', 'r') as f:
    newlines = f.readlines()

# Strips the newline character 
#    print [ format(line.strip()) for line in Lines ]

numbersonly = [ int(line.strip()) for line in newlines ]

print(numbersonly)

# using range for iteration 
#l = [10, 20, 30, 40] 
#for i in range(len(l)): 
#    print(l[i], end =" ") 
#print() 

for first in range(len(numbersonly)):
    for second in range(len(numbersonly)):
        num1 = numbersonly[first]
        num2 = numbersonly[second]

        if num1+num2 == 2020:
            balance = num1 * num2


print(balance)

