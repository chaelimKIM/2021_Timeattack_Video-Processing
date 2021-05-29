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


class DB:

    @staticmethod
    def update_processing(up_id):
        with DataBase.cursor() as curs:
            sql = "SELECT processing FROM upload WHERE up_id=" + str(up_id)
            curs.execute(sql)
            data = curs.fetchone()
            for pr in data:
                if pr == 0:
                    sql = "UPDATE upload SET processing=-1 WHERE up_id=" + str(up_id)
                    curs.execute(sql)
                    DataBase.commit()
                elif pr == -1:
                    sql = "UPDATE upload SET processing=1 WHERE up_id=" + str(up_id)
                    curs.execute(sql)
                    DataBase.commit()
                else:
                    print("Unavailable processing value!")
                    return

    def select_upid_by_processing(self):
        with DataBase.cursor() as curs:
            sql = "SELECT up_id FROM upload WHERE processing=0"
            curs.execute(sql)
            data = curs.fetchone()
            for up_id in data:
                self.update_processing(up_id)
                return up_id

    @staticmethod
    def select_upvidpath(up_id):
        with DataBase.cursor() as curs:
            sql = "SELECT up_vid_path FROM upload_vid WHERE up_vid_id=" + str(up_id)
            curs.execute(sql)
            data = curs.fetchall()
            return data[0][0]

    @staticmethod
    def select_upimgpath(up_id):
        with DataBase.cursor() as curs:
            sql = "SELECT up_img_path FROM upload_img WHERE up_img_id=" + str(up_id)
            curs.execute(sql)
            data = curs.fetchall()
            return data[0][0]

    @staticmethod
    def select_facecount(up_id):
        with DataBase.cursor() as curs:
            sql = "SELECT face_count FROM upload WHERE up_id=" + str(up_id)
            curs.execute(sql)
            data = curs.fetchall()
            return data[0][0]
