import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yhdb.c8nbdutl9vtz.ap-northeast-2.rds.amazonaws.com',
            database = 'movie_db',
            user = 'movie_user1',
            password = '123hello7')
    
    return connection


 # 호스트명은 내 AWS의 RDS -> yh_db -> 엔드포인트 yhdb.c8nbdutl9vtz.ap-northeast-2.rds.amazonaws.com
