"""
Patient data validation module for OpenCare-Core
Implements input validation for patient registration and updates
"""

import re
from datetime import datetime
from typing import Dict, List, Tuple, Any


class PatientValidator:
    """Validator class for patient registration data"""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """
        Validate email format
        
        Args:
            email: Email address to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not email:
            return False, "Email is required"
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_pattern, email):
            return True, ""
        else:
            return False, f"Invalid email format: {email}. Expected format: name@domain.com"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """
        Validate Ugandan phone number format
        
        Args:
            phone: Phone number to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not phone:
            return False, "Phone number is required"
        
        # Ugandan format: 07XXXXXXXX or 2567XXXXXXXX
        phone_pattern = r'^((256)|0)[7-9][0-9]{8}$'
        
        if re.match(phone_pattern, phone):
            return True, ""
        else:
            return False, f"Invalid phone number: {phone}. Use format: 07XXXXXXXX or 2567XXXXXXXX"
    
    @staticmethod
    def validate_full_name(name: str) -> Tuple[bool, str]:
        """
        Validate full name (letters and spaces only)
        
        Args:
            name: Full name to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not name:
            return False, "Full name is required"
        
        if len(name) < 2:
            return False, "Name must be at least 2 characters long"
        
        if len(name) > 100:
            return False, "Name must not exceed 100 characters"
        
        name_pattern = r'^[a-zA-Z\s\'-]{2,100}$'
        
        if re.match(name_pattern, name):
            return True, ""
        else:
            return False, "Name should contain only letters, spaces, apostrophes, or hyphens"
    
    @staticmethod
    def validate_age(age: Any) -> Tuple[bool, str]:
        """
        Validate age range (0-120 years)
        
        Args:
            age: Age value to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if age is None or age == "":
            return False, "Age is required"
        
        try:
            age_int = int(age)
            if 0 <= age_int <= 120:
                return True, ""
            else:
                return False, f"Invalid age: {age_int}. Age must be between 0 and 120 years"
        except (ValueError, TypeError):
            return False, f"Invalid age value: {age}. Age must be a number"
    
    @staticmethod
    def validate_date_of_birth(dob: str) -> Tuple[bool, str]:
        """
        Validate date of birth (not in future, reasonable range)
        
        Args:
            dob: Date of birth in YYYY-MM-DD format
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not dob:
            return True, ""  # Optional field
        
        try:
            birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
            today = datetime.now().date()
            
            if birth_date > today:
                return False, "Date of birth cannot be in the future"
            
            # Calculate age
            age = today.year - birth_date.year
            if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
                age -= 1
            
            if age > 120:
                return False, f"Invalid date of birth. Patient would be {age} years old (max 120)"
            
            return True, ""
            
        except ValueError:
            return False, f"Invalid date format: {dob}. Use YYYY-MM-DD format"
    
    @staticmethod
    def validate_gender(gender: str) -> Tuple[bool, str]:
        """
        Validate gender selection
        
        Args:
            gender: Gender value
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        valid_genders = ["M", "F", "Other", "male", "female", "other", "Male", "Female"]
        
        if not gender:
            return False, "Gender is required"
        
        if gender in valid_genders:
            return True, ""
        else:
            return False, f"Invalid gender: {gender}. Valid options: M, F, Other"
    
    def validate_all(self, patient_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate all patient data fields
        
        Args:
            patient_data: Dictionary containing patient information
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        # Define validation rules
        validations = [
            ("full_name", self.validate_full_name),
            ("email", self.validate_email),
            ("phone", self.validate_phone),
            ("age", self.validate_age),
            ("date_of_birth", self.validate_date_of_birth),
            ("gender", self.validate_gender),
        ]
        
        # Run all validations
        for field_name, validator in validations:
            if field_name in patient_data:
                is_valid, error = validator(patient_data[field_name])
                if not is_valid:
                    errors.append(error)
        
        return len(errors) == 0, errors


# Example usage and test function
def test_validator():
    """Test the validator with sample data"""
    validator = PatientValidator()
    
    # Test valid data
    valid_patient = {
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "0777123456",
        "age": 30,
        "date_of_birth": "1994-01-15",
        "gender": "M"
    }
    
    is_valid, errors = validator.validate_all(valid_patient)
    print(f"Valid patient test - Is valid: {is_valid}, Errors: {errors}")
    
    # Test invalid data
    invalid_patient = {
        "full_name": "J",  # Too short
        "email": "invalid-email",  # Invalid format
        "phone": "12345",  # Invalid phone
        "age": 150,  # Too old
        "gender": "X"  # Invalid gender
    }
    
    is_valid, errors = validator.validate_all(invalid_patient)
    print(f"Invalid patient test - Is valid: {is_valid}, Errors: {errors}")
    
    for error in errors:
        print(f"  - {error}")


if __name__ == "__main__":
    test_validator()
