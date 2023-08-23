testdata = False
filename = "day4-data" if testdata else "day4-sample"

filename = "day4-data"

with open(filename, "r") as raw_file:
    data = [ line.split(",") for line in raw_file ]
#[ ["1-2", "3-4"], ["5-6", "4-7"] ]

data = [ [ [int(i.strip()) for i in k.split("-")] for k in j ] for j in data ]
#[ [ (1, 2), (3, 4) ], [(5, 6), (4, 7) ] ]
#Should have just made these objects or something instead of nesting so much

sets = []

for group in data:
    buf = []
    for item in group:
        buf.append( { j for j in range(item[0], item[1]+1) } )
    sets.append(buf)

print(sets)

count = 0
for group in sets:
    #It's increasingly looking like this should have been arithmetic instead of itemization
    encapsulated = True
    for i in group[0]:
        if i not in group[1]:
            encapsulated = False
            break
    if encapsulated:
        count += 1
        continue
    encapsulated = True
    for i in group[1]:
        if i not in group[0]:
            encapsulated = False
            break
    if encapsulated:
        count += 1

print(count)
