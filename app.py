from flask import Flask, request, jsonify

app = Flask(__name__)

devices = {}

@app.route('/update', methods=['POST'])
def update_device():
    data = request.json
    device_id = data.get("id")
    value = data.get("value")
    devices[device_id] = value
    return jsonify({"status": "ok"})

@app.route('/')
def dashboard():
    html = "<h2>ESP32 Dashboard</h2>"
    for device, val in devices.items():
        html += f"<p><b>{device}</b>: {val}</p>"
    return html

if __name__ == '__main__':
    app.run()
