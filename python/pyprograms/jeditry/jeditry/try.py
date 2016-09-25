#! /usr/bin/env python
#
# topic: file read in
# to run this program ( go to bottom terminal): python try.py configtry

import os, sys, subprocess, math, re, shutil,copy
print

if(len(sys.argv) != 2):
    print("Usage: jedimaster config")
    sys.exit(1);


print "Config file: %s"%sys.argv[1]    # Config file: configtry


#parse config file
config_file = open(sys.argv[1], 'r')   # sys.argv[1] = configtry
config = {}                            # dictionary to store elements of file to be opened

string_regex = re.compile('"(.*?)"')   # read everything inside " " e.g. output_folder = "trial_0/"
value_regex = re.compile('[^ |\t]*')   #                                   temp[0]         temp[1]

                                       # eg. pix_scale=0.03    # pixel scale to use (arseconds per pixel)
                                       #     temp[0]   temp[1]
                                       # if no ^  then, values will not be seen


for line in config_file:
    if not line.startswith("#"):
        temp = line.split("=")         # splitted at = then, we have temp[0] and temp[1]
        if temp[1].startswith("\""):   # start with quotation mark "
            config[temp[0]] = string_regex.findall(temp[1])[0]
        else:                          # is no [0] will print # comments in the config and so on
            config[temp[0]] = value_regex.findall(temp[1])[0]
print config                           # {'HST_image': 'HST.fits', 'image': ... }

config_record = copy.deepcopy(config)

#make the filenames from the config parameters
config['HST_image'] = config['output_folder'] +config['prefix']+config['HST_image']
config['HST_convolved_image'] = config['output_folder'] +config['prefix']+config['HST_convolved_image']


#if the output folder doesn't exist, create it
if (not os.path.exists(config['output_folder'])): # creates an empty folder called trial_0
    os.makedirs(config['output_folder'])          # config['output_folder'] :  output_folder="trial_0/"

#make folder for convolved images
convolved_path = "%sconvolved/"%config['output_folder']
if not os.path.exists(convolved_path):            # inside trial_0/ folder creates empty folder convolved
    os.makedirs(convolved_path)


#make folders because cfitsio is bad at it
# creates 12 folders distorted and stamp inside trial_0

for x in xrange(0, int(math.ceil(float(config['num_galaxies'])/1000))): # num_galaxies=12420
    postage_path = "%sstamp_%i"%(config['output_folder'],x)             # stamp_0 etc
    distorted_path = "%sdistorted_%i"%(config['output_folder'],x)       # distorted_0 etc
    if not os.path.exists(postage_path): os.makedirs(postage_path)
    if not os.path.exists(distorted_path): os.makedirs(distorted_path)

#function to run a program and write output to the shell
# now we are just writing the function
# if there is no executable jedicatalog, then it will only print
#--------------------------
# Running: jedicatalog
# Command:
# ./jedicatalog configtry
#--------------------------
# OSError: [Errno 2] No such file or directory



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
#now we will invoke the function
run_process("jedicatalog", ["./jedicatalog", sys.argv[1]])


