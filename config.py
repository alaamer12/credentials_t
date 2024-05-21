import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch credentials from environment variables
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Default file path for credentials
CREDENTIALS_FILE = 'credentials.txt'
