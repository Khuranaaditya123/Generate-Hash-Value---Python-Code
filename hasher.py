#!/usr/bin/python
import hashlib
hashvalue = input("[*] Enter a string : ")
hashvalueobj1 = hashlib.md5()
hashvalueobj1.update(hashvalue.encode())
print(hashvalueobj1.hexdigest())

hashvalueobj2 = hashlib.sha1()
hashvalueobj2.update(hashvalue.encode())
print(hashvalueobj2.hexdigest())

hashvalueobj3 = hashlib.sha224()
hashvalueobj3.update(hashvalue.encode())
print(hashvalueobj3.hexdigest())

hashvalueobj4 = hashlib.sha256()
hashvalueobj4.update(hashvalue.encode())
print(hashvalueobj4.hexdigest())

hashvalueobj5 = hashlib.sha512()
hashvalueobj5.update(hashvalue.encode())
print(hashvalueobj5.hexdigest())
