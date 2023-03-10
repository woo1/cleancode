# 독립성
def calc_price(base_price: float, tax: float, discount: float) -> float:
    return (base_price * (1+tax)) * (1 - discount)

def show_price(price: float) -> str:
    return "$ {0:,.2f}".format(price)

def str_final_price(base_price: float, tax: float, discount: float, fmt_func=str)->str:
    return fmt_func(calc_price(base_price, tax, discount))

print(str_final_price(10, 0.2, 0.5))
print(str_final_price(1000, 0.2, 0))
print(str_final_price(1000, 0.2, 0.1, fmt_func=show_price))
