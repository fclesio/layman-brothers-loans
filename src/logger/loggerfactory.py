import logging


class LoggerFactory(object):
    _LOG = None

    @staticmethod
    def __create_logger(log_level):
        """
        A private method that interacts with the python logging module
        Parameters
        ----------
        log_level str
            The string to provide the logging level fr the logger
        Returns
        -------
        LoggerFactory._LOG logger
        """

        log_format = (
            "%(asctime)s - %(filename)s - %(funcName)s() - %(levelname)s: %(message)s"
        )

        LoggerFactory._LOG = logging.getLogger()
        logging.basicConfig(
            level=logging.INFO, format=log_format, datefmt="%Y-%m-%d %H:%M:%S"
        )

        if log_level == "INFO":
            LoggerFactory._LOG.setLevel(logging.INFO)
        elif log_level == "ERROR":
            LoggerFactory._LOG.setLevel(logging.ERROR)
        elif log_level == "DEBUG":
            LoggerFactory._LOG.setLevel(logging.DEBUG)
        return LoggerFactory._LOG

    @staticmethod
    def get_logger(log_level):
        """
        A static method called by other modules to initialize logger in
        their own module
        Parameters
        ----------
        log_level str
            The string to provide the logging level fr the logger
        Returns
        -------
        logger logger
        """
        logger = LoggerFactory.__create_logger(log_level)

        return logger
