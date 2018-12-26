# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, request, redirect, url_for, render_template
import os
import time
import string
import random
import json

import logging
from gcloud import storage, pubsub
from google.cloud import pubsub_v1
from pprint import pprint

PROJECT_ID = 'scalable-transcoding'

TOPIC = 'projects/{}/topics/message'.format(PROJECT_ID)

app = Flask(__name__)
app.config['SECRET_KEY']='test'
x = ''
app.debug = True
@app.route('/')
def index():
    return "tada"

@app.route('/transcode', methods = ['POST', 'GET'])
def transcode():
    pubsub_client = pubsub.Client(PROJECT_ID)
    topic = pubsub_client.topic("message")
    # topic.publish(b"this is a   hmt messageasdhajkshdui", foo="201812241613")
    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_name = 'mysub'
    subscription_path = subscriber.subscription_path(
        PROJECT_ID, subscription_name)
    list = []

    def callback(message):
        print('Received message: {}'.format(message.data))
        if message.attributes:
            print("Attributes")
            for key in message.attributes:
                value = message.attributes.get(key)
                print("{}: {}".format(key, value))
        # envelop = json.loads(message)
        pprint: message
        list.append(message)
        message.ack()

    message = subscriber.subscribe(subscription_path, callback=callback)


    # messages = sub.pull(
    #     return_immediately=False, max_messages=110)
    # if messages:
    #     pprint(messages)
    # topic_name = "projects/scalable-transcoding/topics/message"
    # publisher = pubsub.Client(PROJECT_ID)
    # topic_path = publisher.topic(topic_name)
    n=0
    while(n<10):
        time.sleep(10)
        n+=1

    return 'hihi'


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]
