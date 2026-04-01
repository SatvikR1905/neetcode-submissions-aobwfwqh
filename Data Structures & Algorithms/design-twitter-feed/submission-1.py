class Twitter:

    def __init__(self):
        self.hash_tweets = {}
        self.hash_following = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.hash_tweets:
            self.hash_tweets[userId] = []
        self.time += 1
        self.hash_tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.hash_tweets.get(userId, []):
            heapq.heappush(heap,(-tweet[0],tweet[1]))

        followees = self.hash_following.get(userId, set())
        for followeeId in followees:
            if followeeId == userId:
                continue
                
            for tweet in self.hash_tweets.get(followeeId,[]):
                heapq.heappush(heap, (-tweet[0],tweet[1]))

        count = 0
        output = []
        while count < 10 and heap:
            recent_tweet = heapq.heappop(heap)
            count += 1
            output.append(recent_tweet[1]) # we only need tweet Id
        return output
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hash_following:
            self.hash_following[followerId] = set()
        self.hash_following[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hash_following:
            self.hash_following[followerId].discard(followeeId) # can use remove as well but discard will throw an error if the element doesnt exist so discard is much safer


        
