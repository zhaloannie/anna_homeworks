import os
from dotenv import load_dotenv
load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USERNAME = os.getenv("REDIS_USERNAME")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

JWT_SECRET = os.getenv("JWT_SECRET")

#Rabbit
RMQ_PORT = os.getenv("RMQ_PORT")
RMQ_USER = os.getenv("RMQ_USER")
RMQ_VIRTUAL_HOST = os.getenv("RMQ_VIRTUAL_HOST")
RMQ_HOST = os.getenv("RMQ_HOST")
RMQ_PASSWORD = os.getenv("RMQ_PASSWORD")
# RMQ_PORT=5671
# RMQ_USER=lehygact
# RMQ_VIRTUAL_HOST=lehygact
# RMQ_HOST=seal-01.lmq.cloudamqp.com
# RMQ_PASSWORD=vMXQtY7HfrQ_cnCQmFapCkV3W8Hh_J21