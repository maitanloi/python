import hashlib
password = "maitanloi"
salt = "L0iM@i"
hash = hashlib.md5 (password + salt).hexdigest()
print (hash)