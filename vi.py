#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_per_adult=no_of_adults*(37550.0)+(no_of_adults*(37550.0)*0.07)
    rate_per_children=no_of_children*(rate_per_adult*(1/3))+(no_of_children*(rate_per_adult*(1/3))*0.07)
    total_ticket_cost=(rate_per_children+rate_per_adult)-((rate_per_adult+rate_per_children)*0.1)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)