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
        rows = self._connection.execute('SELECT * FROM spaces')
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
    def create(self):
        pass
    # creates a space with name desc price etc
    def delete(self):
        pass
    # deletes a space
    def update(self):
        pass
    # updates an already present space