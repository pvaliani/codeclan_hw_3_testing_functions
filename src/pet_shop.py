# WRITE YOUR FUNCTIONS HERE

#function to get the pet shop name
def get_pet_shop_name(input_dict):
    return input_dict["name"]

#function to get the total cash stored in dictionary
def get_total_cash(input_dict):
    return input_dict["admin"]["total_cash"]

#function to add or remove cash

def add_or_remove_cash(input_dict, input_cash):
    current_cash = get_total_cash(input_dict)
    new_cash = 0

    if input_cash >= 0:
        new_cash = current_cash + input_cash
    else:
        new_cash = current_cash - abs(input_cash)
    
    input_dict["admin"]["total_cash"] = new_cash

#function to get pets sold
  



    # return total_cash
# def add_or_remove_cash(input_dict, input_int):
#     current_value = get_total_cash(input_dict)
#     new_value = 0
#     if input_int >= 0:
#          new_value = current_value + input_int
#     else:
#          new_value = current_value - abs(input_int) # Make input_int an absolute number.
#     input_dict["admin"]["total_cash"] = new_value

    


