import pandas as pd
import time
import datetime
from dateutil import parser

df = pd.read_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/raw.csv')

df = df.replace({r' - ': '', r'(\[)': '', r']': ''}, regex=True)

def dateStd(df):
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    two_day = datetime.timedelta(days=2)
    three_day = datetime.timedelta(days=3)
    four_day = datetime.timedelta(days=4)
    five_day = datetime.timedelta(days=5)
    six_day = datetime.timedelta(days=6)
    seven_day = datetime.timedelta(days=7)
    eight_day = datetime.timedelta(days=8)
    nine_day = datetime.timedelta(days=9)
    ten_day = datetime.timedelta(days=10)
    eleven_day = datetime.timedelta(days=11)
    twelve_day = datetime.timedelta(days=12)
    thirteen_day = datetime.timedelta(days=13)
    fourteen_day = datetime.timedelta(days=14)
    fifteen_day = datetime.timedelta(days=15)
    sixteen_day = datetime.timedelta(days=16)
    seventeen_day = datetime.timedelta(days=17)
    eighteen_day = datetime.timedelta(days=18)
    nineteen_day = datetime.timedelta(days=19)
    twenty_day = datetime.timedelta(days=20)
    twentyone_day = datetime.timedelta(days=21)
    twentytwo_day = datetime.timedelta(days=22)
    twentythree_day = datetime.timedelta(days=23)
    twentyfour_day = datetime.timedelta(days=24)
    twentyfive_day = datetime.timedelta(days=25)
    twentysix_day = datetime.timedelta(days=26)
    twentyseven_day = datetime.timedelta(days=27)
    twentyeight_day = datetime.timedelta(days=28)
    twentynine_day = datetime.timedelta(days=29)
    thirty_day = datetime.timedelta(days=30)
    thirtyone_day = datetime.timedelta(days=31)

    day1 = today - one_day
    day2 = today - two_day
    day3 = today - three_day
    day4 = today - four_day
    day5 = today - five_day
    day6 = today - six_day
    day7 = today - seven_day
    day8 = today - eight_day
    day9 = today - nine_day
    day10 = today - ten_day
    day11 = today - eleven_day
    day12 = today - twelve_day
    day13 = today - thirteen_day
    day14 = today - fourteen_day
    day15 = today - fifteen_day
    day16 = today - sixteen_day
    day17 = today - seventeen_day
    day18 = today - eighteen_day
    day19 = today - nineteen_day
    day20 = today - twenty_day
    day21 = today - twentyone_day
    day22 = today - twentytwo_day
    day23 = today - twentythree_day
    day24 = today - twentyfour_day
    day25 = today - twentyfive_day
    day26 = today - twentysix_day
    day27 = today - twentyseven_day
    day28 = today - twentyeight_day
    day29 = today - twentynine_day
    day30 = today - thirty_day
    day31 = today - thirtyone_day

    df = df.replace({'null' : day31,
                     'Today' : today,
                     'today' : today,
                     'Just posted' : today,
                     'Posted today' : today,
                     '1 day ago': day1,
                     '2 days ago': day2,
                     '3 days ago': day3,
                     '4 days ago': day4,
                     '5 days ago': day5,
                     '6 days ago': day6,
                     '7 days ago': day7,
                     '8 days ago': day8,
                     '9 days ago': day9,
                     '10 days ago': day10,
                     '11 days ago': day11,
                     '12 days ago': day12,
                     '13 days ago': day13,
                     '14 days ago': day14,
                     '15 days ago': day15,
                     '16 days ago': day16,
                     '17 days ago': day17,
                     '18 days ago': day18,
                     '19 days ago': day19,
                     '20 days ago': day20,
                     '21 days ago': day21,
                     '22 days ago': day22,
                     '23 days ago': day23,
                     '24 days ago': day24,
                     '25 days ago': day25,
                     '26 days ago': day26,
                     '27 days ago': day27,
                     '28 days ago': day28,
                     '29 days ago': day29,
                     '30 days ago': day30,
                     '30+ days ago': day30,
                     '+30 days ago': day30,
                     '1 hour ago' : today,
                     '10 hours ago' : today,
                     '11 hours ago' : today,
                     '12 hours ago' : today,
                     '2 hours ago' : today,
                     '3 hours ago' : today,
                     '4 hours ago' : today,
                     '5 hours ago' : today,
                     '6 hours ago' : today,
                     '7 hours ago' : today,
                     '8 hours ago' : today,
                     '9 hours ago' : today,
                     '1 week ago': day7,
                     '2 weeks ago': day14,
                     '3 weeks ago': day21,
                     '4 weeks ago': day28,
                     '1 month ago': day30,
                     'ADVERTISEMENT': day31,
                     })
    return df

df = dateStd(df)

df['job_posted'] = pd.to_datetime(df['job_posted'], yearfirst=True, errors='coerce', infer_datetime_format=True)

df = df.replace({r'(AM)$': r' '}, regex=True)



def remove_dup():
    df_fin = df.drop_duplicates()
    return df_fin


with pd.ExcelWriter('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data1.xlsx') as writer:
    remove_dup().to_excel(writer, sheet_name='Raw Data')
    writer.save()

df1 = pd.read_excel('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data1.xlsx')
df1.to_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data1.csv', encoding='utf-8')


df.to_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data.csv', encoding='utf-8')
print df
end = time.time()
print "end = ", datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
