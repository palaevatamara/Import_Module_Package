import datetime


def logger(old_function):
    path = 'logger.log'

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        func_name = old_function.__name__
        args_str = ', '.join(
            [repr(a) for a in args] +
            [f'{k}={repr(v)}' for k, v in kwargs.items()]
        )
        log_line = f'{timestamp} {func_name}({args_str}) => {result}\n'
        with open(path, 'a') as f:
            f.write(log_line)
        return result

    return new_function

def logger_param(path):
    def __logger(old_function):
        def new_function(*args, _path=path, **kwargs):
            result = old_function(*args, **kwargs)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            func_name = old_function.__name__
            args_str = ', '.join(
                [repr(a) for a in args] +
                [f'{k}={repr(v)}' for k, v in kwargs.items()]
            )
            log_line = f'{timestamp} {func_name}({args_str}) => {result}\n'
            with open(_path, 'a') as f:
                f.write(log_line)
            return result

        return new_function

    return __logger