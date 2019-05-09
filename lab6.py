#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list


class Stack:
    #Create a New Empty Stack
    def __init__(self):
        self.__S = []
    #Display the Stack
    def __str__(self):
        return str(self.__S)
    #Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
    #Remove the top element from stack
    def pop(self):
        return self.__S.pop()
    #See what element is on top of stack
    #Leaves stack unchanged
    def top(self):
        return self.__S[-1]


def postfix(exp):
    stack = Stack()
    listExp = exp.split(' ')
    for x in listExp:
        try:
            intX = float(x)
            stack.push(intX)
        except ValueError:
            operator = x
            number1 = stack.pop()
            number2 = stack.pop()
            if operator == '+':
                finalNumber = number2 + number1
            elif operator == '-':
                finalNumber = number2 - number1
            elif operator == '*':
                finalNumber = number2 * number1
            else:
                finalNumber = number2 / number1
            stack.push(finalNumber)
    return stack.top()


print('Welcome to Postfix Calculator')
print('Enter exit to quit.')
loop = True
while loop:
    userInput = input('Enter Expression:\n')
    if userInput.lower() == 'exit':
        loop = False
    else:
        print('Result:', postfix(userInput))
