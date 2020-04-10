from Impact import computeForImpact
from Severe import computeForSevereImpact
import json

def estimator(data):
  impact = computeForImpact(data)
  severe = computeForSevereImpact(data)
  data_output = {}
  data_output['data'] = {}
  data_output['estimate'] = {}
  data_output['estimate']['impact'] = {}
  data_output['estimate']['severeImpact'] = {}
  data_output['data'].update(data)
  data_output['estimate']['impact'].update(impact)
  data_output['estimate']['severeImpact'].update(severe)
  data = data_output
  return data




if __name__ == "__main__":
  data = {}
  data['region'] = {}
  data['region']['name'] = "Africa"
  data['region']['avgAge'] =  19.7
  data['region']['avgDailyIncomeInUSD'] = 4
  data['region']['avgDailyIncomePopulation']  = 0.73 
  data['timeToElapse'] = 38 
  data['reportedCases'] = 2747
  data['population'] = 92931687
  data['totalHospitalBeds'] = 678874
  data['periodType'] = "days"

  # print(data)
  # print(estimator(data))
  with open('data.json', 'w') as outfile:
      json.dump(estimator(data), outfile)




