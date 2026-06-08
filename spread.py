""" In the social media industry, there is a concept called "spread": how much a post spreads due to "reshares"
after all of the original author's followers see it. As it turns out, social media posts spread at an exponential 
rate! """

def get_estimated_spread(audiences_followers: list[int]) -> float:
    if len(audiences_followers) == 0:
        return 0

    num_followers = len(audiences_followers)
    
    average_audience_followers = sum(audiences_followers) / num_followers
    
    estimated_spread = average_audience_followers * ( num_followers ** 1.2 )

    return estimated_spread
