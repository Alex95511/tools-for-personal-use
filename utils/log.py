import logging
import os


class Logger:
    def __init__(self, log_file="log/message.log", log_level=logging.DEBUG):
        # 创建一个logger对象
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # 创建一个handler，用于写入日志文件
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # 创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            "[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d][%(threadName)s]: %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


LOG_DIR = "log"
GLOBAL_LOGGER = None


def init(name, level=logging.DEBUG):
    global GLOBAL_LOGGER, LOG_DIR
    file_path = os.path.join(LOG_DIR, f"{name}.log")
    GLOBAL_LOGGER = Logger(file_path, level).get_logger()


def info(msg, *args, **kwargs):
    global GLOBAL_LOGGER
    if GLOBAL_LOGGER is None:
        GLOBAL_LOGGER = Logger().get_logger()
    GLOBAL_LOGGER.info(msg, stacklevel=2, *args, **kwargs)


def error(msg, *args, **kwargs):
    global GLOBAL_LOGGER
    if GLOBAL_LOGGER is None:
        GLOBAL_LOGGER = Logger().get_logger()
    GLOBAL_LOGGER.error(msg, stacklevel=2, *args, **kwargs)


def warning(msg, *args, **kwargs):
    global GLOBAL_LOGGER
    if GLOBAL_LOGGER is None:
        GLOBAL_LOGGER = Logger().get_logger()
    GLOBAL_LOGGER.warning(msg, stacklevel=2, *args, **kwargs)


def debug(msg, *args, **kwargs):
    global GLOBAL_LOGGER
    if GLOBAL_LOGGER is None:
        GLOBAL_LOGGER = Logger().get_logger()
    GLOBAL_LOGGER.debug(msg, stacklevel=2, *args, **kwargs)
