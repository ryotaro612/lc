from collections import defaultdict

class Facebook:

    def __init__(self):
        self.t = 0
        self.user_friends = defaultdict(set)
        self.user_posts = defaultdict(list)

    def writePost(self, userId: int, postContent: str) -> None:
        self.user_posts[userId].append([self.t, postContent])
        self.t += 1

    def addFriend(self, user1: int, user2: int) -> None:
        self.user_friends[user1].add(user2)
        self.user_friends[user2].add(user1)
        

    def showPosts(self, userId: int) -> List[str]:
        
        posts = []
        
        for friend in {f for f in self.user_friends[userId] if f != userId}:
            posts.extend(self.user_posts[friend])
        
        posts = sorted(posts, reverse=True)
        return [e[1] for e in posts]

# Your Facebook object will be instantiated and called as such:
# obj = Facebook()
# obj.writePost(userId,postContent)
# obj.addFriend(user1,user2)
# param_3 = obj.showPosts(userId)
