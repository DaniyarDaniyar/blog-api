from decouple import config
# --------------------------------------------
# Env
# --------------------------------------------
ENV_POSSIBLE_OPTIONS = [
    "prod",
    "local",
]

ENV_ID = config(
    "PROJECT_ENV_ID",
    cast=str,
)
SECRET_KEY = 'MY_SUPER_SECRET_KEY'
