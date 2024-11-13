from dotenv import load_dotenv
import os


class Environment:
    def __init__(self):
        load_dotenv('.env.development')
        self.jwt_secret = os.getenv('JWT_SECRET')


environment = Environment()