"""

At LockedIn, we are interested in simulating the exponential growth of an influencer's followers over a certain period with an adjustable growth factor.

Assignment
Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

"""


def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    result = []

    for i in range(0, days + 1):
        if i == 0:
            result.append(n)
        else:
            result.append(n * (factor**i))

    return result
