import matplotlib.pyplot as plt
import numpy as np

import statistics
 
data = [-55, -57, -61, -55, -57, -61, -55, -58, -63, -55, -58, -62, -55, -59, -62, -55, -56, -61, -55, -57, -59, -55, -57, -59, -55, -58, -59, -55, -59, -59, -55, -58, -60, -55, -59, -61, -55, -58, -62, -57, -56, -54, -55, -53, -62, -55, -57, -62, -55, -56, -64, -55, -57, -64, -55, -58, -65, -59, -55, -60, -62, -55, -60, -62, -55, -61, -62, -55, -60, -62, -55, -59, -62, -55, -58, -61, -55, -59, -61, -55, -63, -61, -55, -63, -60, -55, -62, -60, -55, -62, -64, -55, -60, -63, -55, -61, -63, -55, -60, -62, -59, -59, -58, -56, -57, -56, -57, -57, -55, -56, -62, -55, -58, -63, -56, -58, -56, -57, -58, -57, -55, -59, -63, -55, -60, -63, -55, -59, -61, -55, -60, -61, -55, -59, -64, -55, -58, -64, -55, -59, -63, -55, -57, -63, -55, -56, -62, -55, -57, -62, -55, -59, -61, -55, -60, -61, -55, -59, -61, -55, -59, -60, -55, -58, -59, -55, -59, -61, -55, -60, -62]

data2 = [55, 57, 61, 55, 57, 61, 55, 58]
x = statistics.mean(data2)
a = np.std(data2)     

print("desvio:", a)

print("media:", x)

'''
x = (1, 3)
y = (1, 3) # Effectively y = x**2


plt.errorbar(x, y,1, ls='None', lw=2, capthick=2) 

plt.show()

# example data
x = np.arange(0.1, 4, 3)
y = np.exp(-x)

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr


ax =plt.subplots()


ax.errorbar(x, y, yerr=yerr, fmt='o')
ax.set_title('Vert. symmetric')

plt.show()


# Calculate the mean and standard deviation for number of check outs
# each day
mean_total_co_day = daily_data[['weekday', 'cnt']].groupby('weekday').agg([np.mean, np.std])
mean_total_co_day.columns = mean_total_co_day.columns.droplevel()

# Define a function for a bar plot
def barplot(x_data, y_data, error_data, x_label, y_label, title):
    _, ax = plt.subplots()
    # Draw bars, position them in the center of the tick mark on the x-axis
    ax.bar(x_data, y_data, color = '#539caf', align = 'center')
    # Draw error bars to show standard deviation, set ls to 'none'
    # to remove line between points
    ax.errorbar(x_data, y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

# Call the function to create plot
barplot(x_data = mean_total_co_day.index.values
        , y_data = mean_total_co_day['mean']
        , error_data = mean_total_co_day['std']
        , x_label = 'Day of week'
        , y_label = 'Check outs'
        , title = 'Total Check Outs By Day of Week (0 = Sunday)')'

        '''