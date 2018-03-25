import time
import datetime
import pandas as pd
from ghphillips_search import GhPhillips
from lowes_search import Lowes
from craigs_list_search import CraigsList
from indeed_search import Indeed
from connect_colorado_search import ConnectColorado
from build_colorado_search import BuildColorado
from monster_search import Monster
from career_builder_search import CareerBuilder
start = time.time()

print "start = ", datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

GhphillipsPull = GhPhillips()
LowesPull = Lowes()
CraigsListPull = CraigsList()
IndeedPull = Indeed()
ConnectColoradoPull = ConnectColorado()
BuildColoradoPull = BuildColorado()
MonsterPull = Monster()
CareerBuilderPull = CareerBuilder()

cb = CareerBuilderPull.df
bc = BuildColoradoPull.df
gh = GhphillipsPull.df
l = LowesPull.df
cl = CraigsListPull.df
i = IndeedPull.df
m = MonsterPull.df

pd.set_option('max_colwidth', 500)
df = pd.DataFrame()
df_set = [cb, bc, gh, l, cl, i, m]

df = ConnectColoradoPull.df.append(df_set,ignore_index=True)
print df
df = df.to_csv('/Users/tylehman/Desktop/last_leg.csv', encoding='utf-8', index=False)