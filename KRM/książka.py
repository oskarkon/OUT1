import pandas as pd
import numpy as np
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame

frame2=pd.DataFrame(data, columns=['year','state','pop','debt'],
                   index=['one','two','three','four','five','six']
                   )
data=[1,2,-4]
x=pd.Series( data)

val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
