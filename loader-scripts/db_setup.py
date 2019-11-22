# Setup a single data product and series
# wraps the meta scripts with automation

import pathlib as pl 
import configparser as cp
import psycopg2 as psy


meta_scripts_dir = pl.Path.cwd().joinpath('../meta-scripts').resolve()

credentials_dir = pl.Path.home().joinpath('.metralytics')

config_file_name = 'pgdb.ini'

config_file_path = credentials_dir.joinpath(config_file_name)

def make_config_file():
    if not credentials_dir.exists():
        credentials_dir.mkdir()
    
    db_config = cp.ConfigParser()

    db_config['DEFAULT'] = {'host':'localhost',
                            'port':'5432',
                            'user':'galen',
                            'password': '',
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


def get_connection_config(profile='DEFAULT'):
    '''Loads a connection configuration from a pgdb.ini file
    located in the .limetree directory. If no profile is specified, 
    it will load the DEFAULT profile.
    
    Returns:
        Dict of items for a psycopg2 connection to a PostgreSQL database '''

    with open(config_file_path, 'r') as configfile:
        db_config = cp.ConfigParser()
        db_config.read(config_file_path)
    
    db_config_dict = dict(db_config.items(profile))
    
    return db_config_dict

def get_psycopg_conn(profile='DEFAULT'):
    '''returns a psycopg2 connection to the profile named and described in
    the config file at ~/.limetree/pgdb.ini
    
    Returns:
        psycopg2 Connection object'''
    
    config_info = get_connection_config(profile)
    conn = psy.connect(**config_info)
    
    return conn

def get_psycopg_dict_curs(profile='DEFAULT'):
    '''Return a psycopg2.extras.DictCursor for the connection in the 
    profile given
    '''
    
    conn = get_psycopg_conn(profile)
    rd_curs = conn.cursor(cursor_factory=psy_extras.DictCursor)
    
    return rd_curs

