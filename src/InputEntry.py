import math

class InputData:
    def __init__(self, data):
        self.region_name = data['region']['name']
        self.average_age = data['region']['avgAge']
        self.average_Daily_Income_InUSD = data['region']['avgDailyIncomeInUSD']
        self.average_Daily_Income_population = data['region']['avgDailyIncomePopulation'] 
        self.time_to_elapse = data['timeToElapse']
        self.reported_cases = data['reportedCases']
        self.population = data['population']
        self.total_hospital_beds = data['totalHospitalBeds']
        self.period_type = data['periodType']
        

    def getFactor(self):
        if self.period_type == 'days':
            # return math.floor((self.time_to_elapse)/3)
            return (self.time_to_elapse)//3
        elif self.period_type == 'weeks':
            # return math.floor((self.time_to_elapse * 7)/3)
            return (self.time_to_elapse * 7)//3
        elif self.period_type == 'weeks':
            # return math.floor((self.time_to_elapse * 7)/3)
            return (self.time_to_elapse * 30)//3    
        else:
            # return math.floor((self.time_to_elapse * 30)/3)
            return (self.time_to_elapse * 360)//3  
                

    def getPeriod(self):
        if self.period_type == 'days':
            return self.time_to_elapse
        elif self.period_type == 'weeks':
            return self.time_to_elapse * 7
        else:
            return self.time_to_elapse * 30


