testing = False
filename = "day5-sample" if testing else "day5-data"
is_part2 = True
def first_value_address(stack):
    for i in range(len(stack)):
        if stack[i]:
            return i
    return 0

class Instruction:
    def __init__(self, num, src, dest):
        self.num = int(num)
        self.src = int(src) - 1 #numbers given are 1-indexed instead of 0
        self.dest = int(dest) - 1

    def apply(self, data, keep_order=False):
        print(len(data), self.src, self.dest)
        print(f"applying rule {self.num} pieces from {self.src} to {self.dest}")
        print(f"src: {data[self.src]}\ndest: {data[self.dest]}")
        srctop = first_value_address(data[self.src])
        if keep_order:
            srctop += (self.num-1)
        desttop = first_value_address(data[self.dest])
        value = ""
        for i in range(self.num):
            value = data[self.src].pop(srctop)
            print(f"popped value {value}")
            print(f"src value after pop: {data[self.src]}")
            if keep_order:
                srctop -= 1
            data[self.dest].insert(desttop, value)
            print(f"dest value after insert {data[self.dest]}")
            
with open(filename, "r") as file_handle:
    raw_file = [ line.strip("\n") for line in file_handle.readlines() ]

line_width = len(raw_file[0])

# Input format puts characters at index 1, 5, 9, 13, etc
addresses = [ i for i in range(1, line_width + 1, 4) ]

in_header = True

#need to make this big enough for a full stack of letters
state = []
instructions = []

for line in raw_file:
    buf = []
    if line == "":
        in_header = False
        continue
    elif in_header and line[1] != "1":
        for address in addresses:
            char = line[address] if line[address] != " " else ""
            buf.append(char)
        state.append(buf)
    if not in_header:
        buf = line.split(" ")
        instructions.append(Instruction(buf[1], buf[3], buf[5] ) )

# transform to sideways stacks, to make this easier to manipulate
print(len(state[0]))
print(state)
newstate = [ [ state[y][x] for y in range(len(state)) ] for x in range(len(state[0])) ]
print(len(newstate))
print(newstate)
for ins in instructions:
    ins.apply(newstate, is_part2)

print(newstate)
tops = "".join([ line[first_value_address(line)] for line in newstate ])
print(tops)
