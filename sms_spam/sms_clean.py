import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("SMSSpamCollection", sep="\t", header=None, names=["etiket", "mesaj"])

print(f"Toplam satır: {df.shape[0]}")
print("İlk 5 satır:")
print(df.head())

print("\nEksik değerler:")
print(df.isnull().sum())

print("\nYinelenen satır sayısı:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nSınıf dağılımı:")
print(df['etiket'].value_counts())

sns.countplot(data=df, x="etiket")
plt.title("Sınıf Dağılımı")
plt.savefig("sinif_dagilimi.png")
plt.show()

df.to_csv("sms_clean.csv", index=False)
