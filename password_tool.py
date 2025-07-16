import random
import string

def generate_password(length=12):
    """Generate a random password with letters, numbers, and symbols."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_password(password):
    """Check password strength and return score and feedback."""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters")
    
    # Character type checks
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")
        
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Strength rating
    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Good"
    elif score >= 2:
        strength = "Fair"
    else:
        strength = "Weak"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

# Example usage
if __name__ == "__main__":
    # Generate a password
    new_password = generate_password(12)
    print(f"Generated password: {new_password}")
    
    # Check its strength
    result = check_password(new_password)
    print(f"Strength: {result['strength']} ({result['score']}/5)")
    
    # Test with a weak password
    weak_password = "password123"
    result = check_password(weak_password)
    print(f"\nTesting '{weak_password}':")
    print(f"Strength: {result['strength']} ({result['score']}/5)")
    if result['feedback']:
        print("Suggestions:", ", ".join(result['feedback']))
