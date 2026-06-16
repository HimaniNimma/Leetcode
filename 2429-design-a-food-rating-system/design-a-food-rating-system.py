class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}     
        self.cuisine_map = {}    
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            if c not in self.cuisine_map:
                self.cuisine_map[c] =[]
            heapq.heappush(self.cuisine_map[c], (-r, f))      

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_map[cuisine]
        while heap:
            rating, food = heap[0]  
            current_cuisine, current_rating = self.food_info[food]
            if -rating == current_rating: 
                return food
            heapq.heappop(heap) 


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)