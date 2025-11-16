from flask import Flask, jsonify
import os

app = Flask(__name__)

# Root Route 
@app.route('/')
def home():
    return jsonify(message="Hello from Dockerized Flask App!")


# Health Check Route
@app.route('/health')
def health_check():
    return jsonify(status="ok"), 200

# Environment Variable Usage 
@app.route('/env')
def show_env():
    message = os.getenv("WELCOME_MSG", "Default Welcome Message")
    return f"message: {message}"

# Volume write test
@app.route('/log')
def write_log():
    with open("/data/log.txt", "a") as f:
        f.write("Log entry created!\n")
    return "Logged to /data/log.txt"

# Main entry point
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
