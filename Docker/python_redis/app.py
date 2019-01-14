from flask import Flask, render_template 
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="bilab_redis", port=6379, db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = None

    return render_template('index.html', neptun=os.getenv("NEPTUN"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

