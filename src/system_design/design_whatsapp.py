from collections import defaultdict
class WhatsApp:

    def __init__(self):
        self.user_msgs = defaultdict(list)
        self.groups = []

    def sendMessage(self, toUser: int, message: str) -> None:
        self.user_msgs[toUser].append(message)

    def createGroup(self, initialUsers: List[int]) -> int:
        self.groups.append(set(initialUsers))
        return len(self.groups)
        

    def addUserToGroup(self, groupId: int, userId: int) -> None:
        if groupId <= len(self.groups):
            self.groups[groupId - 1].add(userId)

    def sendGroupMessage(self, fromUser: int, groupId: int, message: str) -> None:
        if groupId > len(self.groups):
            return
        group = self.groups[groupId - 1]
        if fromUser in group:
            for user in [user for user in group if user != fromUser]:
                self.user_msgs[user].append(message)
    

    def getMessagesForUser(self, userId: int) -> List[str]:
        return self.user_msgs[userId][::-1]


# Your WhatsApp object will be instantiated and called as such:
# obj = WhatsApp()
# obj.sendMessage(toUser,message)
# param_2 = obj.createGroup(initialUsers)
# obj.addUserToGroup(groupId,userId)
# obj.sendGroupMessage(fromUser,groupId,message)
# param_5 = obj.getMessagesForUser(userId)
