#Write a program to check if a year is leap year or not.
#If a year is divisible by 4

input =1997
#print(input)
#print somewhereelse would have the function declaration
#def print (argument):....

#this is our function declaration
def leapYear(year):
    #check if year is divisible by 4
    # if we do %4 and there is no remainder, then it is divisible by 4

    # condition = year%4
    if(year % 4) == 0:
        return str(year) + " leap year "
    else:
        return str(year) + " not leap year "

# function call needs to be after function declaration (below it)
print(leapYear(input))
