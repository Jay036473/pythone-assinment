1

import pandas as pd

df = pd.read_csv('/content/Cardiovascular dataset.csv', sep=';')
display(df)

2'''What is the shape of the dataset?'''

display(df.shape)

3'''Are there any missing values in the dataset?'''

display(df.isnull().sum())

4'''What’s the average age of patients (in years)?'''

df['age_years'] = df['age'] / 365.25
average_age_years = df['age_years'].mean()
print(f"The average age of patients is: {average_age_years:.2f} years")

5'''What is the distribution of the target variable (cardio)?'''

display(df['cardio'].value_counts())

6'''What is the average age (in years) of patients?'''

print(f"The average age of patients is: {average_age_years:.2f} years")

7'''What is the distribution of BMI? (Create new BMI feature)'''

df['bmi'] = df['weight'] / (df['height'] / 100)**2
display(df['bmi'].describe())

8'''Are there outliers in height or weight?'''

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.boxplot(ax=axes[0], y=df['height'])
axes[0].set_title('Box Plot of Height')
axes[0].set_ylabel('Height (cm)')

sns.boxplot(ax=axes[1], y=df['weight'])
axes[1].set_title('Box Plot of Weight')
axes[1].set_ylabel('Weight (kg)')

plt.tight_layout()
plt.show()

9'''Are there implausible blood pressure values (e.g., ap_hi < ap_lo or too high)?'''

implausible_bp = df[df['ap_lo'] > df['ap_hi']]
print("Number of cases with ap_lo > ap_hi:", len(implausible_bp))
display(implausible_bp.head())

10'''. How many rows have incorrect blood pressure values? Column Condition Reason ap_hi between 80 and 250 realistic systolic ap_lo between 50 and 200 realistic diastolic ap_hi >= ap_lo systolic must be ≥ diastolic logical'''

incorrect_bp_rows = df[
    (df['ap_hi'] < 80) | (df['ap_hi'] > 250) |
    (df['ap_lo'] < 50) | (df['ap_lo'] > 200) |
    (df['ap_hi'] < df['ap_lo'])
]

print("Number of rows with incorrect blood pressure values:", len(incorrect_bp_rows))

11'''Remove rows with invalid blood pressure, height, or weight? Height between 120cm to 220cm Weight between 40 to 200kg'''

df_filtered = df[
    (df['ap_hi'] >= 80) & (df['ap_hi'] <= 250) &
    (df['ap_lo'] >= 50) & (df['ap_lo'] <= 200) &
    (df['ap_hi'] >= df['ap_lo']) &
    (df['height'] >= 120) & (df['height'] <= 220) &
    (df['weight'] >= 40) & (df['weight'] <= 200)
]

print("Number of rows before filtering:", len(df))
print("Number of rows after filtering:", len(df_filtered))

12'''What is the distribution of cholesterol and glucose levels after cleaning?'''

print("Distribution of Cholesterol Levels:")
display(df_filtered['cholesterol'].value_counts())

print("\nDistribution of Glucose Levels:")
display(df_filtered['gluc'].value_counts())

13'''How many smokers have cardiovascular disease?'''

smokers_with_cardio = df_filtered[(df_filtered['smoke'] == 1) & (df_filtered['cardio'] == 1)]
print("Number of smokers with cardiovascular disease:", len(smokers_with_cardio))

14'''Does alcohol intake correlate with higher cardio risk?'''

cardio_by_alcohol = df_filtered.groupby('alco')['cardio'].mean()
print("Proportion of individuals with cardiovascular disease by alcohol intake:")
display(cardio_by_alcohol)

15'''What’s the correlation between features?'''

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
sns.heatmap(df_filtered.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix of Features')
plt.show()

16'''Compare mean BMI for cardio vs. non-cardio'''

mean_bmi_by_cardio = df_filtered.groupby('cardio')['bmi'].mean()
print("Mean BMI for cardio vs. non-cardio:")
display(mean_bmi_by_cardio)

17'''Plot age distribution for those with and without cardio disease'''

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(data=df_filtered, x='age_years', hue='cardio', kde=True, bins=30)
plt.title('Age Distribution for Cardio vs. Non-Cardio')
plt.xlabel('Age (years)')
plt.ylabel('Frequency')
plt.show()

18'''Boxplot of systolic blood pressure by cardio status'''

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(data=df_filtered, x='cardio', y='ap_hi')
plt.title('Systolic Blood Pressure by Cardio Status')
plt.xlabel('Cardiovascular Disease (0: No, 1: Yes)')
plt.ylabel('Systolic Blood Pressure (ap_hi)')
plt.show()

19'''What percentage of patients have above-normal glucose levels?'''

above_normal_glucose_count = df_filtered[df_filtered['gluc'] > 1].shape[0]
total_patients_filtered = df_filtered.shape[0]
percentage_above_normal_glucose = (above_normal_glucose_count / total_patients_filtered) * 100

print(f"Percentage of patients with above-normal glucose levels: {percentage_above_normal_glucose:.2f}%")