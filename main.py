import os
import sqlite3

def modifyLocalStorageDB(path):
    print(path)
    if path.endswith("db"):
        print("识别成功")
        # 连接到数据库
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        
        result = cursor.execute("SELECT value from LocalStorage WHERE key = 'CustomFrameRate'").fetchone()
        conn.commit()
        if(result):
            print("执行成功")
             # 执行修改语句
            cursor.execute(f"UPDATE LocalStorage SET value = 3 WHERE key = 'CustomFrameRate'")
            conn.commit()
            # 关闭数据库
        else:
            print("文件不正确")
            print("执行失败")
        cursor.close()
        conn.close()

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(), 'data.txt'), 'r', encoding="utf8") as file:
        # 读取文件的第一行
        db_directory = file.readline()
        print(db_directory)
        modifyLocalStorageDB(db_directory)