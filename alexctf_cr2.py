cipher = '0529242a631234122d2b36697f13272c207f2021283a6b0c79082f28202a302029142c653f3c7f2a2636273e3f2d653e25217908322921780c3a235b3c2c3f207f372e21733a3a2b37263b3130122f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d283f652c2b31661426292b653a292c372a2f20212a316b283c0929232178373c270f682c216532263b2d3632353c2c3c2a293504613c37373531285b3c2a72273a67212a277f373a243c20203d5d243a202a633d205b3c2d3765342236653a2c7423202f3f652a182239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c263e203d63232f0f20653f207f332065262c31683137223679182f2f372133202f142665212637222220733e383f2426386b'

""" originally i used the cipher as a list of hex strings
cipher_list = [ 0529242a631234122d2b36697f13272c207f2021283a6b0c7908,
                2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908,
                322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012,
                2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d,
                283f652c2b31661426292b653a292c372a2f20212a316b283c09,
                29232178373c270f682c216532263b2d3632353c2c3c2a293504,
                613c37373531285b3c2a72273a67212a277f373a243c20203d5d,
                243a202a633d205b3c2d3765342236653a2c7423202f3f652a18,
                2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c,
                263e203d63232f0f20653f207f332065262c3168313722367918,
                2f2f372133202f142665212637222220733e383f2426386b]
"""

# alexctf{ start ascii
alexctf = [65,76,69,88,67,84,70,123,72,69,82,69,95,71,79,69,83,95,84,72,69,95,75,69,89,125]
# had to execute it many times and modify the key to match the message in ASCII on each row

cipher_bytes = bytearray.fromhex(cipher)
message = []
for i in range(len(cipher_bytes)):
    message.append(cipher_bytes[i]^alexctf[i%26])

# print message in decimal
print("\n Message in decimal:")
for i in range(len(message)):
    if(i%26==0):
        print("\nLine",int(i/26)) # print each original line seperately (each 26 bytes)
    print(message[i],end=" ")

# print message in ASCII
print("\n\n Message in ASCII:")
for i in range(len(message)):
    if(i%26==0): # print each original line seperately (each 26 bytes)
        print()
    print(chr(message[i]),end="")
    

# print key/flag in ascii
print("\n\n Flag:")
for a in alexctf:
    print(chr(a),end="")