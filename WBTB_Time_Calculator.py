from datetime import datetime, timedelta

# Ask the user for their bedtime
bedtime_str = input('Enter your bedtime (hh:mm): ')

# Parse the bedtime string to get a datetime object
bedtime = datetime.strptime(bedtime_str, '%H:%M')

# Calculate the WBTB time by adding 5.5 hours to the bedtime
wbtb_time = bedtime + timedelta(hours=5.5)

# Format the WBTB time as a string and print it
wbtb_time_str = wbtb_time.strftime('%H:%M')
print(f'Your WBTB time is: {wbtb_time_str}')
