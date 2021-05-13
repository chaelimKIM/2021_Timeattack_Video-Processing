import pymysql

DataBase = pymysql.connect(
    host="115.138.67.190",
    user="root",
    passwd="2021capstone7",
    port=3306,
    database="TimeAttack",
    charset="utf8"
)    # MySQL DB에 연결
try:
    with DataBase.cursor() as curs:
        sql = "SELECT VERSION()"
        curs.execute(sql)
        rs = curs.fetchall()

        for row in rs:
            for data in row:
                print(data, end=' ')

        print("DB Connected")    # 연결 성공 시 출력
except:
    print("Connection failed")    # 연결 실패 시 출력


# 테스트용
class UploadDB:

    def __init__(self):
        test = None


#class SelectDB:

