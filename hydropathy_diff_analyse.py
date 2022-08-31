
import numpy as np
diff=np.array([-7.3
,-7.3
,-4.2
,-5.4
,-5.7
,-5.7
,-5.3
,-5
,1
,2.8
,7
,-5.4
,-0.7
,4.6
,4.5
,5.3
,-3.6
,2.9
,-8.3
,-7.3
,-7
,-5.4
,-4.7
,-5.1
,-2.2
,-2.2
,-0.3
,-6.3
,2.9
,-5.4
,3.1
,-2.2
,0.9
,-2.6
,-0.3
,0.6
,7.3
,7.3
,7.3
,4.2
,0.9
,3.1
,0.4
,0.4
,0.4
,0.4
,3.5
,0.7
,8.4
,7.7
,5.8
,6.7
,3.1
,3.2
,3
,2.6
,8.1
,5.4
,-5.3
,8.3
,7.7
,0
,0
,5.3
,0
,5.3
,5.4
,1
,7.3
,-0.4
,-0.4
,-6.7
,-3.5
,-0.7
,-5.8
,-0.4
,-3.2
,-3
,2.9
,-7.3
,-5.4
,0.3
,-0.3])

ddg= np.array([6.77
,6.55
,6.03
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
,7.08
,7.51
,6.38
,6.06
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

plt.scatter(diff,ddg)
m, b = np.polyfit(diff,ddg, 1)
plt.plot(diff, m*diff+b, color='red')
plt.xlabel("differences between the wt and mut")
plt.ylabel("experimental ddg values")
plt.title('hydrophaty index differences of wild type and mutant')
plt.show()

correlation_matrix = np. corrcoef(diff,ddg)
correlation_diffdgg = correlation_matrix[0,1]
r_squared = correlation_diffdgg**2.
print(r_squared)

# r_squared = 0.0011402007637654143
#%%
most_dept= sorted(i for i in ddg if i<0)
diff_dept=np.array([-7.3
,-7.3
,-4.2
,-5.4
,-5.7
,-5.7
,-5.3
,-5
,1
,2.8
,7
,-5.4
,-0.7
,4.6
,4.5
,5.3
,-3.6
,2.9
,-8.3
,-7.3
,-7
,-5.4
,-4.7
,-5.1
,-2.2
,-2.2
,-0.3
,-6.3])
 
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
 


most_enr= sorted(i for i in ddg if i>0)
diff_enr= np.array([2.9
,-5.4
,3.1
,-2.2
,0.9
,-2.6
,-0.3
,0.6
,7.3
,7.3
,7.3
,4.2
,0.9
,3.1
,0.4
,0.4
,0.4
,0.4
,3.5
,0.7
,8.4
,7.7
,5.8
,6.7
,3.1
,3.2
,3
,2.6
,8.1
,5.4
,-5.3
,8.3
,7.7
,0
,0
,5.3
,0
,5.3
,5.4
,1
,7.3
,-0.4
,-0.4
,-6.7
,-3.5
,-0.7
,-5.8
,-0.4
,-3.2
,-3
,2.9
,-7.3
,-5.4
,0.3
,-0.3])

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

p_hydro =stats.ttest_ind(diff,ddg)
print(p_hydro)
      
p_dept =stats.ttest_ind(diff_dept,most_dept)
print(p_dept)

p_enr =stats.ttest_ind(diff_enr,most_enr)
print(p_enr)

#%%

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

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

bp = ax.boxplot(diff, patch_artist = True,
                notch ='True', vert = 0)
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
    
plt.title('hydropathy differences of wt and mut')

plt.show(bp)


