# Object Oriented Programming
# inheritance

class AnimalActions:
	def quack(self): return self.strings['quack']
	def feathers(self): return self.strings['feathers']
	def bark(self): return self.strings['bark']
	def fur(self): return self.strings['fur']

class Duck(AnimalActions):
	strings = dict(
		quack = "Quaaack",
		feathers = "The duck has a gray and white feathers",
		bark = "The Duck cannot Bark",
		fur = "The Duck has not fur")
	
class Person(AnimalActions):
	strings = dict(
		quack = "The person imitates a duck.",
		feathers = "The person takes a feather from ground and shows it.",
		bark = "The Person says woof!",
		fur = "The person puts on a fur coat")

class Dog(AnimalActions):
	strings = dict(
		quack = "The Dog cannot quack.",
		feathers = "The dog has no feathers.",
		bark = "Arf!",
		fur = "The Dog has white fur white black spots.")

def in_the_doghouse(dog):
	print(dog.bark())
	print(dog.feathers())

def in_the_forest(duck):
	print(duck.bark())
	print(duck.fur())


def main():
	donald = Duck()
	john = Person()
	fido = Dog()

	print("- In the forest:")
	for o in (donald, john, fido):
		in_the_forest(o)

	print("- In the doghouse:")
	for o in (donald, john, fido):
		in_the_doghouse(o)

if __name__ == "__main__": main()