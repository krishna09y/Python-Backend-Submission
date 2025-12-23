movies = {
    "Demon Slayer Infinite Castle": True,
    "ThunderBolt": True,
    "The Conjuring Last Rites": True
}  # True means available, False means not available

seats = {
    "B-22": {"type": "Executive", "price": 100},
    "A-12": {"type": "Premium", "price": 250},
    "C-34": {"type": "Platinum", "price": 500}
}  # Clean 'type' key

booking = []  # List to store booked tickets


def movie_show():
    print("\nAvailable movies:")
    any_available = False
    for movie, available in movies.items():
        if available:
            print(f"- {movie}")
            any_available = True

    if not any_available:
        print("Currently no movies are available now, please check later.")


def seats_show():
    print("\nAvailable seats:")
    if not seats:
        print("No seats are available.")
    else:
        for seat, details in seats.items():
            print(f"- Seat: {seat}, Type: {details['type']}, Price: {details['price']}")


def book_ticket(movie, seat):
    # Check if movie exists and is available
    if movie not in movies or not movies[movie]:
        print(f"Sorry, there are no available shows for '{movie}'.")
        return

    # Check if seat exists
    if seat not in seats:
        print(f"Sorry, seat {seat} does not exist.")
        return

    # Check if seat is already booked
    for booking_entry in booking:
        if booking_entry['seat'] == seat:
            print(f"Sorry, seat {seat} is already booked.")
            return

    # Book the ticket
    booking.append({"movie": movie, "seat": seat, "price": seats[seat]["price"]})
    print(f"\nTicket booked successfully for '{movie}' at seat {seat}. Price: {seats[seat]['price']}")

    # Collect customer details
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    print(f"\nBooking confirmed for {name}. Contact: {phone}")
    print("Enjoy your movie!")

    # Remove booked seat
    del seats[seat]

    # Mark movie as unavailable if no seats left
    if not seats:
        movies[movie] = False

    if not any(movies.values()):
        print("\nAll movies are now fully booked.")

    if not seats:
        print("All seats are booked now.")

    print("\nThank you for using our booking system.")


def main():
    while True:
        print("\n--- Movie Booking System ---")
        print("1. Show available movies")
        print("2. Show available seats")
        print("3. Book a ticket")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            movie_show()
        elif choice == '2':
            seats_show()
        elif choice == '3':
            movie = input("Enter the movie name: ")
            seat = input("Enter the seat number: ")
            book_ticket(movie, seat)
        elif choice == '4':
            print("\nExiting the booking system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


# Program Entry Point
if __name__ == "__main__":
    main()
