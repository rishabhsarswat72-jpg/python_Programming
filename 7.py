import datetime

class Logger:
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):
    def log(self, msg):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"[{current_time}] {msg}")

logger = TimestampLogger()
logger.log("System initialized.")
