import pandas as pd
import numpy as np
import re

# Read in pulled and formatted data

df = pd.read_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/formated_data.csv', encoding='utf-8')

# Create a Dictionary of All Job Types

job_types = {

    (r'(Crime Scene Clean)','Non-profit/Government'),     
    (r'(Volunteer)', 'Non-profit/Government'),     
    (r'(Dispatch)', 'Non-profit/Government'), 
    (r'(Dispenser)', 'Non-profit/Government'), 
    (r'(Disab)', 'Disability'), 
    
    (r'(accounting)','Accounting/Finance'),
    (r'(Controller)','Accounting/Finance'),
    (r'(tax)','Accounting/Finance'),
    (r'(accounts)','Accounting/Finance'),
#    (r'(pay)','Accounting/Finance'),
#    (r'(ar )','Accounting/Finance'),
    (r'(audit)','Accounting/Finance'),    
    (r'(accountant)', 'Accounting/Finance'), 
    (r'(finance)', 'Accounting/Finance'), 
    (r'(bookkeep)', 'Accounting/Finance'), 

    (r'(tutor)','Education'),        
    (r'(Career Coach)','Education'),    
    (r'(instructor)','Education'),
    (r'(teacher)','Education'),
    (r'(teacher)','Education'),
    
    (r'(legal)', 'Legal/Architect'),     
    (r'(Architect)','Legal/Architect'),    
    (r'(attorney)','Legal/Architect'),
    (r'(lawyer)','Legal/Architect'),
    
    (r'(analy)', 'Analyst'),    
    (r'(system)', 'Systems/Software'), 
    (r'(programmer)','Systems/Software'),
    (r'(mobile)', 'Systems/Software'),
    (r'(developer)', 'Systems/Software'), 
    (r'(develop)', 'Systems/Software'),     
    (r'(software)', 'Systems/Software'), 
        
    (r'(equip)', 'Manufacturing'),     
    (r'(assemb)','Manufacturing'),
    (r'(Build)', 'Manufacturing'), 
    (r'(fabricat)', 'Manufacturing'), 
    (r'(machin)', 'Manufacturing'), 
    (r'(assemb)','Manufacturing'),
    (r'(foreman)', 'Manufacturing'), 
    (r'(operator)', 'Manufacturing'), 
    (r'(handler)', 'Manufacturing'), 
    (r'(installer)', 'Manufacturing'), 
    (r'(manufacture)', 'Manufacturing'), 
    (r'(metal)', 'Manufacturing'), 
    (r'(product)', 'Manufacturing'), 
    (r'(production)', 'Manufacturing'), 
    
    (r'(marketing)', 'Business'), 
    (r'(project manager)','Business'),
    (r'(product manager)','Business'),    
    (r'(busi)', 'Business'), 
    (r'(bank)', 'Business'), 
    (r'(collections)', 'Business'), 
    (r'(buy)', 'Business'), 
    (r'(human res)', 'Business'), 
    (r'(hr*. rep)', 'Business'), 
    (r'(Lender)', 'Business'), 
    (r'(Loan)', 'Business'), 
    (r'(credit)', 'Business'),   
    (r'(Compli)', 'Business'), 
    (r'(Business Dev)', 'Business'), 
    (r'(estimat)', 'Business'), 
#    (r'(executive)', 'Business'),
    (r'(project)', 'Business'), 
    (r'(quality)', 'Business'), 
    (r'(teller)', 'Business'), 
    (r'(human rec)', 'Business'), 
    (r'(scheduler)', 'Business'), 
    (r'(Business*.operation)', 'Business'), 
    
    (r'(diesel)', 'Auto'),         
    (r'(car )', 'Auto'),
    (r'(automotive)', 'Auto'), 
    (r'(auto)', 'Auto'), 
    (r'(mechanic)', 'Auto'), 
    (r'(mechanical)', 'Auto'),     
    
    (r'(ground)', 'Laborer'), 
    (r'(porter)', 'Laborer'), 
    (r'(farm)','Laborer'),    
    (r'(Event S)', 'Laborer'), 
    (r'(carpenter)', 'Laborer'), 
    (r'(flag)', 'Laborer'), 
    (r'(help wanted)', 'Laborer'), 
    (r'(Loader)', 'Laborer'), 
    (r'(pipe)', 'Laborer'), 
    (r'(crew)', 'Laborer'), 
    (r'(labor)', 'Laborer'), 
    (r'(laborer)', 'Laborer'), 
    (r'(landscape)', 'Laborer'), 
    (r'(Sanitation)', 'Laborer'), 
    (r'(lawn)', 'Laborer'), 
    (r'(lead)', 'Laborer'),
    (r'(mover)', 'Laborer'), 
    (r'(operation)', 'Laborer'), 
    (r'(cement)', 'Laborer'), 
    (r'(forest)', 'Laborer'), 
    (r'(Massage)', 'Laborer'), 
    (r'(yard)', 'Laborer'), 
    
    (r'(host)','Restaurant/Bar'),        
    (r'(dish)','Restaurant/Bar'),    
    (r'(bake)','Restaurant/Bar'),
    (r'(expo)','Restaurant/Bar'),
    (r'(counter)','Restaurant/Bar'),
    (r'(foh)','Restaurant/Bar'),    
    (r'(bar)','Restaurant/Bar'),
    (r'(wait)','Restaurant/Bar'),
    (r'(kitchen)','Restaurant/Bar'),
    (r'(drink)','Restaurant/Bar'),    
    (r'(Breakfast)','Restaurant/Bar'),    
    (r'(banquet)', 'Restaurant/Bar'), 
    (r'(bartender)', 'Restaurant/Bar'),     
    (r'(busser)', 'Restaurant/Bar'),     
    (r'(chef)', 'Restaurant/Bar'), 
    (r'(Cocinero)', 'Restaurant/Bar'), 
    (r'(cook)', 'Restaurant/Bar'), 
    (r'(Concessionist)', 'Restaurant/Bar'), 
    (r'(Culinary)', 'Restaurant/Bar'), 
    (r'(Concierge)', 'Restaurant/Bar'), 
    (r'(Deli )', 'Restaurant/Bar'), 
    (r'(Delivery Driver)', 'Restaurant/Bar'), 
    (r'(Concessionist)', 'Restaurant/Bar'), 
    (r'(Barista)', 'Restaurant/Bar'),     
    (r'(food)', 'Restaurant/Bar'), 
    (r'(meat)', 'Restaurant/Bar'), 
    (r'(dishwasher)', 'Restaurant/Bar'), 
    (r'(front)', 'Restaurant/Bar'),     
    (r'(kitchen)', 'Restaurant/Bar'), 
    (r'(cater)', 'Restaurant/Bar'), 
    (r'(line)', 'Restaurant/Bar'),
    (r'(restaurant)', 'Restaurant/Bar'), 
    (r'(froze)', 'Restaurant/Bar'), 
    (r'(dining)', 'Restaurant/Bar'), 
    (r'(pizza)', 'Restaurant/Bar'), 
    (r'(prep)', 'Restaurant/Bar'), 
    (r'(hotel)', 'Restaurant/Bar'), 
    (r'(sandwich)', 'Restaurant/Bar'), 
    (r'(server)', 'Restaurant/Bar'), 
    (r'(sous)', 'Restaurant/Bar'), 
    (r'(subway)', 'Restaurant/Bar'),      
          
    (r'(admin)','Admin and Office'),
    (r'(recept)','Admin and Office'),
    (r'(Secretary)','Admin and Office'),     
    (r'(desktop)', 'Admin and Office'), 
    (r'(front desk)', 'Admin and Office'), 
    (r'(office )', 'Admin and Office'), 
    (r'(clerk)', 'Admin and Office'), 

#    (r'(mile)', 'Driver/Transportation'),     
    (r'(driv)', 'Driver/Transportation'), 
    (r'(courier)', 'Driver/Transportation'),
    (r'(cdl)', 'Driver/Transportation'), 
    (r'(truck)', 'Driver/Transportation'), 
    (r'(uber)', 'Driver/Transportation'),     
    (r'(delivery)', 'Driver/Transportation'),     
    (r'(transport)', 'Driver/Transportation'),     
     
    (r'(design)', 'Engineer'),      
    (r'(engineer)', 'Engineer'), 
     
    (r'(Environm)', 'Environment'), 
     (r'(maintenance)', 'Maintenance'), 
    (r'(security)', 'security'), 
     
    (r'(Account Executive)','Sales/Account Management'),
    (r'(account manager)','Sales/Account Management'),     
    (r'(sale)', 'Sales/Account Management'), 
    (r'(account s)', 'Sales/Account Management'), 
    
     
    (r'(clean)','Cleaner/Housekeeper'),     
    (r'(laundry)', 'Cleaner/Housekeeper'), 
    (r'(house cleaner)', 'Cleaner/Housekeeper'), 
    (r'(housekee)', 'Cleaner/Housekeeper'), 
    (r'(Custodian)', 'Cleaner/Housekeeper'), 
    (r'(Janitor)', 'Cleaner/Housekeeper'), 

    (r'(remodel)','Contractor'),
    (r'(drywall)','Contractor'),
    (r'(repair)','Contractor'),
    (r'(paint)', 'Contractor'), 
    (r'(floor)', 'Contractor'), 
     
    (r'(hvac)', 'Construction'), 
    (r'(hydro)', 'Construction'), 
    (r'(weld)', 'Construction'), 
    (r'(roof)', 'Construction'), 
    (r'(concrete)', 'Construction'), 
    (r'(construction)', 'Construction'), 
     
    (r'(tech)','Trade/Technician'),     
    (r'(journeyman)', 'Trade/Technician'), 
    (r'(oil)', 'Trade/Technician'), 
    (r'(electrical)', 'Trade/Technician'), 
    (r'(electrician)', 'Trade/Technician'),     
    (r'(plumb)', 'Trade/Technician'), 
    (r'(plumber)', 'Trade/Technician'), 
    (r'(Utili)', 'Trade/Technician'), 
    (r'(support tech)', 'Trade/Technician'), 
    (r'(tech)', 'Trade/Technician'), 
    (r'(technician)', 'Trade/Technician'), 
    (r'(apprentice)', 'Trade/Technician'), 

    (r'(nutrit)','Medical/Healthcare'),     
    (r'(prn )','Medical/Healthcare'),    
    (r'(rn )','Medical/Healthcare'),
    (r'(diet)', 'Medical/Healthcare'), 
    (r'(patient)', 'Medical/Healthcare'), 
    (r'(medical)', 'Medical/Healthcare'), 
    (r'(nurs)', 'Medical/Healthcare'), 
    (r'(dental)', 'Medical/Healthcare'), 
    (r'(clinic)', 'Medical/Healthcare'), 
    (r'(C.N.A)', 'Medical/Healthcare'), 
    (r'(CNA)', 'Medical/Healthcare'),      
     
    (r'(spa)', 'Service'), 
    (r'(salon)', 'Service'), 
    (r'(Barber)', 'Service'), 
     
    (r'(rep)', 'Customer Service'), 
    (r'(representative)', 'Customer Service'), 
    (r'(customer)', 'Customer Service'), 
    (r'(csr)', 'Customer Service'), 
    (r'(client service)', 'Customer Service'), 
     
    (r'(store)', 'Retail'),      
    (r'(produce)', 'Retail'),     
    (r'(retail)', 'Retail'), 
    (r'(merchan)', 'Retail'), 
    (r'(grocery)', 'Retail'), 
    (r'(shift)', 'Retail'), 
    (r'(team member)', 'Retail'),     
    (r'(cashier)', 'Retail'), 
    (r'(warehouse)', 'Warehouse'), 
    (r'(fork)', 'Warehouse'), 

    (r'(GM)','Manager'),     
    (r'(manage)', 'Manager'), 
    (r'(manager)', 'Manager'), 

#    (r'(hr)', 'Business'), 
#    (r'(service)', 'service'), 
#    (r'(senior)', 'senior'), 
#    (r'(seasonal)', 'seasonal'), 
#    (r'(residential)', 'residential'), 
#    (r'(professional)', 'professional'), 
#    (r'(immediate)', 'immediate'), 
#    (r'(inside)', 'inside'), 
#    (r'(home)', 'home'), 
#    (r'(experience)', 'experienced'), 
#    (r'(ft)', 'full time'), 
#    (r'(director)', 'director'), 
#    (r'(civil)', 'civil'), 
#    (r'(mgr)','Manager'),

#    (r'(coordinator)', 'coordinator'), 
#    (r'(benefit)', 'benefit'),
     
#    (r'(entry)', 'entry'), 
#    (r'(care)', 'care'), 
#    (r'(career)', 'career'),      
#    (r'(material)', 'material'), 
#    (r'(leader)', 'leader'), 
#    (r'(consultant)', 'consultant'), 
#    (r'(company)', 'company'), 
     
#    (r'(night)', 'night'), 
#    (r'(assistant)', 'assistant'), 
#    (r'(associate)', 'associate'), 
#    (r'(attendant)', 'attendant'), 
#    (r'(shop)', 'shop'), 
#    (r'(sign)', 'sign'),      
#    (r'(superintendent)', 'superintendent'), 
#    (r'(supervisor)', 'supervisor'),      
#    (r'(train)', 'train'), 
#    (r'(trainee)', 'trainee'),      
#    (r'(water)', 'water'), 
#    (r'(week)', 'week'), 
#    (r'(weekend)', 'weekend'), 
#    (r'(work)', 'work'),      
#    (r'(art)', 'art'), 
#    (r'(worker)', 'worker'), 
#    (r'(Aviati)','Aviation'),
#    (r'(Avioni)','Aviation'),
#    (r'(audio)','audio'),
#    (r'(account)', 'account'), 
#    (r'(agent)', 'agent'), 
#    (r'(opportunity)', 'opportunity'), 
#    (r'(order)', 'order'), 
#    (r'(outside)', 'outside'), 
#    (r'(partner)', 'partner'),     
}

# Scan each item in the list for the regex expression
# If a given job type is found, put the Job Type. 
# Else print "Other"

def job_type_look_up(s, lookuplist):
    for pattern, value in lookuplist:
        if re.search(pattern, s, re.IGNORECASE):
            return value
    return 'Other'

# Pull the job_title series
job_ser = df['job_title']
# Create a new dataframe for job_types 
df1 = pd.DataFrame()

# Scan each cell for a given Job Type

def df_scanner(ser, df):
    for ind, val in ser.iteritems():
        ahHa = job_type_look_up(val, job_types)
        df = df.append({'job_type': ahHa}, ignore_index=True)
    return df
        
# Create a new Column for Job Type
job_type_series = df_scanner(job_ser, df1)

# Merge OG data with job_type column
df_new = pd.concat([df, job_type_series], axis=1)

# Write to a csv file
df_new.to_csv('/Users/tylehman/Desktop/cjap_vm/django/cjap/cjap_engine/js_data/master.csv', encoding='utf-8', index=False)