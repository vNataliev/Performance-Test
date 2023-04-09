import time

N = 120

def swap(line):
    returned_line = ""
    for character in line:
        if ("A" <= character <= "Z"):
            character = chr(ord(character) + 32)
        elif ("a" <= character <= "z"):
            character = chr(ord(character) - 32)
        returned_line += character
    return returned_line


file = open('input_2.txt', 'r')
lines = []
for line in file:
    lines.append(line)
file.close()

print(f"read file {len(lines)}")

start_func = time.time()
for i in range(N):
    for line in lines:
        swap(line)
end_func = time.time()
func_time = end_func - start_func

start_loop = time.time()
for i in range(N):
    for line in lines:
        pass
end_loop = time.time()
loop_time = end_loop - start_loop

print("Empty loop: ", loop_time , " s ")
print("Loop with calculation: ",func_time, " s ")
print("Proper Loop: ",func_time-loop_time, " s ")


#print('Execution time:', elapsed_time/1000000, 'miliseconds')


