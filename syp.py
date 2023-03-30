import pandas as pd
import yfinance as yf
import numpy as np
from suport_streamli import * 
from dataset_conect import sypActual
start_date = "2000-01-01"
end_date = "2023-01-27"


syp = yf.download('^GSPC', start=start_date)

syp=syp.round(3)

anual_syp= syp.groupby(syp.index.year).agg({'Open':'mean','High':'max','Low':'min','Close':'mean','Volume':'mean'}).round()
anual_syp

def ratio_month(anio,data):
    radio=data[data.index.year== anio]
    month=radio.groupby(radio.index.month).mean().round(3)
    return month

def creci_porcentaje(data):
    try:
        f=data['Close'].pct_change()*100
        cre = f.mean().round(2)
        return cre, f
    except AttributeError:
        return 0,0
    
def value_extreme(data,select):
    if select == 'Open':
        data = syp.groupby(syp.index.year).max()
    elif select == 'Low':
        data= syp.groupby(syp.index.year).min()
    return data

def top_ten(select):
    if select == 'mean_total':
        top=close_anual.sort_values('mean_total',ascending=False).index[:10]
    else:
        top=close_anual.sort_values('growth',ascending=False).index[:10]
    return top


def month_sector(select,anio):
    
    x=cierre[select]
    anio=x[x.index.year==anio]
    month= anio.groupby(anio.index.month).mean().round()
    return month