"""

Let's create an "influencer score". It will be a small number (like less than 100) that will give influencers a metric for comparing their social media success against their peers.

Complete the get_influencer_score function. An influencer score is their average engagement percentage multiplied by log base 2 of their follower count.

"""

import math


def get_influencer_score(
    num_followers: int, average_engagement_percentage: float
) -> float:

    influencer_score = average_engagement_percentage * math.log(num_followers, 2)

    return influencer_score
