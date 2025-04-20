def get_string(prompt: str) -> str:
    while True:
        try:
            return prompt.strip(' ').lower()
        except Exception as err:
            return f'{err}'

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(prompt.strip(' '))
        except Exception:
            raise Exception('Invalid number. Please try again.')
