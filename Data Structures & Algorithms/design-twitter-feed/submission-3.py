class Twitter:
    def __init__(self):
        self.time = 0
        self.postsByUser = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.postsByUser[userId].append( [self.time,tweetId] )

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = self.postsByUser[userId][::]

        for follower in self.following[userId]:
            for item in self.postsByUser[follower]:
                pq.append(item)
        
        heapq.heapify(pq)

        count = 10
        news = []
        while pq and count > 0:
            news.append( heapq.heappop(pq)[1] )
            count -= 1
        
        return news


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 

        self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 

        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)   
        
