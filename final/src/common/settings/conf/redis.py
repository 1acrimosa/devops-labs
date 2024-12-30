from common.environ import env

REDIS_URL = env("REDIS_URL", cast=str, default="redis://localhost:6379/0")
