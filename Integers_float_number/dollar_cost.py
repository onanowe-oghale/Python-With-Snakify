# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N.
# It should print two numbers: total cost in dollars and cents.


#--------------

dollar = int(input('How many dollar does the cake cost: '))
cents = int(input('How many cents does the cake cost: '))
cake_numbers = int(input('How many cakes do you wish to get: '))
#calculate the total value in cents
dollar_to_cent = dollar * 100 #100 dollars make a cent
total_value = dollar_to_cent + cents #gives total cents value
cost_total_in_cents = cake_numbers * total_value
#because 100 cents make a dollar we say
actual_dollar_value = cost_total_in_cents // 100
remaining_cent_value = cost_total_in_cents % 100
print(f'The cost for {cake_numbers} cakes will be ${actual_dollar_value} .{remaining_cent_value} cents')