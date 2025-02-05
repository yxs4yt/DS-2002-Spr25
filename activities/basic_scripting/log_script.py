#!/usr/bin/env python3

import logging

logging.basicConfig(filename='my_script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Script started.')

# ... your script logic ...

logging.info('Data processing complete.')