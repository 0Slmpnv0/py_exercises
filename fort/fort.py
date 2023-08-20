class Stack:
    def __init__(self, numberass=None):
        if numberass is None:
            numberass = []
        self.__numberass = numberass

    def run_command(self, command):

        if command == 'DROP':
            if not self.__numberass:
                self.error()
            self.__numberass.pop()

        elif command == 'SWAP':
            if len(self.__numberass) < 2:
                self.error()
            last_element = self.__numberass[len(self.__numberass) - 1]
            pre_last_element = self.__numberass[len(self.__numberass) - 2]

            self.__numberass[len(self.__numberass) - 1], self.__numberass[len(self.__numberass) - 2] = pre_last_element, last_element

        elif command == 'DUP':
            if not self.__numberass:
                self.error()
            self.__numberass.append(self.__numberass[len(self.__numberass) - 1])

        elif command == 'OVER':
            if len(self.__numberass) < 2:
                self.error()
            self.__numberass.append(self.__numberass[len(self.__numberass) - 2])

        elif command == '+':
            if len(self.__numberass) < 2:
                self.error()



    def error(self):
        print('ERROR')
        exit()


if __name__ == '__main__':
    with open('input.txt') as file:
        commands = file.read().split('\n')

    stack = Stack()

    for command in commands:
        stack.run_command(command)

