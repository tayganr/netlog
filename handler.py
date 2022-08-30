import json
from datetime import datetime
import csv

# READ FILE
INPUT_FILE = './input/netlog.json'
with open(INPUT_FILE) as f:
    d = json.load(f)

# CONSTANTS
constants = d.get('constants')
logEventTypes = {}
for logEventType in constants['logEventTypes']:
    logEventTypeId = constants['logEventTypes'][logEventType]
    logEventTypes[logEventTypeId] = logEventType
logSourceTypes = {}
for logSourceType in constants['logSourceType']:
    logSourceTypeId = constants['logSourceType'][logSourceType]
    logSourceTypes[logSourceTypeId] = logSourceType

# PARSE
table = []
for event in d['events']:
    params = event.get('params')
    source = event.get('source')

    if params is not None:
        method = params.get('method')
        url = params.get('url')

    if source is not None and url is not None:
        sourceId = source.get('id')
        sourceType = source.get('type')

        eventType = event.get('type')

        row = (method,url,sourceId,logSourceTypes[sourceType],logEventTypes[eventType])
        table.append(row)

# EXPORT
dt = datetime.now()
dts = dt.strftime("%Y%m%d%H%M%S")
with open(f"./output/{dts}.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['METHOD','URL','SOURCE_ID','SOURCE_TYPE','EVENT_TYPE'])
    writer.writerows(table)
