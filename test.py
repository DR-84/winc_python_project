""" for product in self.products:
            order_size = product["order_size"] - product["sold_per_hour"][i]
            name = product["name"].upper()
            if product["almost_expired"] is False and product["is_expired"] is False:
                is_expired = f"{name} Exp.date is ok!"
            if product["almost_expired"] and product["is_expired"] is False:
                is_expired = f"{name} Almost expired!"
            if product["is_expired"] and product["almost_expired"]:
                is_expired = f"{name} 100% EXPIRED!"
            revenue_this_hour = round(product["sell"] * product["sold_per_hour"][i], 2)
            print(
                f"Name:{name}. Items left:{order_size}. {is_expired}. Made: €{revenue_this_hour}."
            )
 """
