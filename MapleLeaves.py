import pandas as pd
import matplotlib.pyplot as plt
#"Maple Leaves" two samples with different sampling strategy(Measured in mm).
# HYB: hydrobiology group, got random sample from the supervisor
# HSE: hydroscience group, had the freedom to collect an own leaf
sample_data=pd.read_csv('MapleLeaves.csv')
print(sample_data)
type(sample_data)
print(sample_data.length)
print(sample_data.length.iloc[2])
#Compare the length of leaves collected by HSE and HYB students
#Isolating Data from HSE and HYB
hse= sample_data[sample_data.group == 'HSE']
print(hse)
hyb=sample_data[sample_data.group == 'HYB']
print(hyb)
plt.plot(hse.no,hse.length)
plt.plot(hyb.no,hyb.length)
plt.legend(['HSE','HYB'])
plt.xlabel('No. of Samples')
plt.ylabel('Length of Leaves(mm)')
plt.show()
#From plot, HSE students had longer leaves.