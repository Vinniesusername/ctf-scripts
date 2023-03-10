# a script to solve level 11 of bandit by overthewire.org
def rot13(password):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # make dict to store the chars and their index values
    adict = {}
    for char in range(len(alpha) - 1):
        adict[alpha[char]] = char

    new_alpha = alpha[13:26:] + alpha[0:13:] + alpha[39::] + alpha[26:39:] #rot 13

    #make new dict
    ndict = {} #stores the translated chars
    for char in range(len(alpha) - 1):
        ndict[char] = new_alpha[char]
    ndict[100] = " "
    adict[" "] = 100
    final = ""
    for char in password:
        if char.isalpha():
            value = adict[char]
            final += ndict[value]
        else:
            final += char
    return final


print(rot13("Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi"))