testing = False
filename = "day7-sample" if testing else "day7-data"

with open(filename, "r") as infile:
    raw_data = [ line.strip() for line in infile.readlines() ]

class dir:
    def __init__(self, name, parent):
        self.size = 0
        self.files_size = 0
        self.children = {}
        self.files = {}
        self.parent = parent
        self.name = name
        if parent and (name not in self.parent.children):
            self.parent.children[name] = self
            #will this work? everything's pass-by-reference, so it should
    def compute_size(self):
        self.size = sum(self.files.values())
        self.files_size = self.size
        for subdir in self.children:
            self.size += self.children[subdir].compute_size()
        return self.size
    def add_file(self, name, size):
        self.files[name] = size
        self.files_size += size
    def add_child(self, name):
        if name not in self.children:
            self.children[name] = dir(name, self)
            print(f"added child {name} to {self.name}")
        if self.name != "/":
            print(f"{self.name} - parent's children: {self.parent.children.keys()}")
            print(self.children.keys())
        return self.children[name]


#Parse
ls_mode = False
current_dir = None
root = dir("/", None)
for line in raw_data:
    if line[0] == "$":
        cmd = line[2:].split(" ")
        print(cmd)
        if cmd[0] == "cd":
            if cmd[1] == "..":
                current_dir = current_dir.parent
            else:
                if cmd[1] == "/":
                    #Adding this exception so that we can keep an independant root reference
                    current_dir = root
                elif cmd[1] in current_dir.children:
                    current_dir = current_dir.children[cmd[1]]
                #else: # dirname isn't already accounted for
                #    current_dir = current_dir.add_child(cmd[1])
        elif cmd[0] == "ls":
            pass
    else:
        line = line.split(" ")
        #parsing ls output
        if line[0] == "dir":
            current_dir.add_child(line[1])
        else:
            current_dir.add_file(line[1], int(line[0]))

root.compute_size()

#sizes of each dir below 100000

def get_matching_sizes(startdir, maxs=100000, mins=0):
    sizes = []
    if startdir.size >= mins and startdir.size <= maxs:
        sizes.append(startdir.size)
    for d in startdir.children.values():
        sizes.extend(get_matching_sizes(d, maxs, mins))
    return sizes
sz = get_matching_sizes(root)
print(sz)
print(sum(sz))

total_disk = 70000000
free_disk = total_disk - root.size
target_free = 30000000
to_delete = target_free - free_disk

sz = get_matching_sizes(root, target_free, to_delete)
sz.sort()
print(sz[0])
