class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print('woof!')

    def say_name(self):
        print(f'woof {self.name}')

    def __height__(self):
        return self.height

    def __len__(self):
        return 5

# dunders/magic methods
# todo: get height of a dog

def height(obj):
    return obj.__height__()


if __name__ == '__main__':
    d = Dog('fred', 10)
    d.bark()

    l = [1,2,3]
    print(len(l))
    print(len(d))

    # print(height(d))