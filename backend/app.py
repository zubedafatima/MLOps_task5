from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file path
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

    with app.app_context():
        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            print("stored")
            all_users = User.query.all()

            # Print user data
            for user in all_users:
                print(f"User ID: {user.user_id}, Name: {user.user_name}, Email: {user.user_email}")
            return jsonify({'message': 'Data stored successfully'}), 200
        except Exception as e:
            return jsonify({'message': str(e)})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
