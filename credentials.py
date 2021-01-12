users = {
}

userPassword = {
}


class Credential:
    id = 0

    @classmethod
    def increaseID(cls):
        cls.id = cls.id + 1

    @classmethod
    def getId(cls):
        return cls.id
