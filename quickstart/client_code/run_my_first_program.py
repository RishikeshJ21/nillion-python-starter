from nada_dsl import *

def nada_main():
  # Defining a party
  party1 = Party(name="Party1")

  # Secret integer inputs for the party
  my_ini1 = SecretInteger(Input(name="my_init1", party=party1))
  my_ini2 = SecretInteger(Input(name="my_init2", party=party1))

  # Example operation on the secret integers (e.g., addition)
  sum_result = my_ini1 + my_ini2

  # Output the result
  return [Output(sum_result, "sum_output", party1)]

# Create the NADA program
create_nada_program(nada_main)
