from sedov_main_function import sedov_main_time
from sedov_main_function import sedov_main
import pickle
from matplotlib import pyplot as plt
import pandas as pd

##sedov_main_time(3.0, 0.0, 0.001, 0.011, 2, 8.0E13, 1.4, 'dataout.p')
sedov_main(2, 0.0, 0.05, 6.28, 1.4, 'dataout.p')

#df=pd.read_pickle('dataout.p')
##df=pd.DataFrame(df)
#print(df)
##here is the parameter listings for both funtions

##sedov_main(geom_in, omega_in, time_in, blast_energy, gamma_in, outfile)
##sedov_main_time(geom_in, omega_in, time_initial, time_final, time_steps, blast_energy, gamma_in, outfile)

#the following lines, open a file, unpickle the dictionary outputs previuosly writen to that file,
## and then closes the file
## arrays can then be called from the dictionary
##data_in = open('dataout.p', 'rb')
#results = pickle.load(data_in)
#data_in.close()
#pos = results['position']
#rho = results['density']
#plt.plot(pos[1], rho[1])
#plt.show

#the code pickles dictionaries with the following keys and arrays
#use key  like an index to call certain arrays

#single_time_output = {'density': den, 'velocity': vel, 'pressure': pres,
#                      'total_energy': enertot, 'thermal_energy': enertherm, 
#                      'kinetic_energy': enerkin, 'mach': mach, 'position': zpos}

#time_step_output = {'density': den_time, 'velocity': vel_time, 'pressure': pres_time,
#                    'total_energy': enertot_time, 'thermal_energy': enertherm_time, 
#                    'kinetic_energy': enerkin_time, 'mach': mach_time, 
#                    'position': zpos_time, 'time': time}