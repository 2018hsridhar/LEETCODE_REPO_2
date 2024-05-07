'''
1333. Filter Restaurants by Vegan-Friendly, Price and Distance
URL := https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

Complexity
Let N := #-restaurants
Time := O(N)
Space := O(N) ( E ) O(1) ( I ) 

URL := https://stackoverflow.com/questions/1314314/how-can-i-filter-items-from-a-list-in-python

OMG the level of list functional programming
map(x) and reduce(x) are objects -> conv to list(...)

'''
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # Woah PY3 filter objects and lists created on filters
        # [veganFriendly, price, distance ] last 3 fields packaged
        # (A) filter a second time OR (B) if cond the filter itself
        # (tuple[2] == veganFriendly if veganFriendly)
        filterTransform = list(filter(lambda tuple : ( tuple[3] <= maxPrice and tuple[4] <= maxDistance), restaurants))
        if(veganFriendly):
            filterTransform = list(filter(lambda tuple : ( tuple[2] == veganFriendly and tuple[3] <= maxPrice and tuple[4] <= maxDistance), restaurants))
        # [id,rating] data packaged in first two fields : orderBy(rating,id)
        idsOnlyReduce = [restInfo[0] for restInfo in sorted(filterTransform, key=lambda tuple : (tuple[1], tuple[0]), reverse=True)]
        return idsOnlyReduce
        
