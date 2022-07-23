from sys import argv
import json
import random
import csv


class CurrencyExchange:
    json_file = 'config.json'
    csv_file = 'condition.csv'
    csv_field = ['course', 'available_balance_usd', 'available_balance_grn']
    available_balance_usd = None
    available_balance_grn = None

    def __init__(self):
        json_data = self.parse_json()
        self.course = json_data.get('course')
        self.hr_account = json_data.get('hr_account')
        self.usd_account = json_data.get('usd_account')
        self.d = json_data.get('d')
        self.set_available_balance_usd(self.hr_account, self.course)
        self.set_available_balance_grn(self.usd_account, self.course)

    @classmethod
    def set_available_balance_usd(cls, hr_account, course):
        cls.available_balance_usd = round(int(hr_account) / course, 2)

    @classmethod
    def set_available_balance_grn(cls, usd_account, course):
        cls.available_balance_grn = round(usd_account * course, 2)

    def next_current_course(self):
        self.course = round(random.uniform(self.course - self.d, self.course + self.d), 2)
        self.write_json()

    def buy_dollar(self, count):
        need_grivnas = round(count * self.course, 2)
        if self.hr_account < need_grivnas:
            print(f'UNAVAILABLE, REQUIRED BALANCE UAH {need_grivnas}, AVAILABLE {self.hr_account}')
            return
        self.hr_account -= need_grivnas
        self.hr_account = round(self.hr_account, 2)
        self.usd_account += count
        self.write_json()

    def buy_all_dollar(self):
        dif = round(self.hr_account - int(self.hr_account), 2)
        self.hr_account = dif
        self.usd_account += self.available_balance_usd
        self.write_json()

    def sell_dollar(self, count):
        if self.usd_account < count:
            print(f'UNAVAILABLE, REQUIRED BALANCE USD {count}, AVAILABLE {self.usd_account}')
            return
        self.usd_account -= count
        self.hr_account += round(count * self.course, 2)
        self.write_json()

    def sell_all_dollar(self):
        self.hr_account += self.available_balance_grn
        self.usd_account = 0
        self.write_json()

    def write_json(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.__dict__, f)

    def start_default(self):
        self.course = 26.00
        self.hr_account = 10000.00
        self.usd_account = 0.00
        self.d = 0.5
        self.write_json()

    @classmethod
    def parse_json(cls):
        f = open(cls.json_file)
        data = json.load(f)
        f.close()
        return data

    def write_syst_condition(self):
        data_dict = {'course': self.course, 'available_balance_usd': self.available_balance_usd,
                     'available_balance_grn': self.available_balance_grn}
        with open(self.csv_file, 'a', newline="") as f:
            writer = csv.DictWriter(f, self.csv_field)
            writer.writerow(data_dict)


def main():
    ex = CurrencyExchange()
    if len(argv) == 1:
        return
    if 'RATE' in argv:
        print(ex.course)
    if 'AVAILABLE' in argv:
        print(f'USD {ex.usd_account}, UAH{ex.hr_account}')
    if 'BUY' in argv:
        ex.buy_dollar(float(argv[2]))
    if 'SELL' in argv:
        ex.sell_dollar(float(argv[2]))
    if 'BUY_ALL' in argv:
        ex.buy_all_dollar()
    if 'SELL_ALL' in argv:
        ex.sell_all_dollar()
    if 'NEXT' in argv:
        ex.next_current_course()
    if 'RESTART' in argv:
        ex.start_default()
    ex.write_syst_condition()


if __name__ == '__main__':
    main()
