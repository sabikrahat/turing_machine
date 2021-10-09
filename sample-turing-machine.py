import time
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class TuringMachine:
    states: set[str]
    symbols: set[str]
    blank_symbol: str
    input_symbols: set[str]
    initial_state: str
    accepting_states: set[str]
    transitions: dict[tuple[str, str], tuple[str, str, int]]

    head: int = field(init=False)
    tape: defaultdict[int, str] = field(init=False)
    current_state: str = field(init=False)
    halted: bool = field(init=False, default=True)

    def initialize(self, input_symbols):
        self.head = 0
        self.halted = False
        self.current_state = self.initial_state
        self.tape = defaultdict(lambda: "\033[31m~\033[0m", input_symbols)

    def step(self):
        if self.halted:
            raise RuntimeError('Cannot step halted machine')

        try:
            state, symbol, direction = self.transitions[(
                self.current_state, self.tape[self.head])]
        except KeyError:
            self.halted = True
            return
        self.tape[self.head] = symbol
        self.current_state = state
        self.head += direction

    def accepted_input(self):
        if not self.halted:
            raise RuntimeError('Machine still running')
        return self.current_state in self.accepting_states

    def print(self, window=30):
        print(f'{" " * (2 * window + 4)}\033[1;33m⮯\033[0m')
        print('\033[34m... \033[0m', end='')
        print("\033[1;32m ".join(self.tape[i] for i in range(
            self.head - window, self.head + window+12)), end=''"\033[0m")
        print(f'\033[1;34m >>> ( {self.current_state} )\033[0m\n')


def split(word):
    return [char for char in word]


def addition():
    tm = TuringMachine(states={'A', 'B', 'C', 'D', 'Accept'},
                       symbols={'0', '1'},
                       blank_symbol="\033[31m~\033[0m",
                       input_symbols={'1'},
                       initial_state='A',
                       accepting_states={'Accept'},
                       transitions={
        ('A', '1'): ('A', '1', 1),
        ('A', '+'): ('B', '1', 1),
        ('B', '1'): ('B', '1', 1),
        ('B', "\033[31m~\033[0m"): ('C', "\033[31m~\033[0m", -1),
        ('C', '1'): ('D', "\033[31m~\033[0m", -1),
        ('D', '1'): ('D', '1', -1),
        ('D', "\033[31m~\033[0m"): ('Accept', "\033[31m~\033[0m", 1),
    })

    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))

    str1 = ("1"*num1)+"+"
    str2 = ("1"*num2)

    unaryinput = str1+str2
    temp = (split(unaryinput))
    res = dict()
    for idx, ele in enumerate(temp):
        res[idx] = ele

    tm.initialize(res)

    while not tm.halted:
        tm.print()
        tm.step()


def subtraction():
    tm = TuringMachine(states={'A', 'B', 'C', 'D', 'E', 'Accept'},
                       symbols={'0', '1'},
                       blank_symbol='\033[31m~\033[0m',
                       input_symbols={'1'},
                       initial_state='A',
                       accepting_states={'Accept'},
                       transitions={
        ('A', '1'): ('B', '\033[31m~\033[0m', 1),
        ('B', '1'): ('B', '1', 1),
        ('B', '-'): ('B', '-', 1),
        ('B', '\033[31m~\033[0m'): ('C', '\033[31m~\033[0m', -1),
        ('C', '1'): ('D', '\033[31m~\033[0m', -1),
        ('C', '-'): ('E', '1', -1),
        ('D', '-'): ('D', '-', -1),
        ('D', '1'): ('D', '1', -1),
        ('D', '\033[31m~\033[0m'): ('A', '\033[31m~\033[0m', 1),
        ('E', '1'): ('E', '1', -1),
        ('E', '\033[31m~\033[0m'): ('Accept', '\033[31m~\033[0m', 1),
    })

    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    mx = max(num1, num2)
    mn = min(num1, num2)

    str1 = ("1"*mx)+"-"
    str2 = ("1"*mn)

    unaryinput = str1+str2
    temp = (split(unaryinput))
    res = dict()
    for idx, ele in enumerate(temp):
        res[idx] = ele

    tm.initialize(res)

    while not tm.halted:
        tm.print()
        tm.step()


def multiplication():
    tm = TuringMachine(states={'A', 'B', 'C', 'D', 'E', 'F', 'G' 'Accept'},
                       symbols={'0', '1'},
                       blank_symbol='\033[31m~\033[0m',
                       input_symbols={'1'},
                       initial_state='A',
                       accepting_states={'Accept'},
                       transitions={
        ('A', '1'): ('B', '\033[31m~\033[0m', 1),
        ('B', '1'): ('B', '1', 1),
        ('B', '*'): ('C', '*', 1),
        ('C', '1'): ('D', 'x', 1),
        ('D', '>'): ('D', '>', 1),
        ('D', '1'): ('D', '1', 1),
        ('D', '\033[31m~\033[0m'): ('E', '1', -1),
        ('E', '1'): ('E', '1', -1),
        ('E', '>'): ('E', '>', -1),
        ('E', 'x'): ('C', 'x', 1),
        ('C', '>'): ('F', '>', -1),
        ('F', 'x'): ('F', '1', -1),
        ('F', '*'): ('F', '*', -1),
        ('F', '1'): ('F', '1', -1),
        ('F', '\033[31m~\033[0m'): ('A', '\033[31m~\033[0m', 1),
        ('A', '*'): ('G', '\033[31m~\033[0m', 1),
        ('G', '1'): ('G', '\033[31m~\033[0m', 1),
        ('G', '>'): ('Accept', '\033[31m~\033[0m', 1),
    })

    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    mx = max(num1, num2)
    mn = min(num1, num2)

    str1 = ("1"*mn)+"*"
    str2 = ("1"*mx)+">"

    unaryinput = str1+str2
    temp = (split(unaryinput))
    res = dict()
    for idx, ele in enumerate(temp):
        res[idx] = ele

    tm.initialize(res)

    while not tm.halted:
        tm.print()
        tm.step()


def division():
    tm = TuringMachine(states={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'Accept'},
                       symbols={'0', '1'},
                       blank_symbol='\033[31m~\033[0m',
                       input_symbols={'1'},
                       initial_state='A',
                       accepting_states={'Accept'},
                       transitions={
        ('A', '1'): ('B', '\033[31m~\033[0m', 1),
        ('B', '1'): ('B', '1', 1),
        ('B', '/'): ('C', '/', 1),
        ('C', '1'): ('D', 'x', -1),
        ('D', '/'): ('D', '/', -1),
        ('D', '1'): ('D', '1', -1),
        ('D', '\033[31m~\033[0m'): ('A', '1', 1),
        ('C', 'x'): ('C', 'x', 1),
        ('D', 'x'): ('D', 'x', -1),
        ('A', '/'): ('E', '/', 1),
        ('E', 'x'): ('E', 'x', 1),
        ('E', '1'): ('E', '1', 1),
        ('E', '>'): ('E', '>', 1),
        ('E', '\033[31m~\033[0m'): ('F', '1', -1),
        ('F', '>'): ('F', '>', -1),
        ('F', '/'): ('F', '/', -1),
        ('F', '1'): ('F', '1', -1),
        ('F', 'x'): ('F', 'x', -1),
        ('F', '\033[31m~\033[0m'): ('A', '\033[31m~\033[0m', 1),
        ('C', '>'): ('G', '\033[31m~\033[0m', -1),
        ('G', 'x'): ('G', '\033[31m~\033[0m', -1),
        ('G', '/'): ('G', '\033[31m~\033[0m', -1),
        ('G', '1'): ('G', '\033[31m~\033[0m', -1),
        ('G', '\033[31m~\033[0m'): ('I', '\033[31m~\033[0m', 1),
        ('I', '\033[31m~\033[0m'): ('I', '\033[31m~\033[0m', 1),
        ('I', '1'): ('Accept', '1', -1),
    })

    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    mx = max(num1, num2)
    mn = min(num1, num2)

    str1 = ("1"*mn)+"/"
    str2 = ("1"*mx)+">"

    unaryinput = str1+str2
    temp = (split(unaryinput))
    res = dict()
    for idx, ele in enumerate(temp):
        res[idx] = ele

    tm.initialize(res)

    while not tm.halted:
        tm.print()
        tm.step()


if __name__ == '__main__':

    while True:
        print("*------------------------------------------*")
        print("*------------------------------------------*")
        print("|             Turning Machine              |")
        print("*------------------------------------------*")
        print("*------------------------------------------*")
        print("|        1. Addition of Two Number         |")
        print("|------------------------------------------|")
        print("|------------------------------------------|")
        print("|        2. Subtraction of Two Number      |")
        print("|------------------------------------------|")
        print("|------------------------------------------|")
        print("|        3. Multiplication of Two Number   |")
        print("|------------------------------------------|")
        print("|------------------------------------------|")
        print("|        4. Division of Two Number         |")
        print("|------------------------------------------|")
        print("|------------------------------------------|")
        print("|        5. Exit                           |")
        print("*------------------------------------------*")
        print("*------------------------------------------*")

        choice = int(input("\n\nEnter Your Choice: "))
        if(choice == 1):
            addition()
        if(choice == 2):
            subtraction()
        if(choice == 3):
            multiplication()
        if(choice == 4):
            division()
        if(choice == 5):
            print("*------------------------------------------*")
            print("*------------------------------------------*")
            print("|     Thank You for Using Out System       |")
            print("*------------------------------------------*")
            print("*------------------------------------------*")
            break
