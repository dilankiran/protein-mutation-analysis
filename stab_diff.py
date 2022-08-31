import numpy as np 
ddg_exp= np.array([6.77
,6.55
,06.03
,6.85
,-3.86
,-5.04
,-4.17
,-5.68
,5.42
,6.82
,7.66
,6.67
,-4.42
,-4.1
,-3.16
,5.92
,8.81
,6.61
,07.08
,7.51
,6.38
,06.06
,7.44
,6.54
,6.33
,6.33
,5.29
,5.45
,7.29
,7.58
,5.4
,5.54
,6.31
,5.44
,6.56
,5.4
,-5.59
,-5.9
,-3.35
,-4.93
,-3.75
,5.95
,7.95
,11.4
,9.27
,9.32
,12.2
,8.69
,11.1
,8.77
,7.61
,6.95
,7.64
,10.5
,8.57
,6.78
,11.6
,-3.53
,-5.92
,-3.32
,-3.14
,5.9
,5.44
,5.47
,5.4
,6.2
,-8.33
,-3.88
,-3.4
,-11.4
,-9.32
,-6.95
,-12.2
,-8.69
,-7.61
,-9.27
,-10.5
,-8.57
,7.58
,5.59
,8.33
,5.51
,6.19])

stab_diff= np.array([1.07
,1.02
,2.02
,0.76
,-0.38
,-0.32
,-0.43
,0.05
,0.82
,0.54
,-1.79
,0.79
,0.06
,-1.3
,-0.9
,0.03
,-0.54
,-0.05
,0.02
,0.78
,1.82
,0.74
,1.18
,0.79
,0.49
,0.66
,0.44
,-0.96
,-0.1
,0.73
,0.78
,0.54
,0.51
,0.47
,0.22
,0.32
,-1.34
,-1.21
,-1.12
,-2
,0.02
,1.06
,-0.28
,0.13
,-0.29
,-0.13
,0.87
,0.69
,-1.27
,-1.16
,-0.45
,0.18
,0.13
,-0.28
,0.19
,-0.3
,-0.89
,-0.95
,-0.67
,-0.18
,-1.01
,-0.32
,-0.25
,0.23
,-0.41
,0.21
,-0.74
,-0.6
,-1.35
,-0.62
,-0.43
,-0.9
,-1.42
,-1.24
,-0.24
,-0.67
,-0.32
,-1.69
,-0.24
,1.27
,0.77
,1.33
,0.26])

import matplotlib.pyplot as plt

plt.scatter(stab_diff,ddg_exp)
m, b = np.polyfit(stab_diff,ddg_exp, 1)
plt.plot(stab_diff, m*stab_diff+b, color='red')
plt.xlabel("stability differences between the wt and mut")
plt.ylabel("experimental ddg values")
plt.show()

correlation_matrix = np. corrcoef(stab_diff,ddg_exp)
correlation_stabdiffdgg = correlation_matrix[0,1]
r_squared = correlation_stabdiffdgg **2.
print(r_squared)

#%%
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(stab_diff, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
    
plt.title('stability differences between the wt and mutant')

plt.show(bp)

from scipy import stats
p_stab =stats.ttest_ind(stab_diff,ddg_exp)
print(p_stab)
