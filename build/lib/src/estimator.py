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







