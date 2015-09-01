from caesarcipher import encode
from caesarcipher import decode

msg = encode("I Love you", 98)
print msg

msg_d = decode(msg, 98)
print msg_d 
