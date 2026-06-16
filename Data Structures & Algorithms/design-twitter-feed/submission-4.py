class Twitter:
    def __init__(self):
        self.time = 0
        self.postsByUser = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.postsByUser[userId].append( [self.time,tweetId] )

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []

        if self.postsByUser[userId]:
            last_idx = len(self.postsByUser[userId]) - 1
            time, tweetId = self.postsByUser[userId][last_idx]
            pq.append([time,tweetId, userId, last_idx - 1])


        for follower in self.following[userId]:
            if self.postsByUser[follower]:
                last_idx = len(self.postsByUser[follower]) - 1
                time, tweetId = self.postsByUser[follower][last_idx]
                pq.append([time,tweetId, follower, last_idx - 1])

        heapq.heapify(pq)
        news = []
        while pq and len(news) < 10:
            time, tweetId, follower, last_idx = heapq.heappop(pq)
            news.append(tweetId)

            if last_idx >= 0:
                time, tweetId = self.postsByUser[follower][last_idx]
                heapq.heappush(pq,[time, tweetId, follower, last_idx - 1])
        
        return news
        


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 

        self.following[followerId].add(followeeId)        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return 

        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)   
        
