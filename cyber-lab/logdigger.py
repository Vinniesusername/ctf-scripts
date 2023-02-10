import re
def dothething(): #returns the most common ip in a log, and the number of times it appears
    file = "logs/log.txt"
    ipMap= {}
    with open(file) as log:
        for line in log:
            line = line.split()
            ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line[4])
            for ip in ips:
                if ip in ipMap.keys():
                    ipMap[ip] += 1
                else:
                    ipMap[ip] = 1
    count = 0
    ipString = ""
    for ip in ipMap.keys():
        if ipMap[ip] > count:
            count = ipMap[ip]
            ipString = ip
    return (ipString, count)

print(dothething())
