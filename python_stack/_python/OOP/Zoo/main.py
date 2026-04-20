class Animal:
    def __init__(self, name, age, health=20, happiness=30):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10
        
class Lion(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age) 
        self.tail_length = tail_length
        
class Tiger(Animal):
    def __init__(self, name, age, is_swimmer):
        super().__init__(name, age)
        self.is_swimmer = is_swimmer 
    def feed(self):
        self.health += 20
        self.happiness += 20
        print(f"The Tiger {self.name} loves the extra meat!")
        
class Monkey(Animal):
    def __init__(self, name, age, favorite_fruit):
        super().__init__(name, age)
        self.favorite_fruit = favorite_fruit
        
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_lion(self, name, age, tail_length):
        self.animals.append(Lion(name, age, tail_length))

    def add_tiger(self, name, age, is_swimmer):
        self.animals.append(Tiger(name, age, is_swimmer))
        
    def add_monkey(self, name, age, favorite_fruit):
        self.animals.append(Monkey(name, age, favorite_fruit))

    def print_all_info(self):
        print("-" * 20, self.zoo_name, "-" * 20)
        for animal in self.animals:
            animal.display_info()

my_zoo = Zoo("John's Zoo")
my_zoo.add_lion("Simba", 5, "Short")  #HEALTH=30 HAPPINESS=40
my_zoo.add_tiger("moukly", 3, True) #HEALTH=40 , HAPPINESS=50
my_zoo.add_monkey("mino", 7, "Banana")#HEALTH=30 ,HAPPINESS=40

for animal in my_zoo.animals:
    animal.feed()
    
my_zoo.print_all_info()