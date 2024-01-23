import pika
from db.models import Subscriber


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='mailing')
    channel.queue_declare(queue='mailing')
    channel.queue_bind(exchange='mailing', queue='mailing')

    n = 1
    for person in Subscriber.objects:
    
        body = f'Hello, {person.fullname}! Your id is {person.id}'
        channel.basic_publish(exchange='', routing_key='mailing', body=body.encode())
        print(f" [{n}.] Email sent with body {body}'")
        n += 1
        person.update(got_mail= True)
    connection.close()
    

if __name__ == '__main__':
    main()