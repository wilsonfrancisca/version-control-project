import time

class BikeShareStatistics:
    def __init__(self):
        self.city = None
        self.time_period = None

    def get_city(self):
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
        self.city = city.lower()

    def get_time_period(self):
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        self.time_period = time_period.lower()

    def get_month(self):
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        return month.lower()

    def get_day(self, month):
        day = input('\nWhich day? Please type your response as an integer.\n')
        return day.lower()

    def popular_month(self, city_file):
        # TODO: implement popular_month function
        pass

    def popular_day(self, city_file):
        # TODO: implement popular_day function
        pass

    def popular_hour(self, city_file):
        # TODO: implement popular_hour function
        pass

    def trip_duration(self, city_file):
        # TODO: implement trip_duration function
        pass

    def popular_stations(self, city_file):
        # TODO: implement popular_stations function
        pass

    def popular_trip(self, city_file):
        # TODO: implement popular_trip function
        pass

    def users(self, city_file):
        # TODO: implement users function
        pass

    def gender(self, city_file):
        # TODO: implement gender function
        pass

    def birth_years(self, city_file):
        # TODO: implement birth_years function
        pass

    def display_data(self):
        # TODO: implement display_data function
        pass

    def calculate_statistics(self):
        self.get_city()
        self.get_time_period()

        print('Calculating the first statistic...')
        start_time = time.time()

        if self.time_period == 'none':
            self.popular_month(self.city)

        if self.time_period == 'none' or self.time_period == 'month':
            self.popular_day(self.city)

        self.popular_hour(self.city)
        self.trip_duration(self.city)
        self.popular_stations(self.city)
        self.popular_trip(self.city)
        self.users(self.city)
        self.gender(self.city)
        self.birth_years(self.city)

        print("That took %s seconds." % (time.time() - start_time))

        self.display_data()

        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() == 'yes':
            self.calculate_statistics()

if __name__ == "__main__":
    bike_share_stats = BikeShareStatistics()
    bike_share_stats.calculate_statistics()