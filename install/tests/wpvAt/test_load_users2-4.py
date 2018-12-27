import os
from ldap3 import Server, Connection, ALL, LDIF, MODIFY_REPLACE

# variables
rootpw = os.environ['ROOTPW'] if 'ROOTPW' in os.environ else 'changeit'
port = os.environ['SLAPDPORT'] if 'SLAPDPORT' in os.environ else '8389'
host = 'localhost:' + port
rootdn = 'dc=at'
admindn = 'cn=admin,dc=at'
testpw = 'test'

print('testing python-ldap: load users 2-4')
s = Server(host, get_info=ALL)
c = Connection(s, admindn, rootpw, auto_bind=True, raise_exceptions=False)

print('add test-add')
c.add('cn=test-add-operation,o=test', 'inetOrgPerson',
      {'objectClass': 'inetOrgPerson', 'sn': 'test-add', 'cn': 'test-add-operation'})

print('add domain')
c.add('dc=wpv,dc=at', 'domain')

print('adding test users')
c.add('uid=test.user2_adam,dc=wpv,dc=at', 'inetOrgPerson',
      {'objectClass': 'inetOrgPerson', 'givenName': 'Adam', 'cn': 'Adam Bäcker',
       'sn': 'Bäcker'})
c.add('uid=test.user3_eva,dc=wpv,dc=at', 'inetOrgPerson',
      {'objectClass': 'inetOrgPerson', 'givenName': 'Eva', 'cn': 'Eva Schüßler-Bäcker',
       'sn': 'Schüßler-Bäcker'})
c.add('uid=test.user4_berta,dc=wpv,dc=at', 'inetOrgPerson',
      {'objectClass': 'inetOrgPerson', 'givenName': 'Berta', 'cn': 'Berta Chamäleon Koala',
       'sn': 'Chamäleon Koala'})

print('dump_testuser search')
c.search('dc=wpv,dc=at', '(uid=*)')

print('change passwords users 2-4')
c.modify('uid=test.user2_adam', {'userPassword': [(MODIFY_REPLACE, ['newpass'])]})
c.modify('uid=test.user3_eva', {'userPassword': [(MODIFY_REPLACE, ['newpass'])]})
c.modify('uid=test.user4_berta', {'userPassword': [(MODIFY_REPLACE, ['newpass'])]})