#%%
import ibm_db
#%%
dsn_hostname =  "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_pwd =  "d7wfdm25bhgd23-x"
dsn_port = 50000
dsn_database =  "BLUDB"
dsn_uid =  "nwp52966"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_protocol = "TCPIP"
#%%
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)
print(dsn)
#%%
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
#%%
createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"
createStmt = ibm_db.exec_immediate(conn, createQuery)
#%%
insertQuery = "insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"
insertStmt = ibm_db.exec_immediate(conn, insertQuery)
insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)
selectQuery = "select * from INSTRUCTOR"
selectStmt = ibm_db.exec_immediate(conn, selectQuery)
ibm_db.fetch_both(selectStmt)
#%%
while ibm_db.fetch_row(selectStmt) != False:
    print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))

#%%
updateQuery = "update INSTRUCTOR set CITY='MOOSETOWN' where FNAME='Rav'"
updateStmt = ibm_db.exec_immediate(conn, updateQuery)

#%%
import pandas as pd 
import ibm_db_dbi
#%%
pconn = ibm_db_dbi.Connection(conn)
#%%
selectQuery = "select * from INSTRUCTOR"
pdf = pd.read_sql(selectQuery, pconn)
pdf.LNAME[0]
pdf
#%%
pdf.shape
#%%
ibm_db.close(conn)

#%%
