class FruitBasket():
    fruits: list = []
    color: str
    def __init__(self, color):
        self.color = color

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def generator(self):
        self.fruits = ["apple", "banana", "orange"]

b1 = FruitBasket("brown")
b1.add_fruit("OST")
fruits1 = b1.fruits
print(fruits1)

b2 = FruitBasket("green")
b2.generator()
fruits2 = b2.fruits
print(fruits2)
            


    

