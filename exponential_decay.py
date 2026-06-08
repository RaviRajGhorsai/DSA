"""
Exponential Decay
In physics, exponential decay is a process where a quantity decreases over time at a rate proportional to its current value.

We've found that LockedIn influencers tend to lose followers similarly. This means that the more followers you have, the faster you lose them.


The retention_rate is the opposite of fraction_lost_daily. If an influencer lost 0.2 (or 20%) of their followers each day, then the retention rate would be 0.8 (or 80%).


"""


def decayed_followers(
    initial_followers: int, fraction_lost_daily: float, days: int
) -> float:

    retention_rate = 1 - fraction_lost_daily
    final_followers = initial_followers * (retention_rate ** days)

    return final_followers
