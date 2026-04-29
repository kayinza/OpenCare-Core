"""
Patient registration module with integrated validation
"""

from validators import PatientValidator
from typing import Dict, Any, Tuple, List


class PatientRegistration:
    """Handles patient registration with validation"""
    
    def __init__(self):
        self.validator = PatientValidator()
        self.registered_patients = []
    
    def register_patient(self, patient_data: Dict[str, Any]) -> Tuple[bool, str, Dict]:
        """
        Register a new patient with validation
        
        Args:
            patient_data: Patient information dictionary
            
        Returns:
            Tuple of (success, message, patient_record)
        """
        # Validate input data
        is_valid, errors = self.validator.validate_all(patient_data)
        
        if not is_valid:
            error_message = "; ".join(errors)
            return False, f"Validation failed: {error_message}", {}
        
        # Check for duplicate email
        if self.email_exists(patient_data.get("email")):
            return False, "Patient with this email already exists", {}
        
        # Check for duplicate phone
        if self.phone_exists(patient_data.get("phone")):
            return False, "Patient with this phone number already exists", {}
        
        # Create patient record
        patient_record = {
            "patient_id": len(self.registered_patients) + 1,
            "full_name": patient_data.get("full_name"),
            "email": patient_data.get("email"),
            "phone": patient_data.get("phone"),
            "age": patient_data.get("age"),
            "date_of_birth": patient_data.get("date_of_birth"),
            "gender": patient_data.get("gender"),
            "registration_date": "2026-04-29",
            "status": "active"
        }
        
        self.registered_patients.append(patient_record)
        return True, f"Patient registered successfully with ID: {patient_record['patient_id']}", patient_record
    
    def email_exists(self, email: str) -> bool:
        """Check if email already exists"""
        if not email:
            return False
        return any(p.get("email") == email for p in self.registered_patients)
    
    def phone_exists(self, phone: str) -> bool:
        """Check if phone already exists"""
        if not phone:
            return False
        return any(p.get("phone") == phone for p in self.registered_patients)
    
    def get_all_patients(self) -> List[Dict]:
        """Return all registered patients"""
        return self.registered_patients
    
    def get_patient_by_id(self, patient_id: int) -> Dict:
        """Get patient by ID"""
        for patient in self.registered_patients:
            if patient["patient_id"] == patient_id:
                return patient
        return {}


# Test the registration system
def test_registration_system():
    """Test the complete registration system"""
    system = PatientRegistration()
    
    # Test case 1: Valid registration
    print("=== Test Case 1: Valid Patient Registration ===")
    valid_patient = {
        "full_name": "Sarah Mukisa",
        "email": "sarah.mukisa@email.com",
        "phone": "0788123456",
        "age": 28,
        "date_of_birth": "1998-03-15",
        "gender": "F"
    }
    
    success, message, record = system.register_patient(valid_patient)
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"Record: {record}")
    
    # Test case 2: Invalid registration
    print("\n=== Test Case 2: Invalid Patient Registration ===")
    invalid_patient = {
        "full_name": "X",  # Too short
        "email": "bad-email",  # Invalid format
        "phone": "123",  # Invalid phone
        "age": 200,  # Too old
        "gender": "Invalid"
    }
    
    success, message, record = system.register_patient(invalid_patient)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Test case 3: Duplicate email
    print("\n=== Test Case 3: Duplicate Email ===")
    duplicate_patient = {
        "full_name": "Another Sarah",
        "email": "sarah.mukisa@email.com",  # Same email as before
        "phone": "0777999888",
        "age": 30,
        "gender": "F"
    }
    
    success, message, record = system.register_patient(duplicate_patient)
    print(f"Success: {success}")
    print(f"Message: {message}")
    
    # Show all registered patients
    print("\n=== All Registered Patients ===")
    for patient in system.get_all_patients():
        print(f"ID: {patient['patient_id']} | Name: {patient['full_name']} | Email: {patient['email']}")


if __name__ == "__main__":
    test_registration_system()
