with open('inputs/8_input.txt') as f:
    lines = f.read().splitlines()
    
del lines[1]

mapping = {'L': '0', 'R': '1'}

instruction = ''.join(mapping[char] for char in lines[0])

del lines[0]

map_dic = {}
starter_dic = {}
for line in lines:
    node = str(line.split(" = ")[0])
    coord = line.split(" = ")[1].strip("()").split(", ")
    map_dic[node] = coord 
    if node[-1] == 'A':
        starter_dic[node] = coord 
        
        
import threading

map_dic = {}
starter_dic = {}
for line in lines:
    node = str(line.split(" = ")[0])
    coord = line.split(" = ")[1].strip("()").split(", ")
    map_dic[node] = coord 
    if node[-1] == 'A':
        starter_dic[node] = coord 

step = ''
i = 0

def process_step(k, v):
    global starter_dic, map_dic
    step_answer.append(starter_dic[k][int(step)])
    starter_dic[k] = map_dic[starter_dic[k][int(step)]]

while True:
    step = instruction[i % len(instruction)]
    step_answer = []
    threads = []
    for k, v in starter_dic.items():
        t = threading.Thread(target=process_step, args=(k, v))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    i += 1
    if all(v[-1] =='Z' for v in step_answer):
        break
    
    if i%10000 == 0:
        print(i)
count = i

print(count)