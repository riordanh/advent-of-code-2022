testing = False
filename = "day8-sample" if testing else "day8-data"

from math import prod

data = []
with open(filename, "r") as infile:
    data = [ [ int(c) for c in l.strip() ] for l in infile ]

def is_visible(y, x, height_map):
    """returns true if the given tile is visible from the edge (no large numbers in between"""
    max_x = len(height_map[0]) - 1
    max_y = len(height_map) - 1

    if x == 0 or x == max_x \
        or y == 0 or y == max_y:
        #print(f"edge tile {x}, {y}")
        return True

    visible = { "above": True, "below": True, "left": True, "right": True }

    #Above
    for i in range(y):
        if height_map[i][x] >= height_map[y][x]:
            visible["above"] = False
            break
    #Below
    for i in range(max_y, y, -1):
        if height_map[i][x] >= height_map[y][x]:
            visible["below"] = False
            break
    #Left
    for i in range(x):
        if height_map[y][i] >= height_map[y][x]:
            visible["left"] = False
            break
    #Right
    for i in range(max_x, x, -1):
        if height_map[y][i] >= height_map[y][x]:
            visible["right"] = False

    #if True in visible.values():
    #    print(f"{x}, {y}, {visible}")
    #    return True
    return True in visible.values()

def tile_score(y, x, height_map):
    max_x = len(height_map[0]) - 1
    max_y = len(height_map) - 1

    distances = []
    i=0

    #Above
    if y > 0:
        for i in range(y - 1, -1, -1):
            if height_map[i][x] >= height_map[y][x]:
                break
        distances.append(y - i)

    #Below
    if y < max_y:
        for i in range(y + 1, max_y + 1):
            if height_map[i][x] >= height_map[y][x]:
                break
        distances.append(i - y)

    #Left
    if x > 0:
        for i in range(x - 1, -1, -1):
            if height_map[y][i] >= height_map[y][x]:
                break
        distances.append(x-i)

    #Right
    if x < max_x:
        for i in range(x + 1, max_x + 1):
            if height_map[y][i] >= height_map[y][x]:
                break
        distances.append(i-x)
    print(distances)
    return prod(distances)


visible_num = 0

highest_score = 0
current_score = 0

for tile_y in range(len(data)):
    for tile_x in range(len(data[tile_y])):
        visible_num += is_visible(tile_y, tile_x, data)
        current_score = tile_score(tile_y, tile_x, data)
        if current_score > highest_score:
            highest_score = current_score
        print(tile_x, tile_y, current_score)

print(visible_num)
print(highest_score)