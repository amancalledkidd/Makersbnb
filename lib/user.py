class User:
    def __init__(self, id, name, email, password, phone_number) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"User({self.id}, {self.name}, {self.email}, {self.phone_number})"
