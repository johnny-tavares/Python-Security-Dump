from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    with open("logs.txt", "a") as file:
        file.write(f"{data}\n")
    return "Logged", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)