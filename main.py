from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'T 1',
        'Contact': '1234567890',
        'done': False
    },
]

@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please Provide The Data!!!"
        },400)

    task = {
        'id': contacts[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json['Contact'],
        'done': False
    }

    contacts.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully"
    })


@app.route("/get-contacts")
def get_contacts():
    return jsonify({
        "data": contacts,
    })


if(__name__ == '__main__'):
    app.run(debug=True)
