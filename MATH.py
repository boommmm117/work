import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('m4a1.xlsx', header=None)
df.columns = ['DATA']
values= df['DATA']
# ===STATISTICS===

print('==Value DATA==')
print(f'{values}','\n')
print('==STATISTICS==')

stats = [
    ("Max", values.max()),
    ("Min", values.min()),
    ("Sum", values.sum()),
    ("Mean", values.mean()),
    ("Median", values.median()),
    ("Standard Deviation", values.std()),
    ("Variance", values.var()),
    ("Q1", values.quantile(0.25)),
    ("Q2", values.quantile(0.50)),
    ("Q3", values.quantile(0.75))
]

for i,(name,value) in enumerate(stats):
    print(f"{i+1}.{name} = {value}")

# ===graph===

plt.bar(range(len(values)), values)
plt.title("Bar Chart of DATA")
plt.xlabel("Index")
plt.ylabel("Value")
plt.xticks(range(len(values)))
plt.grid(axis='y', linestyle='--')
plt.show()

plt.plot(values,marker='o')
plt.title('Line plot of DATA')
plt.xlabel('index')
plt.ylabel('DATA')
plt.grid(axis='y', linestyle='--')
plt.grid(axis='x', linestyle='--')
plt.show()
