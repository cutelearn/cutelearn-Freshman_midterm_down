'''
替代役各梯次受訓役男諮商來源分析統計表
'''
import csv
import sqlite3
import os

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class MalesubStitute:
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.Echelon = []
        self.Mental = []
        self.SelfHelp = []
        self.Total = []
        self.create_table()

    def read_csv(self):
        '''
        讀取csv文件
        '''
        with open(self.filename,encoding=self.encoding) as f:
            reader = csv.reader(f)
            listreader = list(reader)
            csvData = listreader[2:]
            for row in csvData:
                self.Echelon.append(row[0])
                self.Mental.append(row[2])
                self.SelfHelp.append(row[3])
                self.Total.append(row[4])
        self.write_db()

    def create_table(self):
        '''
        建立資料表
        '''
        if os.path.exists('unit2/替代役各梯次受訓役男諮商來源分析統計表.db'):
            print('資料庫已存在')
        else:
            print('資料庫不存在，建立資料庫')
            conn = sqlite3.connect('unit2/替代役各梯次受訓役男諮商來源分析統計表.db')
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS "替代役各梯次受訓役男諮商來源分析統計表" (
                    "梯次" INTEGER,
                    "身心狀況電腦適性測驗" INTEGER,
                    "主動求助" INTEGER,
                    "總諮商人數" INTEGER
                )
            ''')
            conn.commit()
            conn.close()

    def write_db(self):
        '''
        寫入資料庫
        '''
        conn = sqlite3.connect('unit2/替代役各梯次受訓役男諮商來源分析統計表.db')
        c = conn.cursor()
        for i in range(len(self.Echelon)):
            c.execute('''
                INSERT INTO 替代役各梯次受訓役男諮商來源分析統計表
                VALUES (?,?,?,?)
            ''',(self.Echelon[i], self.Mental[i], self.SelfHelp[i], self.Total[i]))
        conn.commit()
        conn.close()

    def read_db(self):
        '''
        讀取資料庫
        '''
        conn = sqlite3.connect('unit2/替代役各梯次受訓役男諮商來源分析統計表.db')
        c = conn.cursor()
        c.execute('''
            SELECT * FROM 替代役各梯次受訓役男諮商來源分析統計表
        ''')
        result = c.fetchall()
        conn.close()
        return result

    def draw(self):
        '''
        圖表繪製
        '''
        result = self.read_db()
        Echelon = []
        Mental = []
        SelfHelp = []
        Total = []

        for row in result:
            Echelon.append(row[0])
            Mental.append(row[1])
            SelfHelp.append(row[2])
            Total.append(row[3])

        fig, axs = plt.subplots(2, 2, figsize=(12, 10), dpi=100)

        axs[0, 0].plot(Echelon, Mental, c='red', label='Mental')
        axs[0, 0].set_xlabel('Echelon', fontsize=16)
        axs[0, 0].set_ylabel("", fontsize=16)
        axs[0, 0].tick_params(axis='both', which='major', labelsize=12)
        axs[0, 0].yaxis.set_major_locator(MaxNLocator(integer=True))
        axs[0, 0].legend()

        axs[0, 1].plot(Echelon, SelfHelp, c='blue', label='SelfHelp')
        axs[0, 1].set_xlabel('Echelon', fontsize=16)
        axs[0, 1].set_ylabel("", fontsize=16)
        axs[0, 1].tick_params(axis='both', which='major', labelsize=12)
        axs[0, 1].yaxis.set_major_locator(MaxNLocator(integer=True))
        axs[0, 1].legend()

        axs[1, 0].plot(Echelon, Total, c='green', label='Total')
        axs[1, 0].set_xlabel('Echelon', fontsize=16)
        axs[1, 0].set_ylabel("", fontsize=16)
        axs[1, 0].tick_params(axis='both', which='major', labelsize=12)
        axs[1, 0].yaxis.set_major_locator(MaxNLocator(integer=True))
        axs[1, 0].legend()

        axs[1, 1].axis('off')

        plt.show()


def main():
    '''
    主函式
    '''
    MalesubStitute_data = MalesubStitute('unit2/8411152e57c2133b.csv')
    MalesubStitute_data.read_csv()
    MalesubStitute_data.draw()


if __name__ == '__main__':
    main()
