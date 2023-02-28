from project.food import Food
from project.fruit import Fruit

apple = Fruit("Apple Name", "28.02.2023")
bread = Food("29.02.2023")
print(apple.expiration_date)
print(apple.name)
print(bread.expiration_date)