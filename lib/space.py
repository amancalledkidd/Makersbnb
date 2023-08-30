class Space:
    def __init__(self, id,name,address, price, description, user_id):
        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.description = description
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Space({self.id}, {self.name}, {self.address}, {self.price}, {self.description}, {self.user_id})'