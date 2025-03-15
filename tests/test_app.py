import pytest
from app import app, db, User, Todo
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 302  # Should redirect to login

def test_add_todo(client):
    # Create a test user
    user = User(username='testuser', password_hash='testpass')
    db.session.add(user)
    db.session.commit()
    
    # Login (simulate)
    with client.session_transaction() as session:
        session['user_id'] = user.id
    
    # Test adding a todo
    response = client.post('/add', data={'title': 'Test Todo'})
    assert response.status_code == 302  # Should redirect to index
    
    # Verify todo was added
    todo = Todo.query.first()
    assert todo is not None
    assert todo.title == 'Test Todo'
    assert todo.user_id == user.id 