import re, sys, getopt
def dig_logs(logs):
    ips = {}
    for log in logs:
        with open(log) as file:
            for line in file:
                found = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                if found is not None:
                    found = found.group(0)
                    if found in ips.keys():
                        ips[found] += 1
                    else:
                        ips[found] = 1
    most = findMost()
    return most

def findMost(hashmap):
    biggest = - 1
    ip = None
    for x in hashmap.keys():
        if hashmap[x] > biggest:
            biggest = hashmap[x]
            ip = x
    return ip

def printMost(ip, logs):
    for log in logs:
        for line in log:
            found = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if found == ip:
                print(line)

