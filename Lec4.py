# LEC 4 basic input , strings operators  , escape sequences  todays topics



# input is a function which takes input from user and returns it as string


name = input("Enter your name : ")  # take inpur from user and store it in name variable
education=input("Enter your education : ")

print("Hy , My self " , name ," I am  a Student of  " + education)  # return the store input  in the var and print it in the format we want and aslo we contcatenate var  by usinf + operator and also we can use , operator to print the var and string together



# Printing with seperator  ,  end , escape sequence 


#  Normal print statement
print("Hello World , This is a simple print statement ")  # print Hello World


# print with sepeartor (sep)
# sep is used to separate the values with a specific character or string  or any thing else we want to use as a separator between the characters or values we want to print
name1 ='sumaira ramzan'

print ("MySelf ", name1 , end="and here the ( , ) is the separator")  # print MySelf - sumaira ramzan


# print with end
# end is used to specify what to print at the end of the print statement instead of the default newline character (\n) we can use end to specify what to print at the end of the print statement

print("This is about the end  statement", end="And  i am at the end of the line ")



# Escape sequences
# Escape sequences are special characters that are used to represent certain characters or actions in a string. They are represented by a backslash (\) followed by a specific character or sequence of characters.

# new line 
#  \n is used to print the next line in a new line
print("This is the first line \nThis is the second line")  # print This is the first line and This is the second line in new line

# tab space 
# tab space is used to print the next line with a tab space in between
print("This is the first line \tThis is the second line")  # print This is the first line and This is the second line with a tab space in between

# backslash
# backslash is used to print a literal backslash character
print("This is a backslash: \\")  # print This is a backslash: \


# for  quote
# to print a single quote we can use \' and to print a double quote we can use \" 
print("This is a single quote: \'")  # print This is a single quote: '
print("This is a double quote: \"")  # print This is a double quote:

# f string
# f string is a string literal that is prefixed with 'f' or 'F' and allows us to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the __format__ protocol.

name2 = "sumaira"
age = 20
print(f"My name is {name2} and I am {age} years old")  # print My name is sumaira and I am 20 years old

