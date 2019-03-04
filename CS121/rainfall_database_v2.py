"""
Harrison Weiss
homework_02

    Program that implements a class called RainfallTable that builds
    a dictionary of years and rainfall totals from njrainfall.txt.
    Implements different functions that allow the user to determine
    different traits of this data.

"""

import statistics


class RainfallTable():
    # Dictionary where everything will be stored
    rain_table = dict()
    months = ['January', 'February', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December']
    historical_median_rainfall = list()

    def build_historical_median(self):
        for x in range(1, 13):
            self.historical_median_rainfall.append(
                self.get_median_rainfall_for_month(x))

    def __init__(self, path):
        self.build_table(path)

    # Builds the table by appending new keys (year)
    # and their associated values (rainfall) to the rain_table being
    # stored in our instance of the RainfallTable
    def build_table(self, path):
        rain_file = open(path, 'r')
        for line in rain_file:
            tokens = line.split()
            year = int(tokens[0])
            rainfall_list = list()
            for item in tokens[1:]:
                rainfall_list.append(float(item))
            self.rain_table[year] = rainfall_list

    def get_rainfall(self, year, month):
        """
            Returns the rainfall associated with
            the given year and month.  Both values
            are assumed to be integers (month given
            as 1-12, year as a four digit year).
            Raises an exception if the year/month
            combination are not found
        """

        if type(year) != int or type(month) != int:
            raise TypeError
        # once we clear the above, we know were dealing with an int, so we can do math on it
        month -= 1  # Index of months starts at 0
        if year < min(self.rain_table.keys()) or year > max(self.rain_table.keys()):
            raise ValueError
        elif month < 0 or month > 11:
            raise ValueError
        # gets and returns the data we want
        for key in self.rain_table:
            if key == year:
                rainfall = self.rain_table[key][month]
        return rainfall

    def get_average_rainfall_for_month(self, month):
        """ 
            Returns the average rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """

        if type(month) != int:
            raise TypeError
        month -= 1  # Index starts at 0
        if month < 0 or month > 11:
            raise ValueError
        # calculates and returns the value we want
        total_rain = float()
        all_years = [self.rain_table[year][month]
                     for year in self.rain_table]
        for x in all_years:
            total_rain += x
        return round(total_rain / len(all_years), 2)

    def get_min_year(self):
        """
            Returns the minimum year in the table
        """
        return min(self.rain_table.keys())

    def get_max_year(self):
        """
            Returns the maximum year in the table
        """
        return max(self.rain_table.keys())

    def get_median_rainfall_for_month(self, month):
        """ 
            Returns the median rainfall associated with 
            the given month across all years in the table.  
            Month is assumed to be an integer (1-12.
            Raises an exception if the month is not valid.
        """
        if type(month) != int:
            raise TypeError
        month -= 1  # Index starts at 0
        if month < 0 or month > 11:
            raise ValueError
        # calculates and returns the value we want
        total_rain = float()
        all_years = [self.rain_table[year][month]
                     for year in self.rain_table]
        for x in all_years:
            total_rain += x
        # Using the statistics module, we dont have to sort the list
        # rainfall data: median() does this for us, likely by calling
        # sort() and then calculating the median.
        return round(statistics.median(all_years), 2)

    def get_average_rainfall_for_year(self, year):
        """ 
            Returns the average rainfall in
            the given year across all months.
            Raises exception if year is not
            in table
        """

        if year not in self.rain_table.keys():
            raise KeyError
        avg_rain = float()
        for item in self.rain_table[year]:
            avg_rain += item
        avg_rain = avg_rain / len(self.rain_table[year])
        return round(avg_rain, 2)

    def get_median_rainfall_for_year(self, year):
        """ 
            Returns the median rainfall in
            the given year across all months.
            Raises exception if year is not
            in table.
        """

        if year not in self.rain_table.keys():
            raise KeyError
        temp_rain = self.rain_table[year].copy()
        return round(statistics.median(temp_rain), 2)

    def get_all_by_year(self, year):
        """ 
            Returns the rainfall values for each
            month in the given year. Raise exception
            if year is not found.
        """

        if year not in self.rain_table.keys():
            raise KeyError
        for rain in self.rain_table[year]:
            yield rain

    def get_all_by_month(self, month):
        """ 
            Returns the rainfall values for each
            year during the given month.  Raise exception
            if month is not valid
        """

        month -= 1  # index starts at 0
        if month < 0 or month > 11:
            raise ValueError
        for key in self.rain_table:
            yield self.rain_table[key][month]

    def get_droughts(self):
        """ 
            returns a list of strings, representing date (month/year) ranges
            where three or more months in a row had at least 5% less rainfall than
            their historical monthly medians
        """

        which_month = 0  # to iterate over the months of the year
        start_drought = ""  # for being appended later
        end_drought = ""  # same as above
        month_count = 0  # for counting how many months we've seen 5% less than the median rainfall
        self.build_historical_median()

        for key in self.rain_table:
            which_month = 0  # every year we start at month 0
            for value in self.rain_table[key]:
                # calculate 5% less than the median
                if value < (self.historical_median_rainfall[which_month] * 0.95):
                    month_count += 1  # we've found a drought month so we can increment the count
                    if month_count == 1:  # this is the first drought
                        start_drought = str(
                            self.months[which_month]) + " " + str(key)
                    elif month_count > 1:  # otherwise, we've been in a drought
                        end_drought = str(
                            self.months[which_month]) + " " + str(key)
                else:  # for when the rainfall was not less than 5% of the median
                    if month_count > 3:  # for when we meet the condition of being a drought for three months
                        # we can yield the drought time period
                        yield str(start_drought + " to " + end_drought)
                        # reset the values to their initals
                        month_count = 0
                        start_drought = ""
                        end_drought = ""
                    else:
                        month_count = 0
                        start_drought = ""
                        end_drought = ""
                which_month += 1  # iterate to the next month


"""
    MAIN PROGRAM
"""

table = RainfallTable("njrainfall.txt")
print(table.get_rainfall(1993, 's'))
print(table.get_average_rainfall_for_month(6))

for year in range(table.get_min_year(), table.get_max_year()+1) :
    print("Average rainfall in ", year, "=", table.get_average_rainfall_for_year(year))
    print("Median rainfall in ", year, "=", table.get_median_rainfall_for_year(year))
    print("===========")
    for rain in table.get_all_by_year(year):
        print(rain, end='\t')
    print("\n===========")


for month in range(1, 13) :
    print("Average rainfall in month", month, "=", table.get_average_rainfall_for_month(month))
    print("Median rainfall in month", month, "=", table.get_median_rainfall_for_month(month))
    print("===========")
    for rain in table.get_all_by_month(month):
        print(rain, end='\t')
    print("\n===========")

for d in table.get_droughts() :
    print("Drought:  ", d)
