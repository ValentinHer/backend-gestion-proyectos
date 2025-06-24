import bcrypt

def get_password_hash(password: str):
    salts = bcrypt.gensalt(10)
    password_hashed = bcrypt.hashpw(password.encode("utf-8"), salts)
    return password_hashed.decode("utf-8")

def valid_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(bytes(plain_password.encode("utf-8")), bytes(hashed_password.encode("utf-8")))
