
print()
my_list = [ 50 , 51 , 52 , 53 , 52 , 50, 12, 5, 3, "Hellow" , "Test", "A" , 99 ]
print(my_list)

# for i in range( 5 , len(my_list) - 1):
#     print( f'Index:{i} = {my_list[i]}' )

# for x in my_list:
#     if (type(x) == int and x < 99 and x != 50) or x == "Test":
#         print(x)

my_dictionary = {
    "name": "Mr Rosas"
}

my_dictionary["city"] = "Xalapa"
my_dictionary["favorite_movies"] = ["Star Wars" , "LOTR" , "Dune"]

for key , value in my_dictionary.items():
    print(key)

print(my_dictionary)