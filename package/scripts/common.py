import os.path as path

from resource_management import *

PRESTO_RPM_URL = 'http://search.maven.org/remotecontent?filepath=com/facebook/presto/presto-server-rpm/0.115/presto-server-rpm-0.115.rpm'
PRESTO_RPM_NAME = 'presto-server-rpm.x86_64.rpm'

def create_tpch_connector(node_properties):
        Execute('mkdir -p {0}'.format(node_properties['plugin.config-dir']))
        Execute('echo "connector.name=tpch" > {0}'.format(path.join(node_properties['plugin.config-dir'], 'tpch.properties')))