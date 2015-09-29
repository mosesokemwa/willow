# GIGASECOND ANNIVERSARY
# LANGUAGE: PYTHON

# Write a function that will calculate the date that someone will celebrate their 1 gigasecond anniversary.

# Note: A gigasecond is one billion (10**9) seconds.

# The input is three parameters representing someone's birthday.

# As a convenience for celebration planning, the function should also calculate the day of the week and the number of days from today.

# The output should be an array formatted as such: ["YYYY-MM-DD", 'day_of_the_week', days_until]

# You can google datetime in python to familiarize yourself with it


# Examples:

# gigasecond(1988, 5, 15) # ["2020-01-22", "Wednesday", "1764 days left"]
# gigasecond(2015, 2, 17) # ["2046-10-26", "Friday", "11538 days left"]

import datetime, time
def get_user_b_date(year,month,day):
    list_date = []
    list_date.append(str(year))
    list_date.append(str(month))
    list_date.append(str(day))

    date_con = ','.join(list_date)
    t = datetime.datetime(int(list_date[0]),int(list_date[1]),int(list_date[2]))
    time_living = time.mktime(t.timetuple())
    gig_secs = 10 ** 9
    time_rem = gig_secs - time_living


#print int(datetime.timedelta(seconds=10 ** 9) - time_living )


get_user_b_date(1992,8,31)

