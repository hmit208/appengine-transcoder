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

from flask import Flask
import os
import string
import random
import json
import sys

import logging
from gcloud import storage, pubsub

PROJECT_ID = 'scalable-transcoding'

TOPIC = 'projects/{}/topics/message'.format(PROJECT_ID)

app = Flask(__name__)
app.config['SECRET_KEY']='test'

app.debug = True
@app.route('/')
def nhungoc():
    print('tada')
    return 'elf'
@app.route('/transcode')
def transcode():
    # pubsub_client = pubsub.Client(PROJECT_ID)
    # topic = pubsub_client.topic("message")
    # topic.publish(b"this is a   message")
    ret = os.system('ffmpeg -i /app/videos/file_example.mov /app/videos/1080.mp4')
    # ret = os.system('ffmpeg -i /home/e56/Downloads/file_example.mov /home/e56/Downloads/1080.mp4')
    if ret:
        sys.stderr.write("FAILED")
        return "Failed"
    # blob = bucket.blob('output.webm')
    # blob.upload_from_file(open('/tmp/output.webm'))
    sys.stderr.write("SUCCESS")
    return "SUCCESS"
    # return "Done"


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
# [END app]
