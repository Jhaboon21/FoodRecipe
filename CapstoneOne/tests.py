import os
from unittest import TestCase
from app import app
from models import db, connect_db, User
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///food_recipe_test'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///food_recipe_test')
app.config['SQLALCHEMY_ECHO'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['TESTING'] = True

with app.app_context():
    db.session.commit()
    db.drop_all()
    db.create_all()

class UserTests(TestCase):
    """Test user functions."""

    def setUp(self):
        """Clean up existing Users."""
        with app.app_context():
            User.query.delete()

    def tearDown(self):
        """Clean up any bad inserts."""
        with app.app_context():
            db.session.rollback()

    def test_signup_form(self):
        """Display signup form."""
        with app.test_client() as client:
            res = client.get("/signup")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2 class="join-message">Sign Up Today.</h2>', html)

    def test_create_user(self):
        """Sign up user."""
        with app.test_client() as client: 
            user = {"username": "TestUser", "password": "123456", "email": "testemail@yahoo.com", "first_name": "test", "last_name": "user"}
            res = client.post("/signup", data=user, follow_redirects=True)
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            #self.assertIn("Welcome TestUser!", html)


    def test_home(self):
        """Display Homepage"""
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Welcome To Food Recipe Search!</h1>', html)