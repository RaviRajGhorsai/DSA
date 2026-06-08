"""

Logarithmic Scale
In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale. A logarithmic scale can help by compressing the data so that it's easier to understand.

For example, at LockedIn we have influencers with follower counts ranging from 1 to 1,000,000,000. If we want to plot the follower count of each influencer on a graph, it would be difficult to see the differences between the smaller follower counts. We can use a logarithmic scale to compress the data so that it's easier to visualize.

"""

import math

def log_scale(data: list[float], base: float) -> list[float]:

    res = []

    for num in data:
        res.append(math.log(num, base))

    return res
