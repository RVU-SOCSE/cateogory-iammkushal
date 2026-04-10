import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C:/Users/RVUW241/Downloads/laptops.csv.csv')

print(df.columns)
plt.bar(df['experience_level'], df['salary_in_usd'],
        edgecolor='black', linewidth=0.5)

plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.title("Experience vs Salary (Matplotlib)")
plt.show()

sns.barplot(x=df['experience_level'], y=df['salary_in_usd'])

plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.title("Experience vs Salary (Seaborn)")
plt.show()
