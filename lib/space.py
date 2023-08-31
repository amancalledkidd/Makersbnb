class Space:
    def __init__(self, id, name, address, price, description, user_id, image_url=''):
        self.id = id
        self.name = name
        self.address = address
        self.price = price
        self.description = description
        self.user_id = user_id
        if image_url == '':
            self.image_url = 'https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
        else:
            self.image_url = image_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Space({self.id}, {self.name}, {self.address}, {self.price}, {self.description}, {self.user_id})'
