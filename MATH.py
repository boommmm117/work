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
    ("ค่าสูงสุด", values.max()),
    ("ค่าต่ำสุด", values.min()),
    ("ผลรวม", values.sum()),
    ("ค่าเฉลี่ย", values.mean()),
    ("ค่ามัธยฐาน", values.median()),
    ("ส่วนเบี่ยงเบนมาตรฐาน", values.std()),
    ("ความแปรปรวน", values.var()),
    ("ควอไทล์ที่ 1 (Q1)", values.quantile(0.25)),
    ("ควอไทล์ที่ 2 (Q2)", values.quantile(0.50)),
    ("ควอไทล์ที่ 3 (Q3)", values.quantile(0.75))
]

for i,(name,value) in enumerate(stats):
    print(f"{i+1}. {name} = {value}")
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
