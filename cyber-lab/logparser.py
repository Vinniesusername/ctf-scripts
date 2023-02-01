import re
def do_the_thing(file): #file has to be in the same dir as the python script
    hashmap = {}
    with open(file) as f:
        for line in f:
            found = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if found is not None:
                found = found.group(0)
                if found in hashmap.keys():
                    hashmap[found] += 1
                else:
                    hashmap[found] = 1
    total = getTotal(hashmap)
    print("| percent | count | ip |")
    for key in hashmap.keys():
        percent = hashmap[key]/total
        print("|",percent, "|", hashmap[key], "|",  key, "|")

def getTotal(map):
    total = 0
    for key in map.keys():
        total += map[key]
    return total




do_the_thing("auth1.log")
