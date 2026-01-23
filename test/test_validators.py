# Unit tests for business.validators module
import unittest
from business.validators import validate_email, validate_password

class TestValidators(unittest.TestCase):
    def test_validate_email(self):
        # Valid email
        self.assertIsNone(validate_email("valid@example.com"))  # Should pass
        # Invalid emails
        with self.assertRaises(ValueError):
            validate_email("invalid-email")
        with self.assertRaises(ValueError):
            validate_email("")

    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if any(char.isspace() for char in password):  # Check for spaces
            raise ValueError("Password must not contain spaces")






