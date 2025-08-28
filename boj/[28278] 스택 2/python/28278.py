# 스택 구현
import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def isEmpty(self):
        return True if self.count() == 0 else False

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

# 입력 받고 처리
n = int(input())
my_stack = Stack()

for _ in range(n):
    orders = list(map(int, input().split()))
    action = orders[0]

    if action == 1:
        my_stack.push(orders[1])

    elif action == 2:
        print(my_stack.pop())

    elif action == 3:
        print(my_stack.count())

    elif action == 4:
        if my_stack.isEmpty():
            print(1)
        else:
            print(0)

    elif action == 5:
        print(my_stack.peek())
