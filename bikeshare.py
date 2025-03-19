import time
import pandas as pd

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

def display_raw_data(df):
    """Displays raw data upon user request."""
    i = 0
    while True:
        show_data = input("\nWould you like to see 5 rows of raw data? Enter yes or no: ").lower()
        if show_data != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5

def descriptive_statistics(df):
    """Displays descriptive statistics for the dataset."""
    print("\nCalculating Descriptive Statistics...\n")
    start_time = time.time()

    print("\n General Statistics ")
    print(df.describe())

    print("\n Trip Duration Statistics ")
    print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
    print(f"Mean travel time: {df['Trip Duration'].mean()} seconds")
    print(f"Median travel time: {df['Trip Duration'].median()} seconds")
    print(f"Standard deviation of travel time: {df['Trip Duration'].std()} seconds")
    print(f"90th percentile of travel time: {df['Trip Duration'].quantile(0.9)} seconds")

    if 'Birth Year' in df.columns:
        print("\n User Age Distribution ")
        print(f"Earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"Most common year of birth: {int(df['Birth Year'].mode()[0])}")
        print(f"Median year of birth: {int(df['Birth Year'].median())}")
        print(f"Standard deviation of birth years: {df['Birth Year'].std()}")

    print("\n User Type Distribution ")
    print(df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\n Gender Distribution ")
        print(df['Gender'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        descriptive_statistics(df)

        if input('\nWould you like to restart? Enter yes or no: ').lower() != 'yes':
            break

if __name__ == "__main__":
    main()
