class SillyWalkException(RuntimeError):
    def __init__(self, message="Someone walked silly."):
        super().__init__(message)


def walking():
    raise SillyWalkException("My walk has gotten rather silly.")


try:
    walking()
except SillyWalkException as e:
    print(e)
