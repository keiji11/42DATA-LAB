import pandas as pd

df_salaries = pd.read_csv('./datasets/Salaries.csv')
df_titles = pd.read_csv('./datasets/titles.csv')

# 1. Check the head of the datasets
salary_head = df_salaries.head()
# print(salary_head)

# 2. Use the `.info()` method to find out how many entries there are
# df_salaries.info(verbose=False, show_counts=False)

# 3. Check the highest amount of OvertimePay in the dataset
max_OvertimePay = df_salaries['OvertimePay'].max()
# print(max_OvertimePay)

# 4. What is the job title of JOSEPH DRISCOLL?
JD = df_salaries[df_salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
# print(JD)

# 5. How much does JOSEPH DRISCOLL make (including benefits)?
JD_salary = df_salaries[df_salaries['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
# print(JD_salary)

# 6. What is the name of highest paid person (including benefits)?
df_salaries2 = pd.read_csv('./datasets/Salaries.csv', usecols=['EmployeeName', 'TotalPayBenefits'])
max_paid = df_salaries[df_salaries2['TotalPayBenefits'] == df_salaries2['TotalPayBenefits'].max()]['EmployeeName']
# print(max_paid)

# 7. What is the name of lowest paid person (including benefits)?
min_paid = df_salaries[df_salaries2['TotalPayBenefits'] == df_salaries2['TotalPayBenefits'].min()]['EmployeeName']
# print(min_paid)

# 8. What was the average (mean) BasePay of all the employees per year? (2011-2014)
df_salaries3 = pd.read_csv('./datasets/Salaries.csv', usecols=['BasePay'])
mean_base_pay = df_salaries3['BasePay'].mean()
# print('{:.2f}'.format(mean_base_pay))

# 9. How many unique job titles are there?
df_salaries4 = pd.read_csv('./datasets/Salaries.csv', usecols=['JobTitle'])
unique_job_titles = df_salaries4['JobTitle'].nunique()
# print(unique_job_titles)

# 10. What are the top 5 most common jobs?
top_5_jobs = df_salaries4['JobTitle'].value_counts().head(5)
# print(top_5_jobs)

# 11. How many Job Titles were represented by only one person in 2013?(Job Titles with only one occurence in 2013?)
df_salaries5 = pd.read_csv('./datasets/Salaries.csv', usecols=['JobTitle', 'Year'])
df_salaries5['JobTitle'] = df_salaries5['JobTitle'].str.lower()
df_salaries_2013 = df_salaries5[df_salaries5['Year'] == 2013]
df_salaries5_counts = df_salaries_2013['JobTitle'].value_counts()
unique_job_titles_represented = df_salaries5_counts[df_salaries5_counts == 1]
# print(len(unique_job_titles_represented))

# 12. How many people have the word Chief in their job title?
df_salaries4_12 = df_salaries4['JobTitle'].str.lower()
sal_list = list(df_salaries4_12.values)
count_chief = 0
for i in sal_list:
  if 'chief' in i:
      count_chief += 1
print(count_chief)