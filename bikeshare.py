import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """Gets user input for city, month, and day."""
    print("\nHello! Let's explore some US bikeshare data!")

    city = input("\nEnter city (Chicago, New York City, Washington): ").lower()
    while city not in CITY_DATA:
        city = input("Invalid city. Enter again: ").lower()

    month = input("\nEnter month (January - June) or 'all': ").lower()
    while month != 'all' and month not in months:
        month = input("Invalid month. Enter again: ").lower()

    day = input("\nEnter day of week (Sunday - Saturday) or 'all': ").lower()
    while day != 'all' and day not in days:
        day = input("Invalid day. Enter again: ").lower()

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for specified city and filters by month and day."""
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == months.index(month) + 1]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """Displays most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most common month:", months[df['month'].mode()[0] - 1].title())
    print("Most common day of week:", df['day_of_week'].mode()[0])
    print("Most common start hour:", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("Most commonly used start station:", df['Start Station'].mode()[0])
    print("Most commonly used end station:", df['End Station'].mode()[0])
    
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most common trip:", df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays trip duration statistics."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("Total travel time:", df['Trip Duration'].sum(), "seconds")
    print("Average travel time:", df['Trip Duration'].mean(), "seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nCounts of user types:\n", df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nCounts of gender:\n", df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\nEarliest year of birth:", int(df['Birth Year'].min()))
        print("Most recent year of birth:", int(df['Birth Year'].max()))
        print("Most common year of birth:", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        if input('\nWould you like to restart? Enter yes or no: ').lower() != 'yes':
            break

if __name__ == "__main__":
    main()
