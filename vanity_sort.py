"""

We need to sort influencers by vanity. Complete the vanity and vanity_sort functions.

The vanity function accepts an instance of an Influencer and returns their vanity score. The vanity score should be the number of links in their bio multiplied by 5, plus their number of selfies. (Links in bio are weighted more heavily)

The vanity_sort function should return a list of influencers, ordered by their vanity from least to greatest. You can pass a function as a named parameter called key to sorted to control the metric the sorting algorithm will use for comparisons.

"""

class Influencer:
    def __init__(self, num_selfies: int, num_bio_links: int) -> None:
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self) -> str:
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer: Influencer) -> int:
    vanity_score = (influencer.num_bio_links * 5) + influencer.num_selfies

    return vanity_score


def vanity_sort(influencers: list[Influencer]) -> list[Influencer]:
    return sorted(influencers, key=vanity) 
