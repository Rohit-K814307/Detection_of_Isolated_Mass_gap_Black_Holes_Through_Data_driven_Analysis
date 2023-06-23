from data_prepare import *

#generate GAN data
eda_data = generate_CTGan()


print(f"Data Shape: {eda_data.shape}")
print(f"Null Counts: {eda_data.isna().sum().sum()}")
print(f"Value counts: {eda_data['target'].value_counts()}")
print(f"Skew:\n{eda_data.skew()}\n\nKurtosis:\n{eda_data.kurtosis()}")

rcParams['figure.figsize'] = 2,2
for col in list(eda_data.columns):
    plt.figure()
    print(sns.kdeplot(eda_data[col],bw_method=0.5))



