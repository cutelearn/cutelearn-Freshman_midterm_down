'''
股票数据分析
'''
import csv
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, filename, encoding='big5'):
        self.filename = filename
        self.encoding = encoding
        self.dates = []
        self.hight_prices = []
        self.low_prices = []
        self.closing_prices = []
        self.read_csv()

    def read_csv(self):
        '''
        讀取csv文件
        '''
        with open(self.filename, encoding=self.encoding) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            print(header_row)
            listreader = list(reader)
            csvData = listreader[1:-5]
            for row in csvData:
                self.dates.append(row[0])
                self.hight_prices.append(float(row[4]))
                self.low_prices.append(float(row[5]))
                self.closing_prices.append(float(row[6]))

    def draw(self):
        '''
        繪製圖形
        '''
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(self.dates, self.hight_prices, c='red', label='hight')
        plt.plot(self.dates, self.low_prices, c='blue', label='low')
        plt.plot(self.dates, self.closing_prices, c='green', label='closing')
        plt.legend()
        plt.title("stock", fontsize=24)
        plt.xlabel('date', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("prices", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

def main():
    '''
    主函式
    '''
    stock_data = StockData('unit1/STOCK_DAY_6579_201903.csv')
    stock_data.draw()

if __name__ == '__main__':
    main()
