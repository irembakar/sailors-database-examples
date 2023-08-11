import sqlite3

con = sqlite3.connect(":memory:")

# create the tables and insert data
cur = con.cursor()
cur.execute("CREATE TABLE sailors (sid INTEGER PRIMARY KEY, sname TEXT, rating INTEGER);")
cur.execute("CREATE TABLE boats (bid INTEGER PRIMARY KEY, bname TEXT, color TEXT);")
cur.execute("CREATE TABLE reserves (sid INTEGER, bid INTEGER, day DATE, PRIMARY KEY (sid, bid));")
cur.execute("INSERT INTO sailors VALUES (22, 'Dustin', 7);")
cur.execute("INSERT INTO sailors VALUES (31, 'Lubber', 8);")
cur.execute("INSERT INTO sailors VALUES (58, 'Rusty', 10);")
cur.execute("INSERT INTO boats VALUES (101, 'Interlake', 'Blue');")
cur.execute("INSERT INTO boats VALUES (102, 'Interlake', 'Red');")
cur.execute("INSERT INTO boats VALUES (103, 'Clipper', 'Green');")
cur.execute("INSERT INTO reserves VALUES (22, 101, '2023-04-16');")
cur.execute("INSERT INTO reserves VALUES (22, 102, '2023-04-17');")
cur.execute("INSERT INTO reserves VALUES (58, 101, '2023-04-16');")

# select * from sailors;
q1 = "SELECT * FROM sailors;"

# select S.sname,R.bid from sailors S, reserves R where S.sid=R.sid;
q2 = "SELECT S.sname, R.bid FROM sailors S JOIN reserves R ON S.sid = R.sid;"

# select S.sname,B.bname from sailors S, reserves R, boats B where S.sid=R.sid and B.bid=R.bid;
q3 = "SELECT S.sname, B.bname FROM sailors S JOIN reserves R ON S.sid = R.sid JOIN boats B ON R.bid = B.bid;"

# select S.sid from Sailors MINUS select R.sid from reserves R;
q4 = "SELECT sid FROM sailors EXCEPT SELECT sid FROM reserves;"

# select S.sid from reserves R GROUP BY R.sid HAVING count(*)>1;
q5 = "SELECT sid FROM reserves GROUP BY sid HAVING COUNT(*) > 1;"

# execute the queries print the results
cur.execute(q1)
print(cur.fetchall())

cur.execute(q2)
print(cur.fetchall())

cur.execute(q3)
print(cur.fetchall())

cur.execute(q4)
print(cur.fetchall())

cur.execute(q5)
print(cur.fetchall())

# close the connection
con.close()