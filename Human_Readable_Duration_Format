# Level 4 Kata - Code Wars
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of 
# years, days, hours, minutes and seconds.


def format_duration(seconds):
    
    # Create and calculate variables for years, days, 
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = (seconds % 3600) % 60
    return_string = ""
    days = 0
    years = 0
    
    if hours > 24:
        days = hours // 24
        hours = hours % 24
    if days > 365:
        years = days // 365
        days = days % 365
    
    # Construct the list of variables.
    variable_list = []
    if years > 1:
        variable_list.append(str(years) + " years")
    if years == 1:
        variable_list.append("1 year")
        
    if days > 1:
        variable_list.append(str(days) + " days")
    if days == 1:
        variable_list.append("1 day")
        
    if hours > 1:
        variable_list.append(str(hours) + " hours")
    if hours == 1:
        variable_list.append("1 hour")
        
    if minutes > 1:
        variable_list.append(str(minutes) + " minutes")
    if minutes == 1:
        variable_list.append("1 minute")
        
    if secs > 1:
        variable_list.append(str(secs) + " seconds")
    if secs == 1:
        variable_list.append("1 second")
    
    # Construct the return string from the list of variables.
    if len(variable_list) == 5:
        return_string += variable_list[0] + ", " + variable_list[1] + ", " + variable_list[2] + ", " + variable_list[3] + " and " + variable_list[4]
    elif len(variable_list) == 4:
        return_string += variable_list[0] + ", " + variable_list[1] + ", " + variable_list[2] + " and " + variable_list[3]
    elif len(variable_list) == 3:
        return_string += variable_list[0] + ", " + variable_list[1] + " and " + variable_list[2]
    elif len(variable_list) == 2:
        return_string += variable_list[0] + " and " + variable_list[1]
    elif len(variable_list) == 1:
        return_string += variable_list[0]
    else:
        return_string = "now"
    
    # Return the return string.
    return return_string
