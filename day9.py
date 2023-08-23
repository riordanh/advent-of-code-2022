testing = False
filename = "day9-sample" if testing else "day9-data"

part2 = True
Dirs = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1) }

data = []
with open(filename, "r") as infile:
    data = [ line.strip().split(" ") for line in infile ]

data = [ (a.upper(), int(b)) for a, b in data]


class Point:
    def __init__(self, x, y, chain_length, parent = None):
        self.x = x
        self.y = y
        self.pos_log = {x, y}
        self.parent = parent
        if self.parent:
            self.parent.child = self
        if chain_length > 1:
            self.child = Point(x, y, chain_length - 1, self)
        else:
            self.child = None
    def find_tail(self):
        cur_point = self
        while cur_point.child:
            cur_point = cur_point.child
        return cur_point
    def _change_pos(self, direction):
        for c in direction: #Allow compound movements
            self.x += Dirs[c][0]
            self.y += Dirs[c][1]
        self.pos_log.add( (self.x, self.y) )
    def move(self, direction):
        self._change_pos(direction)
        if self.child:
            child_move = ""
            if (self.x - self.child.x) > 1:
                child_move = "R"
                if self.y > self.child.y:
                    child_move += "D"
                elif self.y < self.child.y:
                    child_move += "U"
            elif (self.x - self.child.x) < -1:
                child_move = "L"
                if self.y > self.child.y:
                    child_move += "D"
                elif self.y < self.child.y:
                    child_move += "U"
            if (self.y - self.child.y) > 1:
                child_move = "D"
                if self.x > self.child.x:
                    child_move += "R"
                elif self.x < self.child.x:
                    child_move += "L"
            elif (self.y - self.child.y) < -1:
                child_move = "U"
                if self.x > self.child.x:
                    child_move += "R"
                elif self.x < self.child.x:
                    child_move += "L"
            if child_move:
                self.child.move(child_move)

length = 10 if part2 else 2
snake_head = Point(1, 1, length)
snake_tail = snake_head.find_tail()

for command in data:
    for i in range(command[1]):
        snake_head.move(command[0])
print(len(snake_tail.pos_log))


