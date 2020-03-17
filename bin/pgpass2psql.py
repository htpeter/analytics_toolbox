"""
Transforms pgpass into a config file or a set of psql statements.
"""

import getpass
import csv
import platform

system_type = platform.system()
if system_type == 'Linux':
    os_base_path = f'/home/{getpass.getuser()}/'
elif system_type == 'Darwin':
    os_base_path = f'/Users/{getpass.getuser()}/'
else:
    # prolly gonna be unix given the world, right?
    os_base_path = f'/home/{getpass.getuser()}/'


with open(os_base_path + '.pgpass') as f:
    for line in f.readlines():
        comps = line.split(":")
        hostname, port, database, user = comps[0], comps[1], comps[2], comps[3] 
        print(f'alias varname="psql -h {hostname} -p {port} -U {user} {database}"')
