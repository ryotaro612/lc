class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_min = self.to_min(loginTime)
        logout_min = self.to_min(logoutTime)
        
        if logout_min < login_min:
            logout_min += 24*60
        
        while login_min % 15:
            login_min += 1
        while logout_min % 15:
            logout_min -= 1
        
        count = 0
        while login_min < logout_min:
            login_min += 15
            count += 1

        return count

    def to_min(self, time):
        return int(time[:2]) * 60 + int(time[3:])
