testing = False
filename = "day6-sample" if testing else "day6-data"

with open(filename) as raw_file:
    data = raw_file.read().strip()


def check_quartet(end_index, string):
    start_index = end_index - 3
    substring = string[start_index:end_index+1]
    for i in substring:
        if substring.count(i) > 1:
            return False
    return True

def find_message(end_index, string):
    start_index = end_index - 13
    substring = string[start_index:end_index+1]
    for i in substring:
        if substring.count(i) > 1:
            return False
    return True

for i in range(3, len(data)):
    if check_quartet(i, data):
        print(f"first packet index {i+1}") # puzzle wants a 1-indexed result
        break
for i in range(13, len(data)):
    if find_message(i, data):
        print(f"first message index {i+1}")
        break

