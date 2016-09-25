##==============================================================================
## replace_outfolders
##==============================================================================
def replace_outfolders(outfolders):
    ''' Replaces given list of output folders   '''

    # imports
    import shutil,os

    for outfolder in outfolders:


        if os.path.exists(outfolder):
            print('Replacing folder: ', outfolder)
            shutil.rmtree(outfolder)
            os.makedirs(outfolder)
        else:
            print('Making new folder: ', outfolder)
            os.makedirs(outfolder)


outfolders = ['junk1', 'junk2/a']
replace_outfolders(outfolders)
