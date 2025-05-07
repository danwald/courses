from functools import partial

def log_to(log: str, message: str) -> None:
    with open(f"{log}.log", mode="a") as fp:
        fp.write(f"{message}\n")

securityLogger = partial(log_to, "security")
infoLogger = partial(log_to, "info")
errorLogger = partial(log_to, "error")
debugLogger = partial(log_to, "debug")
accessLogger = partial(log_to, "access")
