class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}) - ${self.price}/night - {'Booked' if self.is_booked else 'Available'}"


class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def view_rooms(self):
        print("\nAvailable Rooms:")
        for room in self.rooms:
            print(room)

    def book_room(self, room_number, guest_name):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_booked:
                    room.is_booked = True
                    self.bookings.append((room, guest_name))
                    print(f"Room {room_number} has been booked for {guest_name}.")
                    return
                else:
                    print(f"Room {room_number} is already booked.")
                    return
        print(f"Room {room_number} does not exist.")

    def view_bookings(self):
        print("\nCurrent Bookings:")
        for room, guest_name in self.bookings:
            print(f"Room {room.room_number} booked by {guest_name}")


def main():
    hotel = Hotel()

    # Adding some rooms to the hotel
    hotel.add_room(Room(101, "Single", 100))
    hotel.add_room(Room(102, "Double", 150))
    hotel.add_room(Room(103, "Suite", 250))

    while True:
        print("\nHotel Booking System")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. View Bookings")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            hotel.view_rooms()
        elif choice == '2':
            room_number = int(input("Enter the room number you want to book: "))
            guest_name = input("Enter your name: ")
            hotel.book_room(room_number, guest_name)
        elif choice == '3':
            hotel.view_bookings()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()