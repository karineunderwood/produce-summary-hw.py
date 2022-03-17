def melon_count_all_days(day_num, path):
    """Here there's a function with a day number and path to the deliveries."""
    
    print("Day", day_num)
    deliveries = open(path)
    for line in deliveries:
        # this will remove extra whitespace "right side" of the line
        line = line.rstrip() 
        #  will creat a list of strings
        words = line.split('|')
        #  assign variables to each item
        melon = words[0]
        count = words[1]
        amount = words[2]

    print(f"Delivered {count} {melon}s for total of ${amount}")
    
    deliveries.close()

# Call all the functions for the 3 days.
melon_count_all_days(1, "um-deliveries-day-1.txt")
melon_count_all_days(2, "um-deliveries-day-2.txt")
melon_count_all_days(3, "um-deliveries-day-3.txt")
