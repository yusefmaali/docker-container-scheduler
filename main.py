import json
import logging
import os
import sys

import container_scheduler
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)-8s [%(name)s] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("docker_container_scheduler")
schedules: list = list()
"""
CONTAINER_SCHEDULES environment variable structure
[
    {
        "container": "container_name_1",
        "crontab": "*/1 * * * *"
    }
]
"""


def load_environment() -> bool:
    global schedules
    logger.info("Loading schedules from environment")

    env_schedules = os.environ.get('CONTAINER_SCHEDULES')
    if env_schedules is None:
        logger.error("No schedules found in the environment")
        return False

    try:
        schedules = json.loads(env_schedules)
    except Exception as e:
        logger.error("The scheduler configuration is not a valid json format", e)
        return False

    if type(schedules) is not list:
        logger.error("The scheduler configuration is not valid")
        return False

    if len(schedules) == 0:
        logger.error("The scheduler configuration doesn't contain any schedule")
        return False

    return True


if __name__ == '__main__':
    load_dotenv()

    if not load_environment():
        exit(1)

    if not container_scheduler.start(schedules):
        exit(1)
