from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_numbers(lst: list):
    for item in lst:
        producer.send('fibonacci',key=f'{item}'.encode('utf-8'), value=f'{item}'.encode('utf-8'))
        producer.flush()

send_numbers([10, 100, 56])
