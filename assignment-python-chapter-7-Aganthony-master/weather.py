# Follow the instructions for coding a weather app
# Daily high temperatures
high_temps = [62, 64, 79, 52, 46, 50, 58, 66, 71, 75, 78, 78, 76, 80, 77]

# Daily low temperatures
low_temps = [42, 48, 47, 26, 28, 28, 32, 37, 43, 46, 48, 47, 48, 49, 50]

# Daily humidity
humidity = [0.48, 0.53, 0.46, 0.44, 0.4, 0.6, 0.58,
            0.5, 0.48, 0.43, 0.41, 0.39, 0.39, 0.3, 0.4]

# Calculate the maximum high temperature
max_high = max(high_temps)

# Calculate the minimum low temperature
min_low = min(low_temps)

# Calculate the average high temperature
avg_high = sum(high_temps) / len(high_temps)
# Calculate the average low temperature
avg_low = sum(low_temps) / len(low_temps)

# Calculate the average humidity
avg_humidity = sum(humidity) / len(humidity)

# Round the temperatures to zero decimal places
max_high = round(max_high)
avg_high = round(avg_high)
min_low = round(min_low)
avg_low = round(avg_low)

# Round the humidity to two decimal places
avg_humidity = round(avg_humidity, 2)

# Output the results to the terminal
print("The average low will be " + str(avg_low) + "°F")
print("Maximum high temperature over the next 15 days: " + str(max_high) + "°F")
print("Minimum low temperature over the next 15 days: " + str(min_low) + "°F")
print("Average high temperature over the next 15 days: " + str(avg_high) + "°F")
print("Average humidity over the next 15 days: " + str(avg_humidity))
