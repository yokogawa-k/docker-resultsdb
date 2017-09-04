# Copy this file to `conf/settings.py` to put it into effect. It overrides the values defined
# in `resultsdb/config.py`.

# ================== General ===================

DEBUG = True
PRODUCTION = False
SECRET_KEY = 'replace-me-with-something-random'

HOST = '0.0.0.0'
PORT = 5001


SQLALCHEMY_DATABASE_URI = 'sqlite:////resultsdb_data/resultsdb_db.sqlite'
# SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbuser:dbpassword@dbhost:dbport/dbname'
SHOW_DB_URI = True

LOGFILE = '/var/log/resultsdb/resultsdb.log'
FILE_LOGGING = False
SYSLOG_LOGGING = False
STREAM_LOGGING = True

# Specify which fields are required (in addition to those already required)
#  when creating result/group/testcase.
# If you want to set some result's extra-data as required, you can do so by
#  prepending 'data.' to the name (e.g. 'data.arch').
REQUIRED_DATA = {
    'create_result': [],
    'create_group': [],
    'create_testcase': [],
}


# ================== Authentication ===================

# Supported values: "oidc"
AUTH_MODULE = None

# OIDC Configuration
OIDC_ADMINS = []
OIDC_CLIENT_SECRETS = 'conf/oauth2_client_secrets.json'
OIDC_AUD = 'My-Client-ID'
OIDC_SCOPE = 'https://pagure.io/taskotron/resultsdb/access'
OIDC_RESOURCE_SERVER_ONLY = True


# ================== Messaging ===================

# Set this to True or False to enable publishing to a message bus
MESSAGE_BUS_PUBLISH = False
# Name of the message bus plugin to use goes here.  'fedmsg' is installed by
# default, but you could create your own.
# Supported values: 'dummy', 'stomp', 'fedmsg'
MESSAGE_BUS_PLUGIN = 'fedmsg'
# You can pass extra arguments to your message bus plugin here.  For instance,
# the fedmsg plugin expects an extra `modname` argument that can be used to
# configure the topic, like this:
#   <topic_prefix>.<environment>.<modname>.<topic>
# e.g. org.fedoraproject.prod.taskotron.result.new
MESSAGE_BUS_KWARGS = {'modname': 'resultsdb'}
