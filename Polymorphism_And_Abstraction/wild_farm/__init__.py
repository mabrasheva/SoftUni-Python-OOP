from project.animals.birds import Owl, Hen
from project.animals.mammals import Dog
from project.food import Meat, Vegetable, Fruit

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)

# hen = Hen("Harry", 10, 10)
# veg = Vegetable(0)
# fruit = Fruit(5)
# meat = Meat(0)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)

hen = Dog("Harry", 10, "home")
veg = Vegetable(0)
fruit = Fruit(5)
meat = Meat(10)
print(hen)
print(hen.make_sound())
print(hen.feed(veg))
hen.feed(fruit)
hen.feed(meat)
print(hen)