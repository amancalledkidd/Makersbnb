class Booking:
    def __init__(self, id, start_date, end_date, total_price, user_id, space_id) -> None:
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price
        self.user_id = user_id
        self.space_id = space_id

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Booking({self.id}, {self.start_date} to {self.end_date}, £{self.total_price:,.2f}, {self.user_id}, {self.space_id})"
