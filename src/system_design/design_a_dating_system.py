"""
["Tinder","signup","getMatches","signup","getMatches","signup","getMatches","getMatches","signup","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","signup","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","signup","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","signup","getMatches","getMatches","getMatches","getMatches","getMatches","getMatches","signup","getMatches","getMatches","signup","getMatches","getMatches","getMatches","signup","getMatches","getMatches","signup"]
[[],[2578,1,1,37,44,82,["Pet sitting","Compact discs"]],[2578],[1934,0,0,59,51,66,["Pet sitting","Zoo visiting","Upcycling","Weaving"]],[2578],[9135,0,1,84,76,79,["Knife collecting","Compact discs","Animation","Scuba Diving"]],[2578],[9135],[1150,0,1,20,74,89,["Scuba Diving","Zoo visiting","Photography","Animation","Pet sitting"]],[9135],[9135],[9135],[941],[5154],[1934],[1934],[1150],[9135],[5097,1,1,83,36,37,["Compact discs","Pet sitting","Weaving","Scuba Diving"]],[2578],[1150],[2578],[5097],[1934],[2174],[1878,0,1,19,25,68,["Zoo visiting","Tourism","Planning","Tarot"]],[1934],[9135],[5029],[5097],[5097],[1878],[801,1,1,39,65,87,["Pet sitting","Knife collecting","Witchcraft","Photography"]],[5097],[6665],[1150],[8958],[5097],[5097],[9925,1,0,29,55,85,["Compact discs"]],[1150],[1878],[8896,0,0,34,31,78,["Pet sitting","Jumping rope"]],[9925],[1878],[1150],[1660,1,1,81,28,60,["Meditation","Upcycling"]],[5097],[5097],[3437,0,1,60,68,74,["Weaving","Animation","Planning"]]]
"""
from collections import defaultdict

class User:
    def __init__(self, user_id, gender, preferred_gender, age, min_preferred_age, max_preferred_age, interests):
        self.user_id = user_id
        self.gender = gender
        self.preferred_gender = preferred_gender
        self.age = age
        self.min_preferred_age = min_preferred_age
        self.max_preferred_age = max_preferred_age
        self.interests = set(interests)
        
    def count_common_interests(self, interests):
        counter = 0
        for interest in interests:
            if interest in self.interests:
                counter += 1
        return counter

class UsersByAge:
    
    def __init__(self):
        # age -> set(User)
        self.users = defaultdict(set)
    
    def add(self, user: User):
        self.users[user.age].add(user)

    def getMatches(self, user: User):
        candidates = []
        for age in range(user.min_preferred_age, user.max_preferred_age + 1):
            for candidate in self.users[age]:
                count = candidate.count_common_interests(user.interests) 
                if  count > 0:
                    candidates.append([count, candidate])
        
        candidates = sorted(candidates, key = lambda x: [-x[0], x[1].user_id])
        candidates = [u[1].user_id for u in candidates if u[1].user_id != user.user_id]
        return candidates[:5]
        
class Tinder:

    def __init__(self):
        self.users = dict()
        self.gender_users = [UsersByAge() for _ in range(2)]
        self.count = 0
    def signup(self, userId: int, gender: int, preferredGender: int, age: int, minPreferredAge: int, maxPreferredAge: int, interests: List[str]) -> None:
        # print(self.count, userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests)
        self.count += 1
        user = User(userId, gender, preferredGender, age, minPreferredAge, maxPreferredAge, interests)
        self.users[userId] = user
        self.gender_users[gender].add(user)

    def getMatches(self, userId: int) -> List[int]:
        # print('getMatch', userId)
        if userId not in self.users:
            return []
        user = self.users[userId]
        
        return self.gender_users[user.preferred_gender].getMatches(user)
        


# Your Tinder object will be instantiated and called as such:
# obj = Tinder()
# obj.signup(userId,gender,preferredGender,age,minPreferredAge,maxPreferredAge,interests)
# param_2 = obj.getMatches(userId)
