from dic import data

def totaldeaths(country):
    total = 0

    for year, value in data["Deaths by Cause"][country].items():
        for death in value["Deaths"].values():
            total += death
            total += value["Number of executions"]

    return f"Total deaths from {country} is {total}"





def Alzheimer(alzheimer):
    
    total = 0
    
    if alzheimer.upper() == "YES":
        for key, value in data["Deaths by Cause"].items():
            
            for year, deaths in value.items():
                total += deaths["Deaths"]["Alzheimer"]
            
    return f"Total deaths from Alzheimer is {total}"


def Parkinson(parkinson):
    
    total = 0
    
    if parkinson.upper() == "YES":
        for key, value in data["Deaths by Cause"].items():
            
            for year, deaths in value.items():
                total += deaths["Deaths"]["Parkinson"]
            
    return f"Total deaths from Parkinson is {total}"



def Nutritional_deficiencies(nutritional_deficiencies):
    
    total = 0
    
    if nutritional_deficiencies.upper() == "YES":
        for key, value in data["Deaths by Cause"].items():
            
            for year, deaths in value.items():
                total += deaths["Deaths"]["Nutritional deficiencies"]
            
    return f"Total deaths from Nutritional deficiencies is {total}"


def Malaria(malaria):
    
    total = 0
    
    if malaria.upper() == "YES":
        for key, value in data["Deaths by Cause"].items():
            
            for year, deaths in value.items():
                total += deaths["Deaths"]["Malaria"]
            
    return f"Total deaths from Malaria is {total}"


def Drowning(drowning):
    
    total = 0
    
    if drowning.upper() == "YES":
        for key, value in data["Deaths by Cause"].items():
            
            for year, deaths in value.items():
                total += deaths["Deaths"]["Drowning"]
            
    return f"Total deaths from Drowning is {total}"


def Years(mini,maxi):
    
    total = 0
    
    for key, value in data["Deaths by Cause"].items():
        
        for year, details in value.items():
            
            if mini <= year <= maxi:
                
                for death in details["Deaths"].values():
                    total += death
                
                total += details["Number of executions"]
                
    return f"Total number of deaths from {mini} to {maxi} is {total}"




