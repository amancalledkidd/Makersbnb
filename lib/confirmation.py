import os
from twilio.rest import Client

def send_text_confirmation(booking, user):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token  = os.getenv('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)
        if booking.confirmed == True:
            message = client.messages.create(
                to=os.getenv('TO_PHONE_NUMBER'),
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                body=(f"\n\nHi {user.name}\n\nYour booking for {booking.space.name} is confirmed!\n\n\U0001F4C5 Check-in is from 3pm on {booking.start_date.strftime('%a %d %b %Y')}\nCheck-out is up until 11am on {booking.end_date.strftime('%a %d %b %Y')}\n\nPayment on arrival is \u00A3{booking.total_price}\n\nLook forward to seeing you. Safe travels!\n\n"))
        else:
             message = client.messages.create(
                to=os.getenv('TO_PHONE_NUMBER'),
                from_=os.getenv('TWILIO_PHONE_NUMBER'),
                body=(f"\n\nWe regret to inform you that your booking for {booking.space.name} has been declined for the dates {booking.start_date.strftime('%a %d %b %Y')} to {booking.end_date.strftime('%a %d %b %Y')}.\n\nPlease explore other available properties or reach out to our support team at makersbnb@makers. vibes assistance.")
            )
        print(message.sid)