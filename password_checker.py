#Password Checker
import requests
#imports python built in hashing  
import hashlib
#all passwords are hashed with SHA-1
#a hash function is a function that generates a value of fixed length for each input it gets

def request_api_data(query_char):
    #only gives the first 5 characters of the hash of password123
    #this ensures they don't know our full password
    url = "https://api.pwnedpasswords.com/range/" + query_char
    #response of 200 indicates everything working
    res = requests.get(url)
    if res.status_code() != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check API and retry!")
    return res

def pwned_api_check(password):
    """Converts password to SHA-1 HASH"""
    #check if password exists in the API response
    #unicode objects must be encoded before hashing, so we use UTF-8 (standard)
    #hexdigest returns a stringle of double length, containing only hexadecimal digits
    #api SHA-1 hashes are all uppercase, so we use .upper()
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return sha1_password

print(pwned_api_check("warship78"))