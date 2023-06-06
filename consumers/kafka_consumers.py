from kafka import KafkaConsumer
from pymongo import MongoClient

# MongoDB configuration
# mongo_client = MongoClient('mongodb://localhost:27017')
# db = mongo_client['your_database']
# collection = db['your_collection']

# Kafka consumer configuration
consumer = KafkaConsumer(
    'TutorialTopic',  # Kafka topic to consume from
    bootstrap_servers='localhost:9092',
    enable_auto_commit=True,
    auto_offset_reset='latest'
)

# def store_data_in_mongodb(data):
#     # Store post data in MongoDB
#     collection.insert_one(data)

def consume_messages():
    for message in consumer:
        try:
            # Parse and process the message data
            data = message.value.decode()
            # Perform any necessary data processing or validation here
            print(data)
            # Store the data in MongoDB
            # store_data_in_mongodb(data)

        except Exception as e:
            # Handle any exceptions during message processing
            print("Exception occurred:", str(e))

if __name__ == '__main__':
    consume_messages()