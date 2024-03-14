from confuse import Configuration
from pydantic import BaseModel


class Config(BaseModel):
    target: str = "localhost"
    port: int = 53
    file: str
    delimiter: str = ","
    thread_count: int = 10


def construct_config(config: str):
    confuse_config = Configuration("dns-papin", __name__)
    confuse_config.set_env(prefix="PAPIN_")
    confuse_config.set_file(config)
    return Config(**confuse_config.flatten())
