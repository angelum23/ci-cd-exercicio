from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/soma', methods=['POST'])
def soma_route():
    data = request.get_json()
    return jsonify({'resultado': data['a'] + data['b']})


@app.route('/multiplica', methods=['POST'])
def multiplica_route():
    data = request.get_json()
    return jsonify({'resultado': data['a'] * data['b']})


if __name__ == '__main__':
    app.run(debug=True)
