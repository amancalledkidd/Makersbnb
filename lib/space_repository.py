from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row['id'],
             row['name'],
              row['address'],
               row['price'],
                row['description'],
                row['user_id'])
    # finds a space
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces ORDER BY id')
        spaces = []
        for row in rows:
            item = Space(row['id'],
             row['name'],
              row['address'],
               row['price'],
                row['description'],
                row['user_id'])
            spaces.append(item)
        return spaces
    # returns all spaces
    def delete(self, id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [id])
        return None
    # deletes a space
    def create(self, space):
        self._connection.execute('INSERT INTO spaces (name,address,price,description,user_id) VALUES(%s,%s,%s,%s,%s) ',[space.name,space.address,space.price,space.description,space.user_id])
        return None
    # creates a space with name desc price etc
    def update(self,space):
        self._connection.execute("UPDATE spaces SET name = %s, address = %s, price = %s, description = %s, user_id = %s  WHERE id = %s",
                                [space.name, space.address, space.price, space.description, space.user_id, space.id])
        return None
    # updates an already present space

  