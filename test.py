import queue

num = queue.Queue()
num1 = queue.Queue()
num.put(2)
num.put(3)
while not num.empty():
    num1.put(num.get())
print(num1.get())
print(num1.get())
