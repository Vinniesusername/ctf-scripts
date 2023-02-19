import re
def parse_log(): #returns the LEAST common ip in a log (src or dest), and the number of times it appears
    file = "logs/network.log"
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
    count = 2147000000 #roughly int max - big enough for this purpose
    ipString = ""
    for ip in ipMap.keys():
        if ipMap[ip] < count:
            count = ipMap[ip]
            ipString = ip
        elif count == 1 and ipMap[ip] == count:
            print("dupe", ip)
    return (ipString, count)

def parse_log_dns(): #checks how many lines in the log connect to a given ip address (google dns server)
    file = "logs/network.log"
    count = 0
    with open(file) as log:
        for line in log:
            ips = re.findall(r"8.8.8.8", line)
            if ips:
                count+=1
    return count





print(parse_log_dns())