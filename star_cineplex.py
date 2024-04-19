class Star_cinema:
    hall_list = []
    
    def entry_hall(self, hall_object):
        Star_cinema.hall_list.append(hall_object)


class Hall(Star_cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        self.entry_hall(self)
    
    def entry_show(self, id, movies_name, time):
        self.show_info = (id, movies_name, time)
        self.show_list.append(self.show_info)

        # making a 2D_grid for seats
        self.seats_2d_grid = []
        for _y in range(self.rows):
            row = []
            for _x in range(self.cols):
                # allocating 0 to each seat initially
                row.append(0)
            self.seats_2d_grid.append(row)

        self.seats[id] = self.seats_2d_grid


    @classmethod
    def book_seats(self, id, seats):
        try:
            # for error  handling
            self.valid_id = []
            self.is_already_booked = False

            for hall in Star_cinema.hall_list:
                for key_id, seat_value in hall.seats.items():
                    self.valid_id.append(key_id)

                    if id == key_id:
                        # print(key_id)
                        for pair_i in seats:
                            # print(pair_i[0], pair_i[1])
                            if seat_value[pair_i[0]][pair_i[1]] == 0 and self.is_already_booked == False:
                                seat_value[pair_i[0]][pair_i[1]] = 1

                                print('\n\tYou have successfully booked your seats. Thanks for your reservation.\n')

                                print('\nCheck out your recent booking reservation:')
                                Hall.view_available_seats(id)
                                
                            elif seat_value[pair_i[0]][pair_i[1]] == 1:
                                self.is_already_booked = True

            if id not in self.valid_id:
                print('\nPlease provide a valid cinema show ID')
            if self.is_already_booked == True:
                print('\nSeat is already booked, please try out other ones')
        except:
            print('\nPlease select valid seat range')


    @classmethod
    def view_show_lists(self):
        for hall in Star_cinema.hall_list:
            print(f"\nHall {hall.hall_no}:")
            # print(hall.show_list)
            for show in hall.show_list:
                print(show)
            print()


    @classmethod
    def view_available_seats(self, id):
        self.valid_id = []

        for hall in Star_cinema.hall_list:
            for key_id, value in hall.seats.items():
                self.valid_id.append(key_id)

                if id == key_id:
                    print(f"\nAvailable seats of Show {key_id}:")
                    for row in value:
                        print(row)
                    print()
        
        if id not in self.valid_id:
            print('\nPlease provide a valid cinema show ID')






hall_1 = Hall(2, 3, '01')
hall_1.entry_show(1, 'jawan', '3 PM')
hall_1.entry_show(2, 'pathan', '6 pm')

hall_2 = Hall(3, 4, '02')
hall_2.entry_show(3, 'tiger', '9 pm')
hall_2.entry_show(4, 'simba', '12 pm')

# for checking purpose...
# Hall.book_seats(1, [(0,0), (1,2)])
# Hall.book_seats(2, [(0,1)])
# Hall.book_seats(3, [(0,1), (0,2), (1,1), (1,2)])
# Hall.book_seats(4, [(2,3), (1,1)])

# Hall.book_seats(4, [(2,3), (1,1)])
# Hall.book_seats(5, [(1,3), (2,2)])
# Hall.book_seats(2, [(1,3), (2,2)])
# Hall.book_seats(2, [(-5,3), (2,2)])

# Hall.view_show_lists()
# Hall.view_available_seats(1)




# creating a replica system
run = True

while run:
    print("\n\tWelcome to 'Star Cineplex' Cinema Hall")
    print("\n\tWhat is your plan today? You can check out latest arrivals\n")

    print('1: View all running show_lists')
    print('2: View available seats of a particular show')
    print('3: View all running show_lists and all available seats')
    print('4: Seat booking to a particular show')
    print('5: Exit')

    option = int(input('\nSelect any of these options:\n\n\n'))


    if option == 1:
        Hall.view_show_lists()
    

    if option == 2:
        id = int(input("Please enter a 'ID number' of the show you want to checkout:\n\n"))

        Hall.view_available_seats(id)
    
    
    if option == 3:
        # printing for tasting all shows & seats
        for hall in Star_cinema.hall_list:
            print(f"\nHall {hall.hall_no}:")
            print(hall.show_list)
            print()
            for key, value in hall.seats.items():
                print(f"Seats available of Show {key}:")
                for row in value:
                    print(row)
                print()        


    if option == 4:
        id = int(input("Please enter a 'ID number' of the show you want to book:\n\n"))

        valid_id = []

        for hall in Star_cinema.hall_list:
            for key_id, seat_value in hall.seats.items():
                valid_id.append(key_id)

        if id not in valid_id:
            print('\nPlease provide a valid cinema show ID\n')

        else:
            print('Now you have to provide seat location in X & Y range pairs.\n')
            print('You can select a single seat or multiple seats too\n')

            seat_number = int(input("Enter the 'number of seat' you want to book now:\n\n"))
            seats = []

            while seat_number > 0:
                pair_X = int(input("provide 'row #' of a seat location:\n"))
                pair_Y = int(input("provide 'column #' of a seat location:\n"))
                
                single_seat = (pair_X, pair_Y)
                seats.append(single_seat)

                seat_number -= 1
            
            # for seat in seats:
            #     print(seat)
            Hall.book_seats(id, seats)
    

    if option == 5:
        run = False

# replica system ends