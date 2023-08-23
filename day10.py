testing = False
filename = "day10-sample" if testing else "day10-data"
import math
data = []
with open(filename, "r") as infile:
    data = [ line.strip().split(" ") for line in infile ]

def render_pixel(cycle, pos):
    col = (cycle-1) % 40
    if col >= pos - 1 and col <= pos + 1:
        return "#"
    else:
        return "."

cycle = 0
cmd_index = 0
ADDX1, ADDX2, NOOP = (1, 2, 3)
x_reg = 1

taps = [ 20, 60, 100, 140, 180, 220 ]
total = 0
state = None

render = [""] * 6
while cmd_index < len(data):
    cycle += 1
    cmd = data[cmd_index][0]

    if cycle in taps:
        buf = cycle*x_reg
        total += buf
        print(x_reg, total)

    row = math.ceil(cycle/40)
    render[row - 1] += render_pixel(cycle, x_reg)

    if cmd == "noop":
        state = NOOP
    if state == ADDX2:
        x_reg += int(data[cmd_index][1])
        state = None
    elif state == None:
        if cmd == "addx":
            state = ADDX1
    if state == ADDX1:
        state = ADDX2

    if state == NOOP or state == None:
        cmd_index += 1
        state = None
print(total)

for row in render:
    print("".join(row))