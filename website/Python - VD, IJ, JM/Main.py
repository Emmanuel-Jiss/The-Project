Booking = []
def submit_booking(email, pitch, start, end, amenities):
    Booking.append(email)
    Booking.append(pitch)
    Booking.append(start)
    Booking.append(end)
    Booking.append(amenities)



Account = []
def submit_account(username, email, password1,password2):
    Account.append(username)
    Account.append(email)
    if password1 == password2:
        Account.append(password1)


