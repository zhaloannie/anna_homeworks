import json
import time
import ssl
import pika
import config
import certifi

ssl_context = ssl.create_default_context(
    cafile=certifi.where(),
)

connection_params = pika.ConnectionParameters(
    host=config.RMQ_HOST,
    port=config.RMQ_PORT,
    virtual_host=config.RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(
        username=config.RMQ_USER,
        password=config.RMQ_PASSWORD
    ),
    ssl_options=pika.SSLOptions(context=ssl_context),
)

def get_connection():
    return pika.BlockingConnection(parameters=connection_params)


def process_log(ch, method, properties, body):
    try:
        data = json.loads(body)
        print(f"New log: {data.get('event')}, user_id: {data.get('user_id')}")
    except json.JSONDecodeError:
        print(f"New log: {body.decode()}")

    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    print("Starting logs consumer...")
    QUEUE = "logs"

    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_log,
        auto_ack=False
    )

    channel.start_consuming()

def main():
    with get_connection() as connection:
        channel = connection.channel()
        consume_logs(channel)


if __name__ == "__main__":
    main()
