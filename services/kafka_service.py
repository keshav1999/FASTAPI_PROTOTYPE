from kafka import KafkaProducer
import json

def background_job(data):
    # Kafka producer to send data to a Kafka topic
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('TutorialTopic', json.dumps(data) .encode())
    producer.flush()

