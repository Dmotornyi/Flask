import sqlite3
import time
import math

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

#    def getMenu(self):
#        sql = '''SELECT * FROM hardware'''
#        try:
#            self.__cur.execute(sql)
#            res = self.__cur.fetchall()
#            if res: return res
#        except:
#            print("Ошибка чтения из БД")
#        return []

    def addTech(self, who_issue, tech_type, tech_name, tech_sn, tech_in, for_whom, tech_locate, tech_buisnes, input_date, input_coment):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO hardware VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (who_issue, tech_type, tech_name, tech_sn, tech_in, for_whom, tech_locate, tech_buisnes, input_date, input_coment, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД " + str(e))
            return False

        return True

    def getHardwareList(self):
        try:
            self.__cur.execute(f"SELECT id, tech_name, tech_sn, tech_in, for_whom, tech_locate, tech_buisnes, input_date, input_coment FROM hardware ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []

    def getHardwareId(self, hardwareId):
        try:
            self.__cur.execute(f"SELECT id, tech_name, tech_sn, tech_in, for_whom, tech_locate, tech_buisnes, input_date, input_coment FROM hardware WHERE id = {hardwareId} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return (False, False)