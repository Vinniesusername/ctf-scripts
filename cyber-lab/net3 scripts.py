import hashlib

def brute_force(): #find matching hash for corned beef and __ #1
    start = "FS{cabbage-wait_that's_not_right_"
    end = "}"
    h = "f91712fa1061438bdce783de7141ae96"
    for x in range(1000):
        md5 = hashlib.md5()
        string = (start + str(x) + end).encode("utf-8")
        md5.update(string)
        if md5.hexdigest() == h:
            print(string)


def brute_force16(): #find matching hash for corn beef and ___ problem #2
    start = "FS{hash-I_had_corned_beef_and_hash_"
    end = "}"
    h = "58a0c2595ace546147d60ebbbb54c62172dce95d34c44893456e450a65892e8d9c5ac87906ce6d8fe288a1114fdecafabc527f7a30c" \
        "2c3b4b0deb90d1c0a9c8c"
    for x in range(4096):   # 000-fff
        sha = hashlib.sha512()
        string = get_string(start, str(hex(x)), end)   # make the string nice and neat
        sha.update(string)
        if sha.hexdigest() == h:
            print(string)


def get_string(start, middle, end):
    middle = middle.strip('0')
    middle = middle.strip('x')
    string = (start + middle + end).encode("utf-8")
    return string


def find_prime(): #script to find suitable d given n and e in RSA encryption. es is list of candidates
    es = "433 865 1297 1729 2161 2593 3025 3457 3889 4321 4753 5185 5617 6049 6481" \
        " 6913 7345 7777 8209 8641 9073 9505 9937 10369 10801 11233 11665 12097 12529 12961 "
    el = es.split()
    for e in el:
        if int(e) % 25 == 0:
            print(e)


brute_force()
brute_force16()
find_prime()