import hashlib
from config import USERNAME, PASSWORD, CREDENTIALS_FILE

class CredentialManager:
    def __init__(self):
        self.username = USERNAME
        self.password = PASSWORD

        if not self.username or not self.password:
            self.load_credentials_from_file(CREDENTIALS_FILE)

    def load_credentials_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    self.username = lines[0].strip()
                    self.password = lines[1].strip()
        except FileNotFoundError:
            print(f"Credentials file '{file_path}' not found.")

    def verify_credentials(self, input_username, input_password):
        if not self.username or not self.password:
            return False
        return (input_username == self.username and
                self.hash_password(input_password) == self.hash_password(self.password))

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
