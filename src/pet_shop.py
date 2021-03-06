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

    if increment>0:
        new_value = get_pets_sold(input_dict) + increment
    
    input_dict["admin"]["pets_sold"] = new_value

#function to get stock count 

def get_stock_count(input_dict_of_list):
    return len(input_dict_of_list["pets"])

#function to get pets by their breed

#define a function which takes an input dictionary of lists and a breed of cat
def get_pets_by_breed(input_dict_of_list, breed):
 
    #create an empty list to store the results of breed
    results = []
    #for each iteration in the list of the values associated with the "pets" key
    for pet in input_dict_of_list["pets"]:
    #if the iteration pointing to 'breed' in the pet dictionaries equals the breed
    #input in the function
        if pet['breed'] == breed:
    #append the result to the empty results list
            results.append(pet)
    #else if the iteration pointing to the 'breed' in the pet dictionaries is empty
        elif pet['breed'] == "":
    #append the result to the results list - ***may be better do this as an "empty" return with a message
            results.append(pet)
    return results

#function to find pets by name and return None if there is no pet

def find_pet_by_name(input_dict_of_list, pet_name):
    #initialise found_pet to None and then
    found_pet = None
    #for each iteration in the list (which is the dictionary value of the "pet" key)
    for pet in input_dict_of_list["pets"]:
    #if the iteration with the key "name" equals the pet_name input to the function
        if pet["name"] == pet_name:
    #set found_pet to this particular iteration and return found_pet with the new value
            found_pet = pet
            return found_pet
    #else if the value of the iteration through the name key equals 0 i.e there is no name, return None
        elif pet["name"] == 0:
            return None

# function to remove pet by name in the list of dictionariess

def remove_pet_by_name(input_dict_of_list, pet_name):
    for pet in input_dict_of_list["pets"]:
        if pet["name"] == pet_name:
            input_dict_of_list["pets"].remove(pet)


# function to add pet to test stock

def add_pet_to_stock(input_dict_of_list, new_pet_dict):
    updated_stock = input_dict_of_list["pets"].append(new_pet_dict)
    return updated_stock

        


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
    return len(input_list_of_dict["pets"])


# function to add a number of pets to a customer
def add_pet_to_customer(input_list_of_dict, customers):
    input_list_of_dict["pets"].append(customers)

#function to determine if customer can afford a pet - if they can, return true.
#if they cannot then return false. Or if the price and customer cash match exactly return True.

def customer_can_afford_pet(input_list_of_dict, new_pet):
    #if the value of cash in the customer list if >= the new_pet price return true
    if input_list_of_dict["cash"] >= new_pet["price"]:
        return True
    else: 
        return False

#function which determines whether to sell a pet to a customer using previously defined functions

def sell_pet_to_customer(petshop_dict, input_pet, input_customer):
    if input_pet != None:
        if customer_can_afford_pet(input_customer, input_pet) == True:
            remove_customer_cash(input_customer, input_pet["price"])
            add_or_remove_cash(petshop_dict, input_pet["price"])
            add_pet_to_customer(input_customer, input_pet)
            remove_pet_by_name(petshop_dict, input_pet)
            increase_pets_sold(petshop_dict, 1)


1


