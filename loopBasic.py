# Print all integers from 0 to 150.

for i in range(151):
    print(i)


# Print all the multiples of 5 from 5 to 1,000
for i in range(5, 10001, 5):
    print(i)


# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i%5:
        print('Coding')
    if i%10:
        print('Coding Dojo')

# Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for i in range(1,500001):
    if(i % 2 !=0):
        sum += i
print(sum)



# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    if(i %2 ==0):
        print(i)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)