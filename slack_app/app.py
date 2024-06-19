import flask
from flask import request, Response
import os
import json

app = flask.Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    # for challenge of slack api
    if 'challenge' in data:
        token = str(data['challenge'])
        return Response(token, mimetype='text/plane')
    # for events which you added
    if 'event' in data:
        print("get event")
        event = data['event']
        if 'user' in event:
            print("user = ", event["user"])
        if "text" in event:
            print("text = ", event["text"])
    return Response("nothing", mimetype='text/plane')


port = os.getenv('VCAP_APP_PORT', '8000')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)
