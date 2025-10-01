# this is the opration file that handles 
# the division manualy as a subtraction
# method
from time import perf_counter_ns

from helper_modules.get_input import get_input

def get_numbers() ->tuple[float,float]:
    dividend:  float = get_input("Dividend: ", float)
    divisor: float =  get_input("Divisor: ", float, excluded_values=[0])
    return dividend, divisor

def  operate_division(dividend: float, divisor: float) -> tuple[float,int,int]:
    if dividend and divisor:
        t1: int = perf_counter_ns()
        quotient: float = 0.0
        temp_dividend: float = dividend
        rem_temp_dividend: float = 0.0
        # Division vor dem Komma
        while temp_dividend > 0.0:
            if temp_dividend >=  divisor:
                temp_dividend = temp_dividend - divisor
                quotient += 1
            else:
                break
        # Division nach dem Komma
        rem_temp_dividend = temp_dividend * 10
        while rem_temp_dividend > 0.0 and quotient % 1 != 0.9:
            if rem_temp_dividend >= divisor:
                rem_temp_dividend = rem_temp_dividend -  divisor
                quotient += 0.1
            elif rem_temp_dividend % divisor >= 0.5 and quotient % 1 != 0.9:
                quotient += ((rem_temp_dividend / divisor) / 10)
                break
            else:
                break
        t2: int = perf_counter_ns()
        return quotient, t1, t2
    return 0.0,0,0

def start_operation() -> None:
    dividend, divisor = get_numbers()
    quotient, t1, t2 = operate_division(dividend, divisor)
    print(f"{dividend:g} : {divisor:g} = {quotient:.6g}")
    print(f"Execution time: {(t2 - t1) / 1_000_000:.3f} ms") # Wiedergabe in Millisekunden

if __name__ == '__main__':
    start_operation()