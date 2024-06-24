from app import create_app, db
from app.models import User, Product
from flask_cors import CORS

app = create_app()

CORS(app, supports_credentials=True)
# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    
