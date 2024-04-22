import configparser

config = configparser.RawConfigParser()

config.read("./configuration/config.ini")

url = config.get('COMMON INFO','url')
print(url)
user = config.get('COMMON INFO','user')
print(user)
passwd = config.get('COMMON INFO','password')
print(passwd)