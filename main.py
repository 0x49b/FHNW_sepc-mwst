import sys

mwst_country = {
    "DE": 0.16,
    "FR": 0.20,
    "HU": 0.27,
    "GR": 0.25,
    "GB": 0.195
}

discounts = {
    "1000": 0.03,
    "5000": 0.05,
    "7000": 0.07,
    "10000": 0.1,
    "15000": 0.15
}


def retailcal():
    number_products = int(sys.argv[1])
    price_product = float(sys.argv[2])
    tax_country = sys.argv[3]

    subtotal = number_products * price_product
    discount = calc_discount(subtotal)
    netto = subtotal - discount
    tax = round(calc_tax(netto, tax_country), 2)
    total = netto + (tax + 1)

    print("N° of Products %s " % number_products)
    print("Price per Product %s" % price_product)
    print("aTax Country %s" % tax_country)

    print("\nThank you for buying stuff at us. Your bill is:")
    print("\tprice for all items %s " % subtotal)
    print("\tdiscount on items %s" % discount)
    print("\tprice after discount %s" % netto)
    print("\ttax to pay %s" % tax)
    print("\ttotal to pay %s" % total)


def calc_tax(price, country) -> float:
    if country in mwst_country:
        return price * mwst_country[country]

    c_list = ""
    for country in mwst_country:
        c_list = c_list + country + " "

    print("Tax Country not in list, possible countries are %s " % c_list)
    sys.exit(1)


def calc_discount(total) -> float:
    discount_val = discounts["15000"]

    if 1000 < total < 4999:
        discount_val = discounts["1000"]
    elif 5000 < total < 6999:
        discount_val = discounts["5000"]
    elif 7000 < total < 9999:
        discount_val = discounts["7000"]
    elif 10000 < total < 49999:
        discount_val = discounts["10000"]

    return total * discount_val


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("argument mismatch. \n usage: python retailcal.py <N° of products> <Price per Product> <Tax Country>")
        sys.exit(1)
    retailcal()
