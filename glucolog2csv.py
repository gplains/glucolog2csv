import pandas as pd
import datetime as dt
import pprint
import sys
pd.set_option('display.max_rows', None)

args=sys.argv
df = pd.read_csv(args[1] ,header=None, names=['scandatetime','count1','count2','comment1','comment2'])
df['scandatetime'] = pd.to_datetime(df['scandatetime'], format='%Y-%m-%d %H:%M:%S')
df['scandate'] = df['scandatetime'].dt.date
df['scantime'] = df['scandatetime'].dt.time

INS={}

for row in df.values:
    date = row[0].strftime("%Y-%m-%d")
    time = row[0].strftime("%H:%M")
    if row[1] in [0,1,2,3,4]:
       p_record ={row[1]:{'time':time,'value':row[2]} }
    else :
        ihour=row[0].hour
        itime = row[0].strftime("%H:%M")
        if ihour>=5 and ihour <9 :
           ihour='c_1'
        elif ihour>=11 and ihour <14 :
           ihour='c_2'
        elif ihour>=17 and ihour <20 :
           ihour='c_3'
        elif ihour>=20 :
           ihour='c_4'
        p_record={ihour:{'time':itime,'value':row[1]} }
    if INS.get(date)==None :
       INS[date] =p_record
    else :
       INS[date] |=p_record

for row in df.values:
    date = row[0].strftime("%Y-%m-%d")

for key in INS :
  c_1 = 0 if INS[key].get('c_1')==None else INS[key]['c_1']['value']
  c_2 = 0 if INS[key].get('c_2')==None else INS[key]['c_2']['value']
  c_3 = 0 if INS[key].get('c_3')==None else INS[key]['c_3']['value']
  c_4 = 0 if INS[key].get('c_4')==None else INS[key]['c_4']['value']
  I_0 = 0 if INS[key].get(0)==None else INS[key][0]['value']
  I_1 = 0 if INS[key].get(1)==None else INS[key][1]['value']
  I_2 = 0 if INS[key].get(2)==None else INS[key][2]['value']
  I_3 = 0 if INS[key].get(3)==None else INS[key][3]['value']
  I_4 = 0 if INS[key].get(4)==None else INS[key][4]['value']
  print (key,int(c_1),int(c_2),int(c_3),int(c_4), int(I_0),int(I_1),int(I_2),int(I_4),sep=',')
