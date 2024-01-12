from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Secret key for signing and verifying JWTs
SECRET_KEY = 'your_secret_key'

# Mock data for loan applications
loan_applications = {}

# Helper function to create JWT tokens
@app.route('/')
def hello():
   return 'Hello'



if __name__ == '__main__':
    app.run(port=5000)
