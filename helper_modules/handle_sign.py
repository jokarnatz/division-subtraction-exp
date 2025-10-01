def handle_sign(func):
    def wrapper(dividend, divisor):
        sign = 1 if dividend * divisor >= 0 else -1
        result, t1, t2 = func(abs(dividend), abs(divisor))
        return result * sign, t1, t2
    return wrapper