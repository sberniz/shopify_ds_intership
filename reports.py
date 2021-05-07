import pandas as pd
FILE_URL = "2019 Winter Data Science Intern Challenge Data Set.csv"
df = pd.read_csv(FILE_URL)

def reports(df):
  df_modified_fixd = df.copy()
  df_modified_fixd['price_per_shoe'] = df['order_amount'] / df['total_items']
  df_modified_fixd = df_modified_fixd[(df_modified_fixd['price_per_shoe'] < 25725.0) & (df_modified_fixd['total_items'] < 2000)]
  return  {'original_mean': df['order_amount'].mean(),
                    'original_mode': df['order_amount'].mode()[0],
                    'revised_mean':df_modified_fixd['order_amount'].mean(),
                    'revised_mode':df_modified_fixd['order_amount'].mode()[0]}

df_report = reports(df)
# nice Print 
for k,v in df_report.items():
  print(f"{k} : ${round(v,2)}")