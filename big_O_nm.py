"""
O(nm)
O(nm) is very similar to O(n^2), but instead of a single input that we care about, there are two. If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.

"""

def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:

    count = 0
    for handles in all_handles:
        
        for handle in handles:
            if brand_name in handle:
                count += 1
        

    avg_follower = count / len(all_handles)

    return avg_follower
