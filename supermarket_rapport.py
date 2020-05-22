import datetime
import supermarket_data
import random


class Hours:
    def __init__(self, opening, closing, delivery):
        self.opening = opening
        self.closing = closing
        self.delivery = delivery

    def hours_open(self):
        hours = self.closing - self.opening
        return hours


class Product:
    def __init__(self, product, sales_percentage):
        self.product = product
        self.sales_percentage = sales_percentage

    def get_product_name(self):
        for items in self.product:
            return items["name"]

    def get_product_value_by_keyname(self, key):
        for items in self.product:
            return items[key]

    def amount_sold_generator(self, i):
        order_size = self.product[i]["order_size"]
        random_percentage = (
            random.randint(self.sales_percentage[0], self.sales_percentage[1]) / 100
        )
        sold_items = order_size * random_percentage
        return sold_items

    def items_sold_per_item(self):
        i = 0
        for item in self.product:
            item["items_sold"] = int(products.amount_sold_generator(i))
            i += 1
        return item

    def sold_per_hour_per_item(self):
        for item in self.product:
            item["sold_per_hour"] = products.randomize_hour_sales(item["items_sold"])
        return item

    def randomize_hour_sales(self, end):
        numlist = []
        for hour in range(important_hours.hours_open() - 1):
            numlist.append(random.randint(0, end))
        sum_numlist = sum(numlist)
        total_makes_one = [i / sum_numlist for i in numlist]
        total_makes_end_num = [i * end for i in total_makes_one]
        round_nums_in_list = [int(i) for i in total_makes_end_num]
        sum_rounded_nums = sum(round_nums_in_list)
        round_nums_in_list.append(end - sum_rounded_nums)
        return round_nums_in_list

    def update_order_size(self, i):
        return self.product[i]["order_size"] - self.product[i]["sold_per_hour"][0]


class Reports:
    def __init__(self, products):
        self.products = products

    def hourly_report(self, i):
        for product in self.products:
            name = product["name"]
            sold = product["items_sold"]
            sold_per_hour = product["sold_per_hour"]
            product["order_size"] = product["order_size"] - product["sold_per_hour"][i]
            # almost expired,
            # is expired
            revenue_this_hour = round(product["sell"] * product["sold_per_hour"][i], 2)
            print(
                "HOUR #",
                i + 1,
                "NAME:",
                name,
                "SOLD:",
                sold,
                "SOLD THIS HOUR:",
                sold_per_hour[i],
                "ITEMS LEFT:",
                product["order_size"],
                "MADE €",
                revenue_this_hour,
            )

    def daily_report(self):
        return

    def weekly_report(self):
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


sales_percentage = 25, 75
products = Product(supermarket_data.products, sales_percentage)
important_hours = Hours(8, 22, 12)
start_date = datetime.datetime(2020, 1, 6, 6)
end_date = datetime.datetime(2020, 1, 6, 23)
reports = Reports(supermarket_data.products,)


def execute_hourly(start, finish):
    while finish > start:
        start = start + datetime.timedelta(hours=1)
        yield start


for hour in execute_hourly(start_date, end_date):
    if start_date == hour - datetime.timedelta(hours=1):
        print("INITIALIZED ORDER SIZE ROBOT NUCLEAR CONTINUUM EXPLODER FUSION!!")
    if hour.hour == 7:
        i = 0
        products.items_sold_per_item()
        products.sold_per_hour_per_item()
        print("its 7 in the morning")
    if hour.hour > 8 and hour.hour < 23:
        print("--------------------------------------------------")
        print(f"print {hour.hour} o' clock report")
        reports.hourly_report(i)
        i += 1
    if hour.hour == 12:
        print("--------------------------------------------------")
        print(f"it's {hour.hour} o'clock, delivery is here!")
    if hour.hour == 22:
        print("--------------------------------------------------")
        print(f"it's {hour.hour} o'clock, end of day {hour} report")
