import pandas as pd
import time
import datetime

inf = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data.csv"
df = pd.read_csv(inf)

end = time.time()
end_str = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')

def getDate(end_str):
    try:
        year_str = end_str[:10]
    except AttributeError:
        year_str = 'broke'
    return year_str

def writeDS():
    today = getDate(end_str)
    out_f = "/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/pulled_data/" + today + ".csv"
    open(out_f,"w+")
    return df.to_csv(out_f, encoding='utf-8', index=False)

try:
    writeDS()
except:
    print "could not write"