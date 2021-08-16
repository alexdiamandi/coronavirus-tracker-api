"""app.config.py"""
import functools
import logging

from pydantic import AnyUrl, BaseSettings

CFG_LOGGER = logging.getLogger("app.config")


class _Settings(BaseSettings):

    settingsInstance = None

    port: int = 5000
    rediscloud_url: AnyUrl = None
    local_redis_url: AnyUrl = None
    # Scout APM
    scout_name: str = None
    # Sentry
    sentry_dsn: str = None

    def __init__(self):
        if _Settings.settingsInstance:
            raise Exception("This is a singleton")
        else:
            _Settings.settingsInstance = self

@functools.lru_cache()
    def get_settings(**kwargs) -> BaseSettings:
        """
        Read settings from the environment or `.env` file.
        https://pydantic-docs.helpmanual.io/usage/settings/#dotenv-env-support

        Usage:
            import app.config

            settings = app.config._Settings.get_settings(_env_file="")
            port_number = settings.port
        """
        CFG_LOGGER.info("Loading Config settings from Environment ...")
        return _Settings(**kwargs)