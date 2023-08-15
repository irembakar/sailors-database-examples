# Reading from existing database version
from radb import *

# connection to the database
db = literal_eval(Connector.connect())

# select * from sailors;
q1 = db.sailors

# select S.sname,R.bid from sailors S, reserves R where S.sid=R.sid;
q2 = db.sailors.join(db.reserves, 'sid').project('sname', 'bid')

# select S.sname,B.bname from sailors S, reserves R, boats B where S.sid=R.sid and B.bid=R.bid;
q3 = db.sailors.join(db.reserves, 'sid').join(db.boats, 'bid').project('sname', 'bname')

# select S.sid from Sailors MINUS select R.sid from reserves R;
q4 = db.sailors.minus(db.reserves.project('sid'))

# select S.sid from reserves R GROUP BY R.sid HAVING count(*)>1;
q5 = db.reserves.group('sid').having('count(*) > 1').project('sid')

# execute the queries print the results
print(q1.execute())
print(q2.execute())
print(q3.execute())
print(q4.execute())
print(q5.execute())