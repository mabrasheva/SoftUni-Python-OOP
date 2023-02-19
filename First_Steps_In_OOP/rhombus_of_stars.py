# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n.

class Rhombus:
    def __init__(self, size: int):
        self.size = size

    def print_rhombus(self):

        for i in range(1, self.size):
            for row in range(self.size - i):
                print(" ", end="")
            for row in range(1, i):
                print("*", end=" ")
            print("*")

        for i in range(self.size, 0, -1):
            for row in range(self.size - i):
                print(" ", end="")
            for row in range(1, i):
                print("*", end=" ")
            print("*")


result = Rhombus(int(input()))
result.print_rhombus()
