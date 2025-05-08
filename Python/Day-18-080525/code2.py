#logging

import logging

#configure basic logging

logger = logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s - %(process)d -  %(levelname)s - %(message)s'
)

# log messages

logging.debug('Debug message')
logging.info('Processing started')
logging.warning('Resource running low')
logging.error('Error occures')
logging.critical('Critical failure')
