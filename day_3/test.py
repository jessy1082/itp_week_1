list_4 = ["abc", 34, True, 40, "male"]
list_5 = [["John", "Smith"], ["Jane", "Doe"]]
print(type(list_5)) # <class 'list'>
print(len(list_5)) # 2


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[0]) # "apple"
print(fruits[-1]) # "mango"
print(fruits[-7]) # "apple"
print(fruits[2:5]) # ['cherry', 'orange','kiwi']
print(fruits[:4]) # "apple", "banana", "cherry", "orange" # NOT INCLUDE KIWI
print(fruits[2:]) # "cherry", "orange", "kiwi", "melon", "mango"
print(fruits[-4:-1]) # "orange" (-4) to, but NOT including "mango" (-1)


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")

  fruits[0] = "strawberry"
print(fruits)

fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)

more_fruits = ["raspberry", "coconut", "pineapple"]
more_fruits[1:2] = ["grape", "durian"]
print(more_fruits)

sports = ["football","soccer","baseball"]
sports.append("lacrosse")
print(sports)


