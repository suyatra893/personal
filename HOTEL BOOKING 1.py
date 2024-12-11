class Room:
    def __init__(self, floor, room_number):
        self.floor = floor
        self.room_number = room_number
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Floor {self.floor}, Room {self.room_number} - {status}"


class Hotel:
    def __init__(self, floors=20, rooms_per_floor=20):
        self.rooms = self.create_rooms(floors, rooms_per_floor)
        self.bookings = []

    def create_rooms(self, floors, rooms_per_floor):
        return [[Room(floor, room_number) for room_number in range(1, rooms_per_floor + 1)] for floor in range(1, floors + 1)]

    def view_rooms(self):
        print("\nAvailable Rooms:")
        for floor in self.rooms:
            for room in floor:
                if not room.is_booked:
                    print(room)

    def book_room(self, floor, room_number, guest_name):
        if floor < 1 or floor > len(self.rooms) or room_number < 1 or room_number > len(self.rooms[0]):
            print("Invalid room number or floor.")
            return

        room = self.rooms[floor - 1][room_number - 1]
        if not room.is_booked:
            room.is_booked = True
            self.bookings.append((room, guest_name))
            print(f"Room {room_number} on Floor {floor} has been booked for {guest_name}.")
        else:
            print(f"Room {room_number} on Floor {floor} is already booked.")

    def view_bookings(self):
        print("\nCurrent Bookings:")
        for room, guest_name in self.bookings:
            print(f"Floor {room.floor}, Room {room.room_number} booked by {guest_name}")


def main():
    hotel = Hotel()

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
            floor = int(input("Enter the floor number (1-20): "))
            room_number = int(input("Enter the room number (1-20): "))
            guest_name = input("Enter your name: ")
            hotel.book_room(floor, room_number, guest_name)
        elif choice == '3':
            hotel.view_bookings()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()