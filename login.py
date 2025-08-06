def authenticate_user(username: str, password: str, user_db: dict) -> bool:
    """
    Authenticates a user against a provided user database.

    Args:
        username (str): The username to authenticate.
        password (str): The password to authenticate.
        user_db (dict): A dictionary mapping usernames to passwords.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    if username in user_db and user_db[username] == password:
        return True
    return False