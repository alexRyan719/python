# Level 5 Kata - Code Wars
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
    stripped_url = ""
    
    # Strip http:// or https:// if the url begins with it.
    if url[:7] == "http://":
        url = url[7:]
    elif url[:8] == "https://":
        url = url[8:]
    
    # Strip www. if it exists in url.
    if url[:4] == "www.":
        url = url[4:]
        
    # Build the stripped url with chars up until a period.
    for char in url:
        if char == ".":
            break
        else:
            stripped_url += char
            
    # Return the stripped url.
    return stripped_url
