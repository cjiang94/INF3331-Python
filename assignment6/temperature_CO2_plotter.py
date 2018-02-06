import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)

def plot_temperature(m, a, b, min, max):
    """
    This function will plot the temperatures for a given month m, within the time range a-b and temperature range min-max.
    m: The month the user chooses as a number
    a: The year the user wants to read temperatures FROM
    b: The year the user wants to read temperatures TO
    min: Minimum temperature the user wants to read
    max: Maximum temperature the user wants to read
    """

    """
    For months the function takes in a number instead of the name of the month. It would be faster with typing the month, but I've decided to do it this way! :D
    """
    month_list = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    month = month_list[m];
    temp_stats = pd.read_csv('temperature.csv', sep = ',')
    temp_stats.index = temp_stats['Year']
    del temp_stats['Year']
    print(temp_stats[month].loc[a:b])
    temp_stats[month].loc[a:b].plot()
    plt.ylim(ymax = max, ymin = min)
    plt.ylabel('Temperature')
    plt.xlabel('Year')
    plt.legend()
    plt.show()

def plot_CO2(a, b, min, max):
    """
    This function will plot the CO2 levels for a given time range a-b and CO2 range min-max.
    a: The year the user wants to read CO2 levels FROM
    b: The year the user wants to read CO2 levels TO
    min: Minimum CO2 level the user wants to read
    max: Maximum CO2 level the user wants to read
    """

    """
    I've used a zero, 0, instead of O in "CO2", because apperantly CO2 is a reserved variable...?
    """
    C02_stats = pd.read_csv('co2.csv', sep = ',')
    C02_stats.index = C02_stats['Year']
    del C02_stats['Year']
    C02_stats.loc[a:b].plot()
    plt.ylim(ymax = max, ymin = min)
    plt.ylabel('CO2 levels')
    plt.xlabel('Year')
    plt.legend()
    plt.show()

#Test, uncomment to see :D
plot_temperature(6, 1880, 2017, 0, 22)
plot_CO2(1774, 1842, 0, 20)
