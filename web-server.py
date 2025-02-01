from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def timeIP():
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    ip_address = request.remote_addr
    
    return jsonify({
        "timestamp": timestamp,
        "ip": ip_address
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
