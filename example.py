class Person:
    class Child:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Child(name={self.name}, age={self.age})"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child_name, child_age):
        child = self.Child(child_name, child_age)
        self.children.append(child)

    # Making the Person class iterable over the children
    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, children={self.children})"

# Example usage:
p = Person("John", 40)
p.add_child("Anna", 10)
p.add_child("Ben", 8)

# Iterating over the children in the person
for child in p:
    print(child)
