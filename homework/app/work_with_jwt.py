import jwt
import time
import datetime
import config

SECRET_KEY = "egfjwhsviufeguyxhuigfmvuxhmimhzmmhoqcegycrxhoxeiuyohexfomidwfbmoxfcohmixfwbonwfcmn"
WRONG_SECRET_KEY = "linganguliguliguliguachalinganguuulinganguuuuuuu"

current_time = datetime.datetime.now(datetime.timezone.utc)

payload_base = {
    "username": "Anna",
    "age": 15,
    "city": "Vienna",
}

#payload_1000 = payload_base.copy()
#payload_1000["exp"] = int(time.time()) + 1000

#token_1000 = jwt.encode(payload_1000, SECRET_KEY, algorithm="HS256")
#print("TOKEN (1000 sec):", token_1000)

#decoded_1000 = jwt.decode(token_1000, SECRET_KEY, algorithms=["HS256"])
#print("DECODED:", decoded_1000)


#payload_10 = payload_base.copy()
#payload_10["exp"] = int(time.time()) + 10

#token_10 = jwt.encode(payload_10, SECRET_KEY, algorithm="HS256")
#print("TOKEN (10 sec):", token_10)

#print("Sleeping 15 seconds...")
#time.sleep(15)

#decoded_10 = jwt.decode(token_10, SECRET_KEY, algorithms=["HS256"])
#print(decoded_10)

payload_500 = payload_base.copy()
payload_500["exp"] = int(time.time()) + 500

token_500 = jwt.encode(payload_500, SECRET_KEY, algorithm="HS256")
print("TOKEN (500 sec):", token_500)

decoded_500 = jwt.decode(token_500, WRONG_SECRET_KEY, algorithms=["HS256"])
print(decoded_500)