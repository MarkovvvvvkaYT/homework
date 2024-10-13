def check_division(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return "Деление на ноль невозможно"
        else:
            return func(*args, **kwargs)


    return wrapper
