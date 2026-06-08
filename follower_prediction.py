"""

Geometric Series

While the influencers who use our platform are really great at taking selfies, most aren't super great at math. We need to write a tool that predicts an influencer's follower growth over time.

"""

def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    
    if influencer_type == "fitness":
        follower_count = follower_count * (4 ** num_months)

    elif influencer_type == "cosmetic":
        follower_count = follower_count * (3 ** num_months)
    
    else:
        follower_count = follower_count * (2 ** num_months)

    return follower_count
