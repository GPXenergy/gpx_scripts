import logging

# create logger with 'spam_application'
gpx_logger = logging.getLogger('gpx_scripts')
gpx_logger.addHandler(logging.StreamHandler())
gpx_logger.setLevel(logging.DEBUG)
