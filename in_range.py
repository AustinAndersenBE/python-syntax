def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    for num in (n for n in nums if n >= lowest and n <= highest): #this is a generator expression that filters the list of nums to only include those that are in range. It is more memory efficient
        print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
