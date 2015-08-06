#written on 6th August 2015
#decryptor for simple XOR with byte-incrementing key
#keyoffset refers to where the key is located in the file
#offsetskip refers to how many bytes to skip decryption once we reach the location holding the key

f = open("input", "rb")
out = open("output", "wb+")
keyoffset = 16
offsetskip = 16
keylength = 8
inc = 4

def increment(ba):
    return [(i+inc)%256 for i in ba]

try:
    c = f.read()
    results = bytearray()
    key = bytearray(c[keyoffset:keyoffset+keylength])
    for p in range(0,keyoffset,keylength)+range(keyoffset+offsetskip,len(c),keylength):
        key = increment(key)
        bytes = bytearray(c[p:p+keylength])
        result = bytearray([(a^b) for (a,b) in zip(bytes,key)])
        results += result
finally:
    f.close()

try:
    out.write(results)
finally:
    out.close()