from strategies.authenticated_strategy import AuthenticatedStrategy
from strategies.non_authenticated_strategy import NonAuthenticatedStrategy
from credentials import CredentialManager


def main():
    credential_manager = CredentialManager()

    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    if credential_manager.verify_credentials(input_username, input_password):
        strategy = AuthenticatedStrategy()
    else:
        strategy = NonAuthenticatedStrategy()

    strategy.execute()


if __name__ == "__main__":
    main()
