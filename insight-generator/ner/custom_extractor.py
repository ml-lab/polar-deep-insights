import re
import nltk

from result import *

class CustomEntityExtractor:
  def __init__(self, content):
    self.lines = nltk.sent_tokenize(content)
    self.entitiesEx = re.compile(r'\b(health and society|bird wintering range|bird wintering ranges|leaf and bloom date|leaf and bloom dates|climate change indicator|climate change indicators|ocean surface temprature|sea surface temprature|tropical storm activity|tropical cyclone activity|heat stroke|lyme disease|growing season|natural gas|carbon dioxide|nitrous oxide|sulfur hexafluoride|climate change|fossil fuel|fossil fuels|sea level|tropical storm|tropical cyclone|storm activity|cyclonic activity|ocean level|fluorinated gas|fluorinated gases|water level|water levels|leaf dates|bloom dates|leaf date|bloom date|sea ice|arctic sea ice|antarctic sea ice|greenhouse gas|greenhouse gases|snow cover|ice cover|ocean acidity|sea acidity|ragweed pollen season|pollen season|crude oil|chlorinated hydrocarbon|chlorinated hydrocarbons|heat-related death|heat-related deaths|heat related death|heat related deaths|ozone hole|system state change|coal|co2|methane|ch4|n2o|perfluorocarbon|perfluorocarbonss|fluorocarbon|sf6|climate|weather|temperature|precipitation|drought|ocean|oceans|ocean heat|land loss|snow|ice|lake ice|snowfall|snowpack|society|health|ecosystem|ecosystems|wildfire|wildfires|streamflow|cfc|cfcs|chlorofluorocarbon|chlorofluorocarbons|cfc11|cfc113|cfc113a|cfc114|cfc115|cfc12|petroleum|petrol|cyclone|storm|hurricane|hurricanes|thunderstorm|thunderstorms|oil|increase|rise|decrease|fall|drop|reduction|decline|loss|transformation|transforming|destruction|removal|glacier|glaciers|halting|decay|retreat|loss|extension|replenishment|evolution|conversion|exchange|displacement|growth|disruption|innundation|maturation|disspiate|interruption|collapse|chemical process|burning|acidification|dilution|hydration|dehydration)\b')

    self.result = EntityResult()

  def extractEntities(self, line):
    return self.entitiesEx.findall(line)

  def extract(self):
    for l in self.lines:
      self.result.accumulate({
        'entities'  : self.extractEntities(l),
      })

    return self.result.freqDistribution()
