import logging

# from common.environ import env

# ---------------------------------------------
# LOGGER settings
# ---------------------------------------------
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[PID: %(process)d] - %(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logging.basicConfig(level=logging.INFO, handlers=[handler])
