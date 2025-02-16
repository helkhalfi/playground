import logging
from watchfiles import watch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
> uv run python src/learn_watchfiles.py
# modify the content of 'src/learn_watchfiles.py'
{(<Change.modified: 2>, '/home/helkhalfi/dev/playground/./src/learn_watchfiles.py')}
{(<Change.modified: 2>, '/home/helkhalfi/dev/playground/./src/learn_watchfiles.py')}

# Added a new files in 'src/fefe'
{(<Change.added: 1>, '/home/helkhalfi/dev/playground/./src/fefe')}

# Added a delete the file 'src/fefe'
{(<Change.deleted: 3>, '/home/helkhalfi/dev/playground/./src/fefe')}
"""

for changes in watch('.'):
    logger.info(changes)
