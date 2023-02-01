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
    for key in hashmap.keys():
        print("ip ",key, "count ", hashmap[key]) #add time plus formatting
do_the_thing("auth1.log")
