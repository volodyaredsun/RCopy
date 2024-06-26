import os
import shutil
from pathlib import Path
from rcopy_funcs import *

current_path = os.getcwd()          # текущий путь

d_file_names = read_file_names(file_tasks)
cur_date = get_cur_date()

for _, p in d_file_names.items():
    #print(p[1], Path(cur_date))
    p2_dest = os.path.join(p[1], cur_date)
    #print(f'p2_dest = {p2_dest}')
    #p2_dest = os.path.dirname(os.path.join(p2_dest, '123'))
    if not os.path.isdir(p2_dest):
        os.makedirs(p2_dest)

#print(d_file_names)
#print(Path(get_cur_date()))

print(current_path)
#print(os.path.join(current_path, 'directory'))