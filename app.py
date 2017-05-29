import logging
import pickle
import redis
import random
from flask import Flask, jsonify
app = Flask(__name__)

r = redis.StrictRedis(host='redis')

app.logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    val = r.get("stations")
    if val is not None:
        data = pickle.loads(val)
        return jsonify(data)
    return 'waiting for refresh/failed refresh', 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
