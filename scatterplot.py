import pandas as pd
import matplotlib.pyplot as plt
import sys
df = pd.read_csv(sys.argv[1])
df1 = df.iloc[:,[2,3]]
plt.scatter(df['Per Capita GDP in US $'],df['Per Capita R&D in US $'],marker='x', color='#dd1255',label="GDP vs R&D Expenditure")
plt.xlabel("Per capita GDP($)")
plt.ylabel("Per capita expenditure on R&D($)")
plt.title('Comparison between per capita GDP and per capita R&D expenditure of different countries')
plt.legend('C_name')
plt.show()
