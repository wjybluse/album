__author__ = 'Elian'

import os
import json
from flask import Flask, Request, render_template, send_from_directory
from gevent.pywsgi import WSGIServer

# need mock all?

app = Flask('Trace')
app.secret_key = 'wan#*&*^*&!^&!@^#&@!#@&!^#@^!*&#'
image_path = os.path.join(app.root_path, 'db', 'files')
db_file = os.path.join(app.root_path, 'db', 'data.db')


@app.route('/', methods=['GET'])
def index():
    return render_template('_hello_.html')


@app.route('/list/img/<story>', methods=['GET'])
def list_images(story=None):
    """
    query information for database
    :param story:story name
    :return:
    """
    images = []
    if not os.path.isdir(os.path.join(image_path, story)):
        os.mkdir(os.path.isdir(os.path.join(image_path, story)))
        return render_template('_images_.html', images=[])
    for image in os.listdir(os.path.join(image_path, story)):
        if not os.path.isfile(os.path.join(os.path.join(image_path, story), image)):
            continue
        img = ImageInfo(name=image, dec=image, story=story)
        images.append(img)
    print('handle img ={0}'.format(images))
    return render_template('_images_.html', images=images)


@app.route('/trace/story/<story>', methods=['GET'])
def show_trace():
    pass


@app.route('/show/<story>/<image>', methods=['GET'])
def show_image(story=None, image=None):
    print('story ={0},name = {1}'.format(story, image))
    return send_from_directory(os.path.join(image_path, story), image)


@app.route('/add/story', methods=['POST'])
def add_story(name=None):
    pass


@app.route('/delete/story/<story>', methods=['DELETE'])
def del_story(name=None):
    pass


@app.route('/add/pic/<story>', methods=['POST'])
def add_pic(story=None):
    pass


class ImageInfo(object):
    __slots__ = ('name', 'timestamp', 'latitude', 'longitude', 'desc', 'story')

    def __init__(self, name=None, timestamp=None, latitude=0, longitude=0, **kwargs):
        self.name = name
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude
        self.desc = kwargs.get('dec')
        self.story = kwargs.get('story')


if __name__ == '__main__':
    server = WSGIServer(('', 5000), app)
    server.serve_forever()
