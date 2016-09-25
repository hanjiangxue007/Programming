#! /usr/bin/env python
#command: python jedimaster.py physics_setting/config 

# inside config: pix_scale     = 0.03  # pixel
#                output_folder = "trial_0/"
#                catalog_file  = "catalog.txt"


import os, sys, subprocess, math, re, shutil,copy

#parse command line inputs
if(len(sys.argv) != 2):
    print("Usage: jedimaster config")
    sys.exit(1);


print "Config file: %s"%sys.argv[1]  # physics_setting/config

#parse config file
config_file = open(sys.argv[1], 'r') # physics_setting/config
config = {}                          # dictionary
string_regex = re.compile('"(.*?)"') # inside ""
value_regex = re.compile('[^ |\t]*') # except pipe and tab, repeated

for line in config_file:
    if not line.startswith("#"):     #ingnore comments
        temp = line.split("=")       # split at = 
        if temp[1].startswith("\""): # starting with quote "
            config[temp[0]] = string_regex.findall(temp[1])[0]
        else:
            config[temp[0]] = value_regex.findall(temp[1])[0]
print config                         # prints list [ ..... ]

config_record = copy.deepcopy(config) # making deep copy of dictionary config



#make the filenames from the config parameters
config['HST_image'] = config['output_folder'] +config['prefix']+config['HST_image']
#                             trial_0/                 trial0_          HST.fits

config['HST_convolved_image'] = config['output_folder'] +config['prefix']+config['HST_convolved_image']
config['LSST_convolved_image'] = config['output_folder'] +config['prefix']+config['LSST_convolved_image']
config['LSST_convolved_noise_image'] = config['output_folder'] +config['prefix']+config['LSST_convolved_noise_image']
config['catalog_file'] = config['output_folder'] + config['prefix'] + config['catalog_file']
config['dislist_file'] =config['output_folder'] + config['prefix'] + config['dislist_file']
config['distortedlist_file'] = config['output_folder'] +config['prefix'] + config['distortedlist_file']
config['convolvedlist_file'] = config['output_folder'] +config['prefix'] + config['convolvedlist_file']

#if the output folder doesn't exist, create it
if (not os.path.exists(config['output_folder'])): # empty folder called
    os.makedirs(config['output_folder'])          # trial_0

#make folder for convolved images
convolved_path = "%sconvolved/"%config['output_folder']
#                 trial_0/convolved
if not os.path.exists(convolved_path): # empty folder inside trial_0/
    os.makedirs(convolved_path)        # convolved


#make folders because cfitsio is bad at it
#                  13                           12420
for x in xrange(0, int(math.ceil(float(config['num_galaxies'])/1000))):
    postage_path = "%sstamp_%i"%(config['output_folder'],x)
    # stamp_0 to stamp_12
    
    distorted_path = "%sdistorted_%i"%(config['output_folder'],x)
    # distorted_0 to distorted_12
    
    if not os.path.exists(postage_path): os.makedirs(postage_path)
    if not os.path.exists(distorted_path): os.makedirs(distorted_path)

#function to run a program and write output to the shell
#eg. run_process("jedicatalog", ["./jedicatalog", sys.argv[1]])
def run_process(name, args,):
    print "------------------------------------------------------------------------"
    print "Running: %s\nCommand:"%name
    for arg in args:
        print arg,
    print ""
    print "------------------------------------------------------------------------"
    process = subprocess.Popen(args)

    process.communicate()
    if process.returncode != 0:
        print "Error: %s did not terminate correctly. Return code: %i."%(name, process.returncode)
        sys.exit(1)

#make the catalog of galaxies
run_process("jedicatalog", ["./jedicatalog", sys.argv[1]])


print "jedisim successful! Exiting."



