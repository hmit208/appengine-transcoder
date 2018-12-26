from google.cloud import pubsub_v1
import time
import pprint
import json

subscriber = pubsub_v1.SubscriberClient()
project_id = 'scalable-transcoding'
topic_name = 'message'
subscription_name = 'mysub'
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)
list = []


def callback(message):
    print('Received message: {}'.format(message.data))
    if message.attributes:
        print("Attributes")
        for key in message.attributes:
            value = message.attributes.get(key)
            print("{}: {}".format(key,value))
    # envelop = json.loads(message)
    pprint: message
    list.append(message)
    message.ack()

# time.sleep(10)
message = subscriber.subscribe(subscription_path, callback=callback)
print("Listening from {}".format(subscription_path))
while True:
    time.sleep(20)
