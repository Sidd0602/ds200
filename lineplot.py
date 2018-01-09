import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(sys.argv[1], index_col='Year')
plotdata = df['All Minerals - Value']
plt.plot(plotdata, label='Mining data from 2000-16', marker='s')
plt.xlabel('Year')
plt.ylabel('Production-value')
plt.title('Minerals produced from 2000-2016')
plt.show()
