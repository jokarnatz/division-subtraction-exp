from sys import exit
from time import sleep

def get_input(prompt: str, datatype: type, **excluded_values):
    """
    Get user input with validation.
    
    Args:
        prompt: The input prompt to display
        datatype: The expected data type (int, float, str)
        excluded_values: Keyword argument with list of values to exclude
    
    Returns:
        The validated input converted to the specified datatype
    """
    while True:
        try:
            value = datatype(input(prompt).replace(',','.'))
            # Check for excluded values
            if excluded_values:
                excluded_list = list(excluded_values.values())[0]
                if value in excluded_list:
                    raise ValueError(f'Value must not be in {excluded_list}.')
            
            return value
            
        except (ValueError, TypeError):
            print('Invalid input. Please try again.')
        except KeyboardInterrupt:
            print('\nExiting')
            sleep(0.5)
            exit(0)
        except EOFError:
            print('\nInput stream ended. Exiting.')
            exit(0)
        except Exception as e:
            print(f'An error occurred: {e}')
            exit(1)