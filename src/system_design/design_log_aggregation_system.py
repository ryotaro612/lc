from collections import defaultdict
class LogAggregator:

    def __init__(self, machines: int, services: int):
        self.logs = dict()
        self.machine_logs = defaultdict(list)
        self.service_logs = defaultdict(list)

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.logs[logId] = message
        self.machine_logs[machineId].append(logId)
        self.service_logs[serviceId].append(logId)
        

    def getLogsFromMachine(self, machineId: int) -> List[int]:
        return self.machine_logs[machineId]

    def getLogsOfService(self, serviceId: int) -> List[int]:
        return self.service_logs[serviceId]

    def search(self, serviceId: int, searchString: str) -> List[str]:
        return [self.logs[log_id] 
                for log_id 
                in self.service_logs[serviceId]
                if searchString in self.logs[log_id]
               ]

# Your LogAggregator object will be instantiated and called as such:
# obj = LogAggregator(machines, services)
# obj.pushLog(logId,machineId,serviceId,message)
# param_2 = obj.getLogsFromMachine(machineId)
# param_3 = obj.getLogsOfService(serviceId)
# param_4 = obj.search(serviceId,searchString)
