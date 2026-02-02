import config
import ssl
import pika
import json
import certifi

ssl_context = ssl.create_default_context(
    cafile=certifi.where(),
)

connection_params=pika.ConnectionParameters(
    host=config.RMQ_HOST,
    port=config.RMQ_PORT,
    virtual_host=config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=config.RMQ_USER, password=config.RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context),
)

def get_connection():
    return pika.BlockingConnection(parameters=connection_params)


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            print(channel)

def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = "logs"
    channel.queue_declare(queue=QUEUE)

    for item in range(100):
        message = {
            "event": "user_registered",
            "user_id": item
        }

        body = json.dumps(message)

        channel.basic_publish(
            exchange="",
            routing_key=QUEUE,
            body=body
        )

        print(body)

if __name__ == "__main__":
    main()
