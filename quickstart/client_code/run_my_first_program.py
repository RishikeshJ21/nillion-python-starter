from nada_dsl import *

def nada_main():
    # Define parties
    cinema = Party(name="Cinema")
    user = Party(name="User")

    # Define ticket options
    floor_ticket_price = 500
    balcony_ticket_price = 600

    # Input for ticket selection
    ticket_type = Input(name="ticket_type", party=user, datatype=str, domain=["floor", "balcony"])

    # Coupon codes and discounts
    coupon_discounts = {
        "HHGOA": 0.2,   # 20% discount
        "NillionRocks": 0.25   # 25% discount
    }

    # Input for coupon code
    coupon_code = Input(name="coupon_code", party=user, datatype=str, domain=["HHGOA", "NillionRocks"])

    # Secure computation to determine discount based on coupon code
    discount_rate = If(coupon_code == "HHGOA", coupon_discounts["HHGOA"],
                       If(coupon_code == "NillionRocks", coupon_discounts["NillionRocks"], 0.0))

    # Calculate ticket price after discount
    ticket_price = If(ticket_type == "floor", floor_ticket_price, balcony_ticket_price)
    discounted_price = ticket_price * (1 - discount_rate)

    # Output the discounted price to the user
    return Output(discounted_price, "discounted_price", party=user)

# Create the NADA program
create_nada_program(nada_main)