# #make postage stamp images that fit the catalog parameters
# run_process("jeditransform", ['./jeditransform', config['catalog_file'], config['dislist_file']])
#
# #lens the galaxies one at a time
# run_process("jedidistort", ['./jedidistort', config['nx'], config['ny'], config['dislist_file'], config['lenses_file'], config['pix_scale'], config['lens_z']])
#
# #combine the lensed galaxies onto one large image
# run_process("jedipaste (make unconvolved image)", ['./jedipaste', config['nx'], config['ny'], config['distortedlist_file'], config['HST_image']])
#
# #convonlve the large image with the PSF
# #this creates one image for each band of the image
# run_process("jediconvolve", ['./jediconvolve', config['HST_image'], config['psf_file'], convolved_path])
#
# #combine each band into a single image
# run_process("jedipaste (make convolved image)", ['./jedipaste', config['nx'], config['ny'], config['convolvedlist_file'], config['HST_convolved_image']])
#
# #scale the image down from HST to LSST scale and trim the edges
# run_process("jedirescale", ['./jedirescale', config['HST_convolved_image'], config['pix_scale'], config['final_pix_scale'], config['x_trim'], config['y_trim'], config['LSST_convolved_image']])
#
# #simulate exposure time and add Poisson noise
# run_process("jedinoise", ['./jedinoise', config['LSST_convolved_image'], config['exp_time'], config['noise_mean'], config['LSST_convolved_noise_image']])
#
#
#
#
# ###make the folder for the 90_ simulations
# ###this is an ugly, but fast way to do this. almost all of the next section is redundant
# ###if this gets any more complicated, it should be completely rewritten
#
# pre = "90_"
# config_record['90_prefix'] = pre + config_record['prefix']
# config_record['90_output_folder'] = pre+config_record['output_folder']
# config['90_output_folder'] = config_record['90_output_folder']
#
# config['90_HST_image'] = config_record['90_output_folder'] +config_record['90_prefix']+config_record['HST_image']
# config['90_HST_convolved_image'] = config_record['90_output_folder'] +config_record['90_prefix']+config_record['HST_convolved_image']
# config['90_LSST_convolved_image'] = config_record['90_output_folder'] +config_record['90_prefix']+config_record['LSST_convolved_image']
# config['90_LSST_convolved_noise_image'] = config_record['90_output_folder'] +config_record['90_prefix']+config_record['LSST_convolved_noise_image']
# config['90_catalog_file'] = config_record['90_output_folder'] + config_record['90_prefix'] + config_record['catalog_file']
# config['90_dislist_file'] =config_record['90_output_folder'] + config_record['90_prefix'] + config_record['dislist_file']
# config['90_distortedlist_file'] = config_record['90_output_folder'] +config_record['90_prefix'] + config_record['distortedlist_file']
# config['90_convolvedlist_file'] = config_record['90_output_folder'] +config_record['90_prefix'] + config_record['convolvedlist_file']
#
# print config_record['90_prefix']
# print config_record['90_output_folder']
# print config['90_HST_image']
# print config['90_HST_convolved_image']
# print config['90_LSST_convolved_image']
# print config['90_LSST_convolved_noise_image']
# print config['90_catalog_file']
# print config['90_dislist_file']
# print config['90_distortedlist_file']
# print config['90_convolvedlist_file']
#
#
# #if the output folder doesn't exist, create it
# if (not os.path.exists(config['90_output_folder'])):
#     os.makedirs(config['90_output_folder'])
#
#
# #make folder for convolved images
# convolved_path = "%sconvolved/"%(config['90_output_folder'])
# if not os.path.exists(convolved_path):
#     os.makedirs(convolved_path)
#
#
# #make folders because cfitsio is bad at it
# for x in xrange(0, int(math.ceil(float(config['num_galaxies'])/1000))):
#     postage_path = "%sstamp_%i"%(config['90_output_folder'],x)
#     distorted_path = "%sdistorted_%i"%(config['90_output_folder'],x)
#     if not os.path.exists(postage_path): os.makedirs(postage_path)
#     if not os.path.exists(distorted_path): os.makedirs(distorted_path)
#
#
# old_catalog_file= open(config['catalog_file'], 'r')
# catalog_file= open(config['90_catalog_file'], 'w')
# for old_line in old_catalog_file:
#     l = old_line.split("\t")
#     angle = float(l[3])+90
#     angle -= 360*(int(angle)/360)
#     l[3] = str(angle)
#     l[-1]= l[-1].replace(config['output_folder'],config['90_output_folder'])
#     l[-2]= l[-2].replace(config['output_folder'],config['90_output_folder'])
#     line = "\t".join(l)
#     catalog_file.write(line)
# old_catalog_file.close()
# catalog_file.close()
#
#
# old_convolvedlist_file= open(config['convolvedlist_file'], 'r')
# convolvedlist_file= open(config['90_convolvedlist_file'], 'w')
# for old_line in old_convolvedlist_file:
#     line = old_line.replace(config['output_folder'],config['90_output_folder'])
#     convolvedlist_file.write(line)
# old_convolvedlist_file.close()
# convolvedlist_file.close()
#
# old_distortedlist_file= open(config['distortedlist_file'], 'r')
# distortedlist_file= open(config['90_distortedlist_file'], 'w')
# for old_line in old_distortedlist_file:
#     line = old_line.replace(config['output_folder'],config['90_output_folder'])
#     distortedlist_file.write(line)
# old_distortedlist_file.close()
# distortedlist_file.close()
#
#
# #make postage stamp images that fit the catalog parameters
# run_process("jeditransform", ['./jeditransform', config['90_catalog_file'], config['90_dislist_file']])
#
# #lens the galaxies one at a time
# run_process("jedidistort", ['./jedidistort', config['nx'], config['ny'], config['90_dislist_file'], config['lenses_file'], config['pix_scale'], config['lens_z']])
#
# #combine the lensed galaxies onto one large image
# run_process("jedipaste (make unconvolved image)", ['./jedipaste', config['nx'], config['ny'], config['90_distortedlist_file'], config['90_HST_image']])
#
# #convonlve the large image with the PSF
# #this creates one image for each band of the image
# run_process("jediconvolve", ['./jediconvolve', config['90_HST_image'], config['psf_file'], convolved_path])
#
# #combine each band into a single image
# run_process("jedipaste (make convolved image)", ['./jedipaste', config['nx'], config['ny'], config['90_convolvedlist_file'], config['90_HST_convolved_image']])
#
# #scale the image down from HST to LSST scale and trim the edges
# run_process("jedirescale", ['./jedirescale', config['90_HST_convolved_image'], config['pix_scale'], config['final_pix_scale'], config['x_trim'], config['y_trim'], config['90_LSST_convolved_image']])
#
# #simulate exposure time and add Poisson noise
# run_process("jedinoise", ['./jedinoise', config['90_LSST_convolved_image'], config['exp_time'], config['noise_mean'], config['90_LSST_convolved_noise_image']])
#
#
# print "jedisim successful! Exiting."
