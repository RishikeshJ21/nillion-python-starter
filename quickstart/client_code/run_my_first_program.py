from nada_dsl import *

def nada_main():
    # Define parties
    cinema = Party(name="Cinema")
    user = Party(name="User")

    # Define ticket options with their details
    movie_options = {
        "Avengers: Endgame": {
            "floor_price": 500,
            "balcony_price": 600
        },
        "Joker": {
            "floor_price": 450,
            "balcony_price": 550
        },
        "Inception": {
            "floor_price": 480,
            "balcony_price": 580
        }
    }

    # Input for movie selection
    movie_choice = Input(name="movie_choice", party=user, datatype=str,
                         domain=["Avengers: Endgame", "Joker", "Inception"])

    # Input for ticket type selection
    ticket_type = Input(name="ticket_type", party=user, datatype=str, domain=["floor", "balcony"])

    # Input for user's basic information
    user_name = Input(name="user_name", party=user, datatype=str)
    user_age = Input(name="user_age", party=user, datatype=int)
    user_email = Input(name="user_email", party=user, datatype=str)

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

    # Retrieve selected movie details
    selected_movie = Case(
        movie_choice == "Avengers: Endgame", movie_options["Avengers: Endgame"],
        movie_choice == "Joker", movie_options["Joker"],
        movie_choice == "Inception", movie_options["Inception"]
    )

    # Calculate ticket price after discount
    ticket_price = If(ticket_type == "floor", selected_movie["floor_price"], selected_movie["balcony_price"])
    discounted_price = ticket_price * (1 - discount_rate)

    # Output the discounted price to the user
    return Output(discounted_price, "discounted_price", party=user)

# Create the NADA program
create_nada_program(nada_main)
