import numpy as np
import pandas as pd

# myDict = dict ( one =1 , two =2 , info = ' some information ')
# myDict2 = { ' ten ':1 , ' twenty ' :20 ,
# ' info ': ' more information '}
# print ( myDict [ 'info' ])
# print ( myDict . keys ())

df = pd.read_csv( 'data.txt' , engine = 'python', skipfooter = 3 , delimiter = '[ ,]*')
print(df.values)