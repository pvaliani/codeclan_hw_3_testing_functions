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

def get_stock_count(input_dict_of_list):
    return len(input_dict_of_list["pets"])

#function to get pets by their breed

def get_pets_by_breed(input_dict_of_list, breed):
    results = []
    for pet in input_dict_of_list["pets"]:
        if pet['breed'] == breed:
            results.append(pet)
        elif pet['breed'] == "":
            results.append(pet)
    return results

#function to find pets by name and return None if there is no pet

def find_pet_by_name(input_dict_of_list, pet_name):
    found_pet = None

    for pet in input_dict_of_list["pets"]:
        if pet["name"] == pet_name:
            found_pet = pet
            return found_pet
        elif pet["name"] == 0:
            return None

# function to remove pet by name in the list of dictionariess

def remove_pet_by_name(input_dict_of_list, pet_name):
    for pet in input_dict_of_list["pets"]:
        if pet["name"] == pet_name:
            input_dict_of_list["pets"].remove(pet)
          


        


# def find_pet_by_name(shop_dict, pet_name):
#     found_pet = None
#     for pet in shop_dict["pets"]:
#         if pet["name"] == pet_name:
#             found_pet = pet
#             return found_pet






#function to get customer cash
def get_customer_cash(input_list_of_dict):
    return input_list_of_dict["cash"]


#function to remove customer cash

def remove_customer_cash(input_list_of_dict, input_cash):

    if input_cash >0:
        new_cash = get_customer_cash(input_list_of_dict) - abs(input_cash)
    
    input_list_of_dict["cash"] = new_cash

# function to retrieve customers pet count

def get_customer_pet_count(input_list_of_dict):
    
    if input_list_of_dict["pets"] == []:
        return 0
    else:
        return input_list_of_dict["pets"]

# function to add a number of pets to a customer

def add_pet_to_customer(input_list_of_dict, pet_num):

    for pet in input_list_of_dict["pets"]:
        if pet_num > 0:
            new_pets = input_list_of_dict["pets"] + pet_num
        elif input_list_of_dict["pets"] == []:
            return 0
        
        input_list_of_dict["pets"] = new_pets

    


