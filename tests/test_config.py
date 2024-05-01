class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test_secret_key'
    SERVER_NAME = 'localhost.localdomain'  # Add this line