"""implement a Strategy Pattern for flexible input validation. For example, having different
validation strategies for password strength (e.g., "basic" vs. "strong" validation rules)."""
# business/strategies.py

from abc import ABC, abstractmethod

# Abstract Base Class for validation strategies
class PasswordValidationStrategy(ABC):
    # Abstract validate method that subclasses need to implement
    @abstractmethod
    def validate(self, password):
        """Validate the password."""
        pass

# Basic Validation Strategy
class BasicPasswordValidationStrategy(PasswordValidationStrategy):
    def validate(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")

# Strong Validation Strategy
class StrongPasswordValidationStrategy(PasswordValidationStrategy):
    def validate(self, password):
        if len(password) < 12:
            raise ValueError("Password must be at least 12 characters long")
        if not any(ch.isupper() for ch in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(ch.islower() for ch in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(ch.isdigit() for ch in password):
            raise ValueError("Password must contain at least one digit")
        if not any(ch in "!@#$%^&*()_-+=<>?/{}~" for ch in password):
            raise ValueError("Password must contain at least one special character")