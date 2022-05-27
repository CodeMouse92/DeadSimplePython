class SecretAgent:

    _codeword = ""

    def __init__(self, codename):
        self.codename = codename
        self._secrets = []

    def __del__(self):
        print(f"Agent {self.codename} has been disavowed!")

    def remember(self, secret):
        self._secrets.append(secret)

    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword

    @staticmethod
    def inquire(question):
        print("I know nothing.")

    @classmethod
    def _encrypt(cls, message, *, decrypt=False):
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return ''.join(chr(ord(m) + code) for m in message)

    # METHOD 1

    # def _getsecret(self):
    #     return self._secrets[-1] if self._secrets else None

    # def _setsecret(self, value):
    #     self._secrets.append(self._encrypt(value))

    # def _delsecret(self):
    #     self._secrets = []

    # secret = property(fget=_getsecret, fset=_setsecret, fdel=_delsecret)

    # METHOD 2

    # secret = property()

    # @secret.getter
    # def secret(self):
    #     return self._secrets[-1] if self._secrets else None

    # @secret.setter
    # def secret(self, value):
    #     self._secrets.append(self._encrypt(value))

    # @secret.deleter
    # def secret(self):
    #     self._secrets = []

    # METHOD 3

    @property
    def secret(self):
        return self._secrets[-1] if self._secrets else None

    @secret.setter
    def secret(self, value):
        self._secrets.append(self._encrypt(value))

    @secret.deleter
    def secret(self):
        self._secrets = []


mouse = SecretAgent("Mouse")
mouse.inform("Parmesano")

print(mouse.secret)    # prints "None"
mouse.secret = "12345 Main Street"
print(mouse.secret)    # prints "ϗϘϙϚϛφϳЇЏДφϹКИЋЋК"
mouse.secret = "555-1234"
print(mouse.secret)    # prints "ϛϛϛϓϗϘϙϚ"

print(mouse._secrets)  # prints two values
del mouse.secret
print(mouse._secrets)  # prints empty list
