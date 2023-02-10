import re
def parse_log(): #returns the most common ip in a log, and the number of times it appears
    file = "logs/log.txt"
    ipMap= {}
    with open(file) as log:
        for line in log:
            line = line.split()
            ipInfo = line[4].split(";")
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

print(parse_log())

def parse_log2(): #returns the most common client making ftp requests
    file = "logs/log.txt"
    ipMap= {}
    with open(file) as log:
        for line in log:
            line = line.split()
            ipInfo = line[4].split(";")
            if ipInfo[1] in ipMap.keys() and ipInfo[7] == "FTP":
                ipMap[ipInfo[1]] += 1
            elif ipInfo[1] not in ipMap.keys() and ipInfo[7] == "FTP":
                ipMap[ipInfo[1]] = 1
    count = 0
    ipString = ""
    for ip in ipMap.keys():
        if ipMap[ip] > count:
            count = ipMap[ip]
            ipString = ip
    return (ipString, count)

print(parse_log2())