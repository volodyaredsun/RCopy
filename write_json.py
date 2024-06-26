import json
from parm_rcopy import *

data = {
    'dropbox': {
        'd_init': 'd:\1\new\C',
        'd_dest': 'e:\00 -RESERV_COPY\11 - DropBox'
    },
    'mega': {
        'd_init': 'd:\1\new\С',
        'd_dest': 'e:\00 -RESERV_COPY\13 - DropBox'
    }

}

with open(file_tasks, 'w', encoding='utf-8') as fw:
    json.dump(data, fw)