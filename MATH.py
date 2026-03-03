import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('DATA1.xlsx', header=None)
df.columns = ['DATA']

data = df['DATA']
# ===STATISTICS===

print('==Value DATA==')
print(f'{data}','\n')
print('==STATISTICS==')

stats = [
    ("Max", data.max()),
    ("Min", data.min()),
    ("Sum", data.sum()),
    ("Mean", data.mean()),
    ("Median", data.median()),
    ("Standard Deviation", data.std()),
    ("Variance", data.var()),
    ("Q1", data.quantile(0.25)),
    ("Q2", data.quantile(0.50)),
    ("Q3", data.quantile(0.75))
]

for i,(name,value) in enumerate(stats):
    print(f"{i+1}.{name} = {value}")

# ===graph===

plt.bar(range(len(data)), data)
plt.title("Bar Chart of DATA")
plt.xlabel("Index")
plt.ylabel("Value")
plt.xticks(range(len(data)))
plt.grid(axis='y', linestyle='--')
plt.show()

plt.plot(data,marker='o')
plt.title('Line plot of DATA')
plt.xlabel('index')
plt.ylabel('DATA')
plt.grid(axis='y', linestyle='--')
plt.grid(axis='x', linestyle='--')
plt.show()
