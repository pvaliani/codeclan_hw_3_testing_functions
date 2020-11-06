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

#function to retrieve pets sold

def get_pets_sold(input_dict):
    return input_dict["admin"]["pets_sold"]

#function to increase pets sold

def increase_pets_sold(input_dict, increment):
    new_value = 0

    if increment >0:
        new_value = get_pets_sold(input_dict) + increment
    
    input_dict["admin"]["pets_sold"] = new_value

#function to get stock count 

# def get_stock_count(input_dict):
#     for pet in input_dict:
#         return len(input_dict["pets"])


#function to get customer cash
def get_customer_cash(input_list_of_dict):
    return input_list_of_dict["cash"]


#function to remove customer cash

def remove_customer_cash(input_list_of_dict, input_cash):

    if input_cash >0:
        new_cash = get_customer_cash(input_list_of_dict) - abs(input_cash)
    
    input_list_of_dict["cash"] = new_cash

    


