from scipy import stats

rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print (stats.ttest_1samp(rvs,5.0))

print("*******************")
print("Comparing two samples")
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 8,scale = 10,size = 500)
print (stats.ttest_ind(rvs1,rvs2))