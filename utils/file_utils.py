import os
import datetime

def generae_filename(file_name):
    
    new_file_name = os.path.split(file_name)[1]

    prefix = str(datetime.datetime.now())

    return "-".join([prefix,new_file_name])
