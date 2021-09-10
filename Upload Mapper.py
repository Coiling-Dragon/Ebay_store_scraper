from Mapper import main_mapper_program
import os
import psutil
import time
from small_programs.AMAZON_API_INVLOADER import flat_file_invloader
from small_programs.bqool_uploader import Bqool_Uploader



#================================================================= May need to def function_path_finder():
program_path = os.path.realpath(__file__).split('\\')
program_path = program_path[0:(len(program_path)-1)]
program_path = "/".join(program_path)
if 'Googledrive' in program_path:
    program_path = program_path.split('Googledrive')[0] + 'Googledrive/Python_Shared/In_Out_' + str(os.getenv('username'))
if 'Google Drive' in program_path:
    program_path = program_path.split('Google Drive')[0] + 'Google Drive/Python_Shared/In_Out_' + str(os.getenv('username'))
print(program_path)
#=================================================================

file_folder = program_path + '/files_Mapper/'

start_time = time.time()

#user_name = os.path.expanduser("~").split('\\')[2]
user_name = str(os.getenv('username'))
print(user_name+'---------------\n')


main_mapper_program(file_folder)


upl_error = True
while upl_error == True:
    try:
        
        flat_file_invloader(file_folder)
        upl_error = False
        
    except Exception as ex:
            print(ex,'---------Error in Uploading files to AMAZON')

            
upl_error = True  
while upl_error == True:
    try:
        
        Bqool_Uploader(file_folder)
        upl_error = False
        
    except Exception as ex:
            print(ex,'---------Error in Uploading files TO BQOOL')
            #raise ex
            try:
                for proc in psutil.process_iter():
                    #print(proc.name())
                    if 'chrome' in proc.name():
                        proc.kill()
            except:
                pass



elapsed_time = round((time.time() - start_time),2)

hours_ = elapsed_time//3600
min_ = (elapsed_time%3600)//60
sec_ = (elapsed_time%60)


print("\n\nFinished in:",int(hours_),'Hours,',int(min_),'min,',(sec_),'sec.')

time_str = str(time.strftime('%Y-%m-%d %Hh%Ms', time.localtime(time.time()) ))
print(time_str)