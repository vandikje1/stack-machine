class StackMachine:
    def __init__(self, data):
        self.data = data
        self.stack = []

    def push(self, number):
        self.stack.append(number)
        print(f"PUSH {number}")

    def pop(self):
        number = self.stack.pop()
        print("POP")
        return number

    def handle_operator(self, char):
        second = self.pop()
        first = self.pop()
        if char == "+":
            result = first + second
            print(f"ADD {first}, {second}")
        elif char == "-":
            result = first - second
            print(f"SUB {first}, {second}")
        else:
            raise ValueError(f"unknown char: {char}")
        self.push(result)

    def execute(self):
        number = ""

        for char in self.data:
            if char.isdigit():
                number += char
            elif char.isspace():
                if number:
                    self.push(int(number))
                    number = ""
            else:
                self.handle_operator(char)
        result = self.pop()
        print(result)
        return result


stack_machine = StackMachine("14 2 + 6 5 - +")
stack_machine.execute()
