# Setup a single data product and series
# wraps the meta scripts with automation

import pathlib as pl 
import configparser as cp


meta_scripts_dir = pl.Path.cwd().joinpath('../meta-scripts').resolve()

credentials_dir = pl.Path.home().joinpath('.metralytics')

config_file_path = credentials_dir.joinpath('pgdb.ini')

def make_config_file():
    if not credentials_dir.exists():
        credentials_dir.mkdir()
    
    db_config = cp.SafeConfigParser()

    db_config['DEFAULT'] = {'host':'localhost',
                            'port':'5432',
                            'user':'galen',
                            'password':'',
                            'dbname':'postgres',
                            }

    db_config['local-admin'] = {'host':'localhost',
                            'port':'5432',
                            'user':'admin',
                            'password':'',
                            'dbname':'postgres',
                            }

    db_config['census_loader'] = {'host':'localhost',
                            'port':'5432',
                            'user':'census_loader',
                            'password':'',
                            'dbname':'postgres',
                            'schema':'census'}


    db_config['census_user'] = {'host':'localhost',
                            'port':'5432',
                            'user':'gswint',
                            'password':'',
                            'dbname':'postgres',
                            'schema':'census'}

    with open(config_file_path, 'w') as configfile:
        db_config.write(configfile)




# db_config = cp.SafeConfigParser()

# # read host, port, user, password, dbname, schema for 'census'
# db_config.read(config_file)
# cfg_host = db_config.get('census', 'host')
# cfg_port = db_config.get('census', 'port')
# cfg_user = db_config.get('census', 'user')
# cfg_password = db_config.get('census', 'password')
# cfg_dbname = db_config.get('census', 'dbname')
# cfg_schema = db_config.get('census', 'dbname')
