import pandas as pd
def read_data ():
    csv1 = '/Users/mac/Downloads/order_region_a(in).csv'
    csv2 = '/Users/mac/Downloads/order_region_b(in).csv'

    dfa = pd.read_csv(csv1)
    dfb = pd.read_csv(csv2)
    return (dfa,dfb)
