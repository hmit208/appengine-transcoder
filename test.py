import time

from google.cloud import pubsub_v1


project_id = 'scalable-transcoding'
topic_name = 'message'
subscription_name = 'mysub'
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())

for n in range(1, 10):
    data = u'Message number 1 {}'.format(n)
    # Data must be a bytestring
    data = data.encode('utf-8')
    # When you publish a message, the client returns a Future.
    message_future = publisher.publish(topic_path, data=data, id='{}'.format(n), url="hachium.com", email="thanh28@gmail.com")
    message_future.add_done_callback(callback)

print('Published message IDs:')

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

# def callback(message):
#     print('Received message: {}'.format(message))
#     message.ack()
#
# subscriber.subscribe(subscription_path, callback=callback)

# We must keep the main thread from exiting to allow it to process
# messages in the background.
