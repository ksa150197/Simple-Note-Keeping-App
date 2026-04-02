from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)

print("APP STARTED")

# Database setup (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Note Model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(timezone.utc))

# Create DB
with app.app_context():
    db.create_all()

# Routes
@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    if search_query:
        notes = Note.query.filter(Note.content.contains(search_query)).order_by(Note.timestamp.desc()).all()
    else:
        notes = Note.query.order_by(Note.timestamp.desc()).all()
    return render_template('index.html', notes=notes, search_query=search_query)

@app.route('/add', methods=['POST'])
def add_note():
    content = request.form.get('content')
    if content:
        new_note = Note(content=content)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))

# Run app (ONLY here)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)