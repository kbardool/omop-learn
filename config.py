
# Database Setup
PG_HOST = '20.224.120.22'
PG_PORT = '5444'
DB_NAME = 'OHDSI'
PG_USERNAME = "athena_admin"
PG_PASSWORD = "3Ej14dDacXaBFliu"

PG_HOST ='wt-1-00.exascience.org'
PG_PORT = '5432'
DB_NAME ='athena'
PG_USERNAME = "postgres"
PG_PASSWORD = "postgres"

# PG_USERNAME = 'athena'
# PG_PASSWORD = '7YPAGTLKzlY66l2G'

# Schemas
OMOP_CDM_SCHEMA = 'omopcdm' # schema holding standard OMOP tables
CDM_AUX_SCHEMA = 'results' # schema to hold auxilliary tables not tied to a particular schema
CDM_VERSION = 'v5.3.1' # set to 'v5.x.x' if on v5

# SQL Paths
SQL_PATH_COHORTS = 'sql/Cohorts' # path to SQL scripts that generate cohorts
SQL_PATH_FEATURES = 'sql/Features' # path to SQL scripts that generate features

# Cache
DEFAULT_SAVE_LOC = '/tmp/' # where to save temp files

# Only used in ORM code
omop_schema = 'omopcdm'
user_schema = 'results'
