import random
from threading import Thread
from threading import Lock

input_list = [1]
lines_list = 1000
thread_count = 100
line_length = int(10000/thread_count)
x = 1

def generateLine(len):
    line = ""
    for i in range(len):
        x = random.randrange(0,100)
        if (x >= 30):
            if (x > 64):
                line += chr(random.randrange(65, 91))
            else:
                line += chr(random.randrange(97, 123))
        else:
            if (x >= 10):
                line += chr(random.randrange(33, 65))
            elif (x >= 20):
                line += chr(random.randrange(91, 97))
            else:
                line += chr(random.randrange(123, 127))
    return line + '\n'

def task(file, lock, length):
    # task loop
    for f in range(int(length/10)):
        character = ""
        for b in range(10):
            d = random.randrange(0, 100)
            if (d >= 30):
                if (d > 64):
                    character += chr(random.randrange(65, 91))
                else:
                    character += chr(random.randrange(97, 123))
            else:
                if (d >= 10):
                    character += chr(random.randrange(33, 65))
                elif (d >= 20):
                    character += chr(random.randrange(91, 97))
                else:
                    character += chr(random.randrange(123, 127))
        with lock:
            file.write(character)


# for element in input_list:
#     input_title = f'input_{element}.txt'
#     with open(input_title, 'w') as file:
#         for line_count in range(lines_list[element-1]):
#             file.write(generateLine(line_length))

lock = Lock()
# defile the shared file path
filepath = 'input_2.txt'
# open the file
file = open(filepath, 'a')
# configure many threads
for i in range(lines_list):
    with lock:
        file.write("\n")
    threads = [Thread(target=task, args=(file, lock, line_length)) for _ in range(thread_count)]
    # start threads
    for thread in threads:
        thread.start()
    # wait for threads to finish
    for thread in threads:
        thread.join()
# close the file
file.close()
