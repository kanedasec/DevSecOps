from app import create_app, db
import os

app = create_app()

with app.app_context():
    db.create_all()

host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")

if __name__ == '__main__':
    app.run(host=host, port=5000)
