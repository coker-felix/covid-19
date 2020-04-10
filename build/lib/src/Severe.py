from InputEntry import InputData

def computeForSevereImpact(data):
    # Create new instance of InputData class
    impactdata = InputData(data)

    # Make computations
    # CHALLENGE 1
    currentlyInfected = impactdata.reported_cases * 50
    factor = impactdata.getFactor()
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)
    infectionsByRequestedTime = round(infectionsByRequestedTime)

    # CHALLENGE 2
    severeCasesByRequestedTime = (15/100) *  infectionsByRequestedTime
    severeCasesByRequestedTime = round(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime  = ((35/100) * impactdata.total_hospital_beds) - severeCasesByRequestedTime
    hospitalBedsByRequestedTime = round(hospitalBedsByRequestedTime)

    # CHALLENGE 2
    casesForICUByRequestedTime = (5/100) * infectionsByRequestedTime
    casesForICUByRequestedTime = round(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = (2/100) * infectionsByRequestedTime
    casesForVentilatorsByRequestedTime = round(casesForVentilatorsByRequestedTime)

    period = impactdata.getPeriod()
    dollarsInFlight = infectionsByRequestedTime * impactdata.average_Daily_Income_population * impactdata.average_Daily_Income_InUSD * period
    dollarsInFlight = round(dollarsInFlight, 2)

    data = {}
    data['currentlyInfected'] = currentlyInfected
    data['infectionsByRequestedTime'] = infectionsByRequestedTime
    data['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    data['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    data['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    data['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
    data['dollarsInFlight'] = dollarsInFlight
    severeResult = data
    return severeResult



