import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input("Would you like to see data for (chicago or new york city or washington)?\n").lower()
        try:
            df=pd.read_csv(CITY_DATA[city])
            break
        except:
            print("You Entered invalid city ")
            
    print()
            

    # get user input for month (all, january, february, ... , june)
    while True:
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month=input("Would you like to filter the data by month?\nIf 'yes' Type which month: january, february, march, april, may, june \nIf 'no time filter' Type 'all'\n").lower()
        try:
            df['Start Time']=pd.to_datetime(df['Start Time'])
            df['month']=df['Start Time'].dt.month
            if month != 'all':
                month=months.index(month) +1
                df=df[df['month'] == month]
                break
            elif month =='all':
                break
        except:
            print("You Entered invalid month")
            
    print()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        day=input("Would you like to filter the data by day?\nIf 'yes' Type which day: monday, tuesday, wednesday, thursday, friday, saturday, sunday\nIf 'no time filter' Type 'all'\n").lower()
        try:
            df['Start Time']=pd.to_datetime(df['Start Time'])
            df['day_of_week'] = df['Start Time'].dt.weekday_name
            if day in days:
                df=df[df['day_of_week']==day.title()]
                break
            elif day =='all':
                break
        except:
            print("You Entered invalid day")
            
    print()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        - load data file into a dataframe
        - convert the Start Time column to datetime
        - extract month and day of week from Start Time to create new columns
        - filter by month if applicable
        - filter by day of week if applicable
        - print the first five rows of the filtered dataframe
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    parameters:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        - convert the Start Time column to datetime
        - extract month , day of week, and hour from Start Time to create new columns
        - Pandas DataFrame: mode()[0] function to get most common month, day of week ,and hour
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time']=pd.to_datetime(df['Start Time'])

    """ display the most common month"""
    
    df['month']=df['Start Time'].dt.month
    
    popular_month=df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)


    """ display the most common day of week"""
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day=df['day_of_week'].mode()[0]
    print('Most Frequent Day:', popular_day)


    """ display the most common start hour"""
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

    """ find the most common hour (from 0 to 23)"""
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    parameters:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        -create a new column name:combine_stations is a ombination of start station and end station
        - Pandas DataFrame: mode()[0] function to get most common start station,
          end station,and combination of start station and end  station trip
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """ display most commonly used start station"""
    
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)


    """ display most commonly used end station"""
    
    popular_end_station=df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)


    """ display most frequent combination of start station and end station trip"""
    
    df['combine_stations']=df['Start Station']+" to "+df['End Station']
    trip=df['combine_stations'].mode()[0]
    print('Most Frequent trip:', trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    parameters:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        - Pandas DataFrame : sum() function to get total travel time
        - Pandas DataFrame: mean() function to get mean travel time
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """ display total travel time"""
    
    total_duration=df['Trip Duration'].sum()
    print("The Total Trip Duration:",total_duration,"Seconds")


    """ display mean travel time"""
    
    average_duration=df['Trip Duration'].mean()
    print("The Average Trip Duration:",average_duration,"Seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    parameters:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        -use try except statements to handle the case of washingtion city that doesn't have Gender and Birth Year columns
        - use pandas.Series.value_counts() function to get counts of user types and counts of gender
        - Pandas DataFrame : min() function to get the earliest year of birth
        - Pandas DataFrame : max() function to get the recent year of birth
        - Pandas DataFrame: mode()[0] function to get most common  year of birth
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """ Display counts of user types"""
    
    user_types=pd.Series(df['User Type']).value_counts()
    print("Number for each User Type:",user_types)


    """ Display counts of gender"""
    try:
        gender_counts=pd.Series(df['Gender']).value_counts()
        print("\nNumber for each User Gender:",gender_counts)
        
    except:
        print("Gender info not exist in the Dataset")


    """ Display earliest, most recent, and most common year of birth"""
    
    try:
        earliest_year=df['Birth Year'].min()
        recent_year=df['Birth Year'].max()
        pouplar_year=df['Birth Year'].mode()[0]
        print("The Earliest Year Of Birth:",earliest_year)
        print("The Recent Year Of Birth:",recent_year)
        print("Most Frequent Year Of Birth:",pouplar_year)
        
    except:
        print("Birth Year info not exist in the Dataset")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays the filtered dataframe.
    parameters:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Steps:
        - Ask the user if he wants to see the first 5 rows of data
        - use while loop to test the input from the user 
        - Ask another question inside while loop if he want to see the next 5 rows of data
    
    """
    view_data = input("Do you want to see the first 5 rows of data? Enter yes or no?\n").lower()
    view_display="yes"
    start_loc = 0
    end_loc=5
    while view_data !="no" and view_display !="no" and start_loc<=df.shape[0] :
        print(df.iloc[start_loc:end_loc])
        start_loc+=5
        end_loc+=5
        view_display = input("Do you want to see the next 5 rows of data?\n").lower()
        
        
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
