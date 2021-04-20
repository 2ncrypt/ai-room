import pymysql as q

db = q.connect( #db로그인 기본 형식은 지켜줘야함.
    host='localhost',
    port= 3306,
    user = 'root',
    passwd = 'ekthdlek12',
    db = 'busan'
)
sql = '''
CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
cursor = db.cursor()
# fly = cursor.execute
# fly('SELECT * FROM users;') #쿼리문 실행 excute
# users = cursor.fetchall() 
# #쿼리를 실행시켜 받은 값들을 fetchall로 모아서 users 변수에 전달

# fly(sql)
# db.commit() #이거안해도 클로즈하면 올라가긴함.
# db.close()

# fly('SELECT * FROM topic;')
# topic = cursor.fetchall()
# print(topic)
