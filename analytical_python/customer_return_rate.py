import pandas as pd

def convert_dtype(x):
    if not x:
        return ''
    try:
        return str(x)
    except:
        return ''


df = pd.read_csv('user_log.csv', converters={'First_purchase_cohort': convert_dtype, 'event_type': convert_dtype}, sep=',')
df = df[['uid', 'date', 'First_purchase_cohort', 'Week_date', 'event_type']]

df_pivot_table = df.pivot_table(index=['Week_date', 'First_purchase_cohort', 'event_type'],
                                values=['uid'],
                                aggfunc=['nunique'],)

print(df_pivot_table.query("event_type == 'purchase' and Week_date != 19"))
