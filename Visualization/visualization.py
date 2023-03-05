from methods import preProcess_methods
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
from sklearn.decomposition import PCA

getFeatures, getLabels, getViewData = preProcess_methods()
dfTotal, X_res, y_res = getViewData()


#Distribution plot
from matplotlib import rcParams
rcParams['figure.figsize'] = 2,2
for col in list(dfTotal.columns):
    plt.figure()
    sns.kdeplot(dfTotal[col],bw_method=0.5)


#PCA full data plot
pca = PCA(n_components=1)
Xcop = X_res.copy()
Xcop = pca.fit_transform(Xcop)
fig = plt.figure()
ax = fig.add_subplot()
for i in range(1000):
    ax.scatter(Xcop[i][0], y_res[i])
ax.set_xlabel('Principle Component 1')
ax.set_ylabel('ID')
plt.show()

