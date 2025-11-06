import pandas as pd
import ast
import json
from sqlalchemy import create_engine
def read_data (file1,file2):
    csv1 = file1
    csv2 = file2

    dfa = pd.read_csv(csv1)
    dfb = pd.read_csv(csv2)
    print("Data has been fetch successfully")
    process(dfa,dfb)
def process(dfa,dfb):
    print("Data is processing.....")
    dfa["region"] = 'A'
    dfb["region"] = 'B'
    combo = pd.concat([dfa, dfb], ignore_index=True)
    combo["total_sales"] = combo["QuantityOrdered"] * combo["ItemPrice"]
    combo = combo.drop_duplicates(subset="OrderId", keep="first")
    combo["PromotionDiscount"] = combo["PromotionDiscount"].apply(ast.literal_eval)
    combo["net_sale"] = combo["total_sales"] - combo["PromotionDiscount"].apply(lambda x: float(x["Amount"]))
    combo = combo[combo["net_sale"] > 0]
    combo["PromotionDiscount"] = combo["PromotionDiscount"].apply(json.dumps)
    combo.reset_index(drop=True, inplace=True)
    print("data has been processed successfully")
    add_data_to_sql(combo)

def add_data_to_sql(combo):
    engine = create_engine("sqlite:///sales_data.db")
    combo.to_sql("sales_table", engine, if_exists="replace", index=False)
    print("data has added to database")