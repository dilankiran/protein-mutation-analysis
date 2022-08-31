import numpy as np
proximal_diff= np.array([-3
,-2
,-3
,-1
,16
,23
,6
,38
,-21
,-16
,-1
,-2
,1
,1
,1
,-15
,-4
,22
,6
,2
,7
,0
,16
,11
,-26
,-36
,-36
,6
,9
,1
,-43
,-29
,-44
,-28
,-40
,-37
,0
,-8
,0
,1
,0
,-43
,0
,-1
,2
,-3
,-5
,5
,-3
,-2
,-1
,3
,-3
,-3
,17
,10
,-3
,3
,18
,-29
,-16
,0
,0
,-40
,-8
,-2
,0
,43
,-1
,3
,6
,-1
,6
,0
,3
,7
,10
,0
,14
,-8
,-5
,-8
,-39])

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

import matplotlib.pyplot as plt

plt.scatter(proximal_diff,ddg_exp)
m, b = np.polyfit(proximal_diff,ddg_exp, 1)
plt.plot(proximal_diff, m*proximal_diff, color='red')
plt.xlabel("of which proximal differences between the wt and mut")
plt.ylabel("experimental ddg values")
plt.show()

correlation_matrix = np. corrcoef(proximal_diff,ddg_exp)
correlation_proximalbdiffdgg = correlation_matrix[0,1]
r_squared = correlation_proximalbdiffdgg **2.
print(r_squared)

from scipy import stats
p_prox =stats.ttest_ind(proximal_diff,ddg_exp)
print(p_prox)

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(proximal_diff, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
    
plt.title('of which proximal differences between the wt and mut')

plt.show(bp)

#%% 

most_dept= sorted(i for i in ddg_exp if i<0)

diff_dept= np.array([-3
,-2
,-3
,-1
,16
,23
,6
,38
,-21
,-16
,-1
,-2
,1
,1
,1
,-15
,-4
,22
,6
,2
,7
,0
,16
,11
,-26
,-36
,-36
,6])

plt.scatter(diff_dept,most_dept)
m, b = np.polyfit(diff_dept,most_dept,1)
plt.plot(diff_dept, m*diff_dept+b, color='blue')
plt.title("most depleted")
plt.xlabel("differences between the wt and mut")
plt.ylabel("experimental ddg values")
plt.show()

correlation_matrix = np. corrcoef(diff_dept,most_dept)
correlation_diffdggmostdept= correlation_matrix[0,1]
r_squared_mostdept = correlation_diffdggmostdept**2.
print(r_squared_mostdept)

most_enr= sorted(i for i in ddg_exp if i>0)
diff_enr= np.array([9
,1
,-43
,-29
,-44
,-28
,-40
,-37
,0
,-8
,0
,1
,0
,-43
,0
,-1
,2
,-3
,-5
,5
,-3
,-2
,-1
,3
,-3
,-3
,17
,10
,-3
,3
,18
,-29
,-16
,0
,0
,-40
,-8
,-2
,0
,43
,-1
,3
,6
,-1
,6
,0
,3
,7
,10
,0
,14
,-8
,-5
,-8
,-39])

plt.scatter(diff_enr,most_enr)
m, b = np.polyfit(diff_enr,most_enr,1)
plt.plot(diff_enr, m*diff_enr+b, color='green')
plt.title("most enriched")
plt.xlabel("differences between the wt and mut")
plt.ylabel("experimental ddg values")
plt.show()

correlation_matrix = np. corrcoef(diff_enr,most_enr)
correlation_diffdggmostenr= correlation_matrix[0,1]
r_squared_mostenr = correlation_diffdggmostenr**2.
print(r_squared_mostenr)

from scipy import stats
      
p_dept =stats.ttest_ind(diff_dept,most_dept)
print(p_dept)

p_enr =stats.ttest_ind(diff_enr,most_enr)
print(p_enr)

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(diff_enr, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
    
plt.title('most enriched')

plt.show(bp)

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(diff_dept, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
    
plt.title('most depleted')

plt.show(bp)
