from cryptography.fernet import Fernet


def generate_key():
    """Generate and return a new encryption key."""
    return Fernet.generate_key()


def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """Decrypt an encrypted message using the provided key."""
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

