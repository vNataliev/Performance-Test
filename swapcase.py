import time

N = 3500

file = open('input_2.txt', 'r')
lines = []
for line in file:
    lines.append(line)
file.close()

print(f"read file {len(lines)}")

start_func = time.time()
for i in range(N):
    for line in lines:
        line = line.swapcase()
end_func = time.time()
func_time = end_func - start_func

# file.close()

# file = open('input_1.txt', 'r')

start_loop = time.time()
for i in range(N):
    for line in lines:
        pass
end_loop = time.time()
loop_time = end_loop - start_loop

print("Empty loop: ", loop_time , " s ")
print("Loop with calculation: ",func_time, " s ")
print("Proper Loop: ",func_time-loop_time, " s ")
