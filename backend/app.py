from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3305/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String(255))
    def __init__(self, name, email):
        self.user_name = name
        self.user_email = email
@app.route('/store-data', methods=['POST'])
def store_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if name is None or email is None:
        return jsonify({'message': 'Name and email are required'}), 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Data stored successfully'}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
