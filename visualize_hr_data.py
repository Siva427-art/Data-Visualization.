import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('hr_employee_data.csv')

# Set style
sns.set(style="whitegrid")

# Salary distribution by department
plt.figure(figsize=(8,5))
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title('Salary Distribution by Department')
plt.savefig('salary_by_department.png')
plt.close()

# Performance vs. Experience
plt.figure(figsize=(8,5))
sns.scatterplot(x='YearsExperience', y='PerformanceScore', hue='Department', data=df, s=100)
plt.title('Performance vs. Experience by Department')
plt.savefig('performance_vs_experience.png')
plt.close()

# Average salary per department
plt.figure(figsize=(8,5))
sns.barplot(x='Department', y='Salary', data=df, estimator=sum, ci=None, palette='Set1')
plt.title('Total Salary by Department')
plt.savefig('total_salary_by_department.png')
plt.close()

print('Visualizations created! Check the PNG files.')
