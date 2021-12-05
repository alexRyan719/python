# Level 5 Kata - Code Wars
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)


def make_readable(seconds):
    # Declare string variable to return human readable time.
    hum_read_time = ""
    
    # Create int variables for hours, minutes, and seconds from the input seconds.
    hour = seconds // 3600
    seconds -= (3600 * hour)
    minute = seconds // 60
    seconds -= (60 * minute)
    second = seconds % 21600
    
    # Build return string.
    if hour < 10:
        hum_read_time += "0"
    hum_read_time += str(hour) + ":"
    if minute < 10:
        hum_read_time += "0"
    hum_read_time += str(minute) + ":"
    if second < 10:
        hum_read_time += "0"
    hum_read_time += str(second)    
    
    # Return the return string.
    return hum_read_time
