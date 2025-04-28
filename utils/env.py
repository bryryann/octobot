import os
from dotenv import load_dotenv

load_dotenv()

def get_env(key: str, default=None) -> str:
    env = os.getenv(key, default)
    return env if isinstance(env, str) else ""
