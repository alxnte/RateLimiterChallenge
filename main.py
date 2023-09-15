from flask import Flask, jsonify, request
from RateLimiter import RateLimiter
import time

# HTTP Server to test RateLimiter class

app = Flask(__name__)

@app.route('/get_time', methods=['GET'])
def get_time():
    client_ip = request.remote_addr
    try:
        request_timestamp = int(request.args.get('timestamp'))  # Get request timestamp from query parameter
    except ValueError:
        request_timestamp  = int(time.time() * 1000) # Set timestamp to current time if timestamp is not present 
        # An empty string will raise a ValueError

    if rate_limiter.is_allowed(client_ip, request_timestamp):
        response = {
            'status': 'success',
            'message': 'Current time',
            'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(request_timestamp / 1000.0))
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 'error',
            'message': 'Rate limit exceeded'
        }
        return jsonify(response), 429

if __name__ == '__main__':
    rate_limiter = RateLimiter(interval_ms=10000, limit=5)  # Set rate limiting to 5 requests per 10 seconds
    app.run(host='0.0.0.0', port=5000)