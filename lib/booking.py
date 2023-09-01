from datetime import date

class Booking:
    def __init__(self, id: int, start_date: date, end_date: date, total_price: float, user_id: int, space_id: int, confirmed=False, space=None) -> None:
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price
        self.user_id = user_id
        self.space_id = space_id
        self.space_name = ''
        self.space_address = ''
        self.confirmed = confirmed
        self.space = space

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Booking({self.id}, {self.start_date} to {self.end_date}, £{self.total_price:,.2f}, {self.user_id}, {self.space_id})"
