import datetime
import supermarket_data
import random


class Hours:
    def __init__(self, opening, closing, delivery):
        self.opening = opening
        self.closing = closing
        self.delivery = delivery


class Product:
    def __init__(self, product):
        self.product = product

    def get_product_name(self):
        return self.product["name"]

    def get_product_value_by_keyname(self, key):
        return self.product[key]

    def amount_sold_generator(self, from_percentage, till_percentage):
        return


class Reports:
    def __init__(self, product, sales, orders):
        self.product = product
        self.sales = sales
        self.orders = orders

    def hourly_report(self, product, sales):
        return

    def daily_report(self, product, sales):
        return

    def weekly_report(self, product, sales):
        return


class GenerateTxtReport:
    def __init__(self):
        return


class OnSale:
    def __init__(self, product):
        return

    def random_33_off(self):
        # if sale item in list date is >= 3 days ago
        # if is_third_off or is_half_off = False
        # sale random product from lnt(products) --> is_third_off = True
        # on_sale_price = amount * 0.66
        # date_third_off = todaydate
        return

    def random_50_off(self):
        # if date is 3 days ago
        # if is_third_off or is_half_off  = False
        # sale random product from lnt(products) --> is_half_off = True
        # on_sale_price = amount * 0.50
        # date_half_off = todaydate
        return

    def almost_expired_sale(self):
        # if date is 1 days from today
        # expire_date_sale = True
        # date_half_off = todaydate
        # on_sale_price = (amount * 0.65) or (on_sale_price * 0.65)
        return


class Order:
    def __init__(self):
        return


albert_van_den_broek = Hours(8, 22, 12)
start_date = datetime.datetime(2020, 1, 6, 8)
end_date = datetime.datetime(2020, 1, 7, 8)


def report_hourly(start, finish):
    while finish > start:
        start = start + datetime.timedelta(hours=1)
        yield start


for hour in report_hourly(start_date, end_date):
    if hour.hour > 8 and hour.hour < 22:
        print(f"print {hour.hour} o' clock report")
    if hour.hour == 12:
        print(f"it's {hour.hour} o'clock, delivery is here!")
    if hour.hour == 22:
        print(f"it's {hour.hour} o'clock, end of day report")


""" def random_subtractor_per_hour(subtractable_amount, hours):
    subtracted = []
    large_num = subtractable_amount / 2
    while hours != 0:
        num = random.randint(0, large_num)
        if subtractable_amount != 0 or subtractable_amount > num:
            subtracted.append(num)
            subtractable_amount = subtractable_amount - num
            hours -= 1
        else:
            subtracted.append(subtractable_amount)
            subtractable_amount - subtractable_amount
            hours -= 1

        print(subtracted)


random_subtractor_per_hour(100, 12) """
