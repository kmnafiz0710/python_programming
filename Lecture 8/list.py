a="Amar sonar bangla, "
b="   Amar sonar bangla,         "
c=['Amar','sonar','bangla']
print(len(a))
print(a[1])
print(a*10)
print(a[5:17]) #5 index theke 17 index porjnoto
print(a[:17]) #Shuru theke 17 index porjnoto
print(a[5:]) #5 index theke sesh porjnoto
print(a[-8:-1]) #last er dik the count korte hobe,last diker -8 index theke -1 index porjnto.

print(a.lower())  #Converts the string to lowercase.
print(a.upper()) #Converts the string to uppercase.
print(a.capitalize())   #Capitalizes the first character of the sentence.
print(a.title())   #Capitalizes the first letter of every word
print(b.strip())   #first and last theke unusual comma remove kore.
print(a.count("a")) # word ti kotobar ache seta check kora.
print("".join(c))  #Joins a list of strings into one string.


# exercise 8.1

department=input("Enter your department name ")

print(department.lower())
print(department.upper())
print(department.capitalize())
print(department.title())

# exercise 8.2
x= input("To print each character,write something: ")
i=0
while i<len(x):
    print(x[i])
    i+=1


# exercise 8.3

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

full_name= first_name+" "+last_name
print("Hello, ",full_name)

print("\n")

my_list=[3414,154,25,65,45,767,89,6795,67,34,51,24,2,534,76,9780]
list2=[15,6,31,6,16,6,13,641,374457,24,7,1346,46,134,6]
print("The number of element are: ",len(my_list))
my_list[1]="Apple"    # replace the list item
my_list.append("Banana")
my_list.insert(1,"Jackfruits")
my_list.extend(list2)
for x in my_list:
    print(x)


a=['asdfagf','gag','bgrrwegdfsg']
my_list.sort()
print (my_list)

my_list.reverse()
print (my_list.count(89))

a.sort()
print (a)
