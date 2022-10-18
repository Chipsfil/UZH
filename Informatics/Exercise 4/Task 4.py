#!/usr/bin/env python3


####################################
#DOESN'T GIVE MAX POINT, ONLY 2.75/3
####################################


# These are examples for valid and invalid inputs to your validation function
from curses.ascii import isalpha


IPv4_STRING = "127.0.0.1"
IPv4_INVALID_STRING = "300.0.0.291"
IPv6_STRING = "f001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_STRING_2= "0g:0g:0g:0g:0g:0g:0g:0g"
IPv6_INVALID_STRING = "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"
INVALID_IP_STRING = "Some arbitrary string"


def is_valid_IPv4_octet(octet: str):
    "Returns True if octet represents a valid IPv4 octet, False otherwise"
    if len(octet)<=3 and len(octet)>0:
        if int(octet)>=0 and int(octet)<=255:
            return True
        else:
            return False
    else:
        return False

def is_valid_IPv4(ip: str):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    valid=True
    for i in ip.split("."):
        if is_valid_IPv4_octet(i)==True:
            valid= valid*True
        else:
            valid= valid*False
    if valid==True:
        return True
    else:
        return False

def is_valid_IPv6_hextet(hextet: str):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    valid_letters=["a","A","b","B","c","C","d","D","e","E","f","F"]
    state=True
    if len(hextet)<=4 and len(hextet)>0:
        for i in hextet:
            if (i.isalpha()==True) and (i in valid_letters) or (i.isdigit()==True):
                pass
            else:
                state=False
        if state==False:
            return False
        elif int(hextet,16)>=0 and int(hextet,16)<=65535:
            return True
        else:
            return False
    else:
        return False

def is_valid_IPv6(ip: str):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    valid=True
    for i in ip.split(":"):
        if is_valid_IPv6_hextet(i)==True:
            valid = valid * True
        else:
            valid = valid * False
    if valid==True:
        return True
    else:
        return False

def is_valid_IP(ip: str):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if ":" in ip:
        if len(ip)>=15 and len(ip)<=39:
            return is_valid_IPv6(ip)
        else:
            return False
    else:
        if len(ip)>=7 and len(ip)<=15:
            return is_valid_IPv4(ip)
        else:
            return False


# The following lines call is_valid_IP and print the result.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(
    f"{IPv4_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_STRING))
print(
    f"{IPv4_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv4_INVALID_STRING),
)
print(
    f"{IPv6_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_STRING))
print(
    f"{IPv6_STRING_2} is a valid IP Address:",
    is_valid_IP(IPv6_STRING_2))
print(
    f"{IPv6_INVALID_STRING} is a valid IP Address:",
    is_valid_IP(IPv6_INVALID_STRING),
)
print(
    f"{INVALID_IP_STRING} is a valid IP Address:",
    is_valid_IP(INVALID_IP_STRING),
)
