class Twitter:

    def __init__(self):
        # map of userIDs to people they follow
        self.followMap = defaultdict(set)

        # stores userIDs and their tweets as a list of count, tweetid pairs
        # where count tracks tweet orders and is incremented on every tweet
        self.tweetMap = defaultdict(list)

        # tracker for tweet orders
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # add new tweet to tweet map with (count, tweetId)
        # count represents how recent the tweet was, with a lower number being
        # more recent
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # add user's own userId into following map
        self.followMap[userId].add(userId)

        # add first tweet from every user the user follows, including
        # user themselves
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:

                # start from most recent tweet (end of list)
                index = len(self.tweetMap[followeeId]) - 1

                # push onto min heap
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:

            # pop the top 10 most recent tweets from the heap
            # and add to the result
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # add that user's next tweet into the heap. 
            # heap sorting preserves the order
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # add a followee id to the list of followMap[followerId]
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove a followee id from list of followMap[followerId]
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
