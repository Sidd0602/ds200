import pandas as pd
import matplotlib.pyplot as plt
import sys
df = pd.read_csv(sys.argv[1])
df1= df.iloc[:,[2,3,4,5]]
plotMap=[]

plotMap.append(df['JAN-FEB'].dropna().tolist())
plotMap.append(df['MAR-MAY'].dropna().tolist())
plotMap.append(df['JUN-SEP'].dropna().tolist())
plotMap.append(df['OCT-DEC'].dropna().tolist())
plt.boxplot(plotMap)
plt.xlabel('Seasons')
plt.ylabel('Temperature(Celsius)')
plt.xticks([1,2,3,4],["JAN-FEB","MAR-MAY","JUN-SEP","OCT-DEC"])
plt.title('Mean temperature in India between 1901-2012')
plt.show()
