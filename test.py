from decouple import config

password = config("PASSWORD", default=1234, cast=int)
print(password)