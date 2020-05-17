# initial information
# open from 8:00 till 22:00
# discounts: -33% & -50% if almost past exp.date -35%
# (exp discount can go on top of regular discount!)
# start amount is init amount
# produce is sold at end of every hour.
# cannot sell more then available
# random  regular sell counter for every product is between 25%-75%
# random discount sell counter for every product is between 50%-100%
# random exp.discount sell counter also between 50%-100%
# orders arrive next day 12 afternoon, arrived means available!
# 2 random products on sale every 3 days, products cannot be on sale twice in a row.
# exp. date is delivery day + days to expire
# if exp.date is expired throw out
# order new produce if less then a certain %. order 100%?

# rapports:
# hourly: how much produce left, how much is almost* exp.date,
# how  much is exp.date, how much money made.
# *almost is relative because for something that lasts 10 days alsmost is 1 maybe 2 days for
# something of 365 days almost is a week or two.
# daily: per product: how much was made on this, was it on sale? what kind of sale?
# daily: how much dit we pay for the products, how much did we make on the products.
# daily: what was ordered, how much and how much was that.
# weekly: how much profit/loss last week.
# weekly: how much was lost on expired produce.
# ALL OF THE ABOVE MUST BE REPORTED IN .TXT FILES PER DAY THAT INCLUDES HOURLY LOGS,
# IN A WEEK REPORT THAT INCLUDES DAY REPORTS AND WEEK REPORT.


products = [
    {"name": "apple", "keeps_days": 10, "buy": 0.1, "sell": 0.7, "order_size": 200},
    """ {
        "name": "toothpaste",
        "keeps_days": 365,
        "buy": 1.80,
        "sell": 2.30,
        "order_size": 100,
    },
    {"name": "carrot", "keeps_days": 14, "buy": 0.4, "sell": 1, "order_size": 200},
    {"name": "avocado", "keeps_days": 6, "buy": 1, "sell": 1.20, "order_size": 150},
    {"name": "toilet paper", "keeps_days": 365, "buy": 2, "sell": 4, "order_size": 100},
    {
        "name": "salmon",
        "keeps_days": 4,
        "buy": 1.7,
        "sell": 4,
        "last_day_discount": True,
        "order_size": 50,
    },
    {
        "name": "quinoa salad",
        "keeps_days": 4,
        "buy": 2.3,
        "sell": 4.5,
        "last_day_discount": True,
        "order_size": 50,
    },
    {
        "name": "frozen pizza",
        "keeps_days": 150,
        "buy": 0.7,
        "sell": 2.5,
        "order_size": 100,
    },
    {"name": "cola", "keeps_days": 365, "buy": 0.7, "sell": 2.5, "order_size": 200},
    {
        "name": "croissant",
        "keeps_days": 1,
        "buy": 0.7,
        "sell": 1,
        "last_hour_discount": True,
        "order_size": 50,
    },
    {
        "name": "bread",
        "keeps_days": 1,
        "buy": 0.4,
        "sell": 1.2,
        "last_hour_discount": True,
        "order_size": 50,
    }, """,
]

# test
