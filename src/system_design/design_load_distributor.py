"""
["DCLoadBalancer","addMachine","addMachine","addMachine","addMachine","addApplication","addApplication","addApplication","addApplication","getApplications","addMachine","addApplication","stopApplication","addApplication","getApplications","removeMachine","getApplications"]
[[],[1,1],[2,10],[3,10],[4,15],[1,3],[2,11],[3,6],[4,5],[2],[5,10],[5,5],[3],[6,5],[4],[4],[2]]

["DCLoadBalancer","addMachine","getApplications","addMachine","getApplications","getApplications","removeMachine","getApplications","addMachine","getApplications","getApplications","addMachine","removeMachine","addApplication","addMachine","removeMachine","getApplications","getApplications","addApplication","addMachine","addMachine","getApplications","getApplications","getApplications","addApplication","removeMachine","removeMachine","removeMachine","addApplication","getApplications","removeMachine","addMachine","addApplication","getApplications","removeMachine","addMachine","getApplications","getApplications","addMachine","removeMachine","addMachine","addApplication","getApplications","getApplications","getApplications","getApplications","getApplications","getApplications","getApplications","getApplications","removeMachine","getApplications","addApplication","getApplications","getApplications","addApplication","addMachine","addApplication","getApplications","getApplications"]
[[],[12264,47135],[12264],[23997,34056],[12264],[12264],[12264],[23997],[98265,54003],[23997],[98265],[54533,71366],[98265],[78014,8255],[43462,85258],[54533],[23997],[43462],[92855,18342],[87711,47893],[15946,54614],[43462],[87711],[87711],[81574,91970],[23997],[87711],[15946],[95319,30396],[43462],[43462],[37053,57590],[42444,41923],[37053],[37053],[99424,56702],[99424],[99424],[23317,9135],[99424],[55754,74790],[96466,15626],[55754],[23317],[23317],[23317],[55754],[23317],[55754],[55754],[55754],[23317],[84463,77320],[23317],[23317],[21655,29544],[49468,56127],[50191,1576],[23317],[23317]]
"""

import heapq

class DCLoadBalancer:

    def __init__(self):
        self.heap = []
        self.machine_apps =dict()
        self.app_machine = dict()
        self.machine_cap = dict()
        

    def addMachine(self, machineId: int, capacity: int) -> None:
        """Registers a machine with the given machineId and maximum capacity.
        """
        heapq.heappush(self.heap, [-capacity, machineId])
        self.machine_apps[machineId] = dict()
        self.machine_cap[machineId] = capacity
        # print('add machine', self.heap)
        
    def removeMachine(self, machineId: int) -> None:
        """Removes the machine with the given machineId. 
        
        All applications running on this machine are automatically 
        reallocated to other machines in the same order as they were added to this machine. 
        The applications should be reallocated in the same manner as addApplication.
        """
        del self.machine_cap[machineId]
        apps = self.machine_apps[machineId]
        # apps: app_id -> [load, is_removed]
        del self.machine_apps[machineId]
        for app_id in apps:
            if app_id in self.app_machine:
                del self.app_machine[app_id]
            
        new_heap = []
        machine_ids = set()
        for cap, m_id in self.heap:
            if m_id not in machine_ids and machineId != m_id:
                heapq.heappush(new_heap, [cap, m_id])
                machine_ids.add(m_id)
                
        self.heap = new_heap
        
        for app_id in apps:
            if apps[app_id][1]:
                self.addApplication(app_id, apps[app_id][0])
         
        # print('removeMachine', machineId, self.machine_apps, self.app_machine)

    def addApplication(self, appId: int, loadUse: int) -> int:
        """Allocates an application with the given appId and loadUse to 
        the machine with the largest remaining capacity that can handle the additional request. 
        If there is a tie, the machine with the lowest ID is used. 
        Returns the machine ID that the application is allocated to. 
        If no machine can handle the request, return -1.
        """
        
        if self.heap and -self.heap[0][0] >= loadUse:
            capacity, machine_id = heapq.heappop(self.heap)
            self.machine_cap[machine_id] -= loadUse
            heapq.heappush(self.heap, [capacity + loadUse, machine_id])
            self.machine_apps[machine_id][appId] = [loadUse, True]
            self.app_machine[appId] = machine_id
            # print('add app', appId, loadUse, self.machine_apps, self.app_machine)
            return machine_id
        else:
            return -1

    def stopApplication(self, appId: int) -> None:
        """Stops and removes the application with the given appId from the machine it is running on,              freeing up the machine's capacity by its corresponding loadUse.
            If the application does not exist, nothing happens.
        """
        if appId not in self.app_machine:
            return
        
        machine_id = self.app_machine[appId]
        del self.app_machine[appId]
        self.machine_cap[machine_id] += self.machine_apps[machine_id][appId][0]
        self.machine_apps[machine_id][appId][1] = False
        heapq.heappush(self.heap, [-self.machine_cap[machine_id], machine_id])
        # print('stop_app', appId, self.machine_apps, self.app_machine)

    def getApplications(self, machineId: int) -> List[int]:
        """ Returns a list of application IDs running on a machine with the given machineId in the order in which they were added. If there are more than 10 applications, return only the first 10 IDs.
        """
        apps = self.machine_apps.get(machineId, dict())
        stopped = []
        result = []
        for app_id in apps:
            is_running = apps[app_id][1]
            if is_running:
                result.append(app_id)
                if len(result) == 10:
                    break
            else:
                stopped.append(app_id)
        
        for app_id in stopped:
            del apps[app_id]
        
        # print('get apps', machineId, self.machine_apps, self.app_machine)
        return result
"""
DCLoadBalancer()
addMachine(1, 1)
addMachine(2, 10)
addMachine(3, 10)
addMachine(4, 15)
addApplication(1, 3)
addApplication([2,11)
addApplication(3,6)
addApplication(4,5)
getApplications(2)
addMachine(5, 10)
addApplication(5, 5)
stopApplication(3)
addApplication(6, 5)
getApplications(4)
removeMachine(4)
getAplications(2)
"""
# Your DCLoadBalancer object will be instantiated and called as such:
# obj = DCLoadBalancer()
# obj.addMachine(machineId,capacity)
# obj.removeMachine(machineId)
# param_3 = obj.addApplication(appId,loadUse)
# obj.stopApplication(appId)
# param_5 = obj.getApplications(machineId)
