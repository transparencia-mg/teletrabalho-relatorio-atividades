from bs4 import BeautifulSoup
from pandas import read_html
import pandas as pd
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("servidor", help="nome do servidor na pasta data/")
args = parser.parse_args()

who = args.servidor

df = pd.DataFrame()

for dirname, dirnames, filenames in os.walk(f'data/{who}'):
    for filename in filenames:
        if filename != '.gitkeep':
          path = os.path.join(dirname, filename)
          lst = read_html(path, encoding='utf-8')[0]
          tmp = pd.DataFrame(lst).dropna(how='all')
          tmp['SERVIDOR'] = who
          tmp['MES'] = re.search('\d{4}-\d{2}', path).group(0)
          tmp['ATIVIDADE'] = ''
          tmp['PROJETO'] = ''
          tmp['ROTINA'] = ''
          df = pd.concat([df, tmp])


df.to_excel(f'{who}.xlsx', index=False)
