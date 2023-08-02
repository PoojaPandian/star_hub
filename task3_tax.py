def salary_tax(**employee):
    a = employee["salary"] * (0 / 100)
    b = employee["salary"] * (15 / 100)
    c = employee["salary"] * (20 / 100)
    d = employee["salary"] * (25 / 100)
    e = employee["salary"] * (30 / 100)
    if employee["salary"] <= 750000:
        print(employee["first_name"] + employee["last_name"] + " ,your tax amount is", a)
    elif employee["salary"] > 750000 and employee["salary"] <= 1000000:
        print(employee["first_name"] + employee["last_name"] + " ,your tax amount is", b)
    elif employee["salary"] > 1000000 and employee["salary"] <= 1250000:
        print(employee["first_name"] + employee["last_name"] + " ,your tax amount is", c)
    elif employee["salary"] > 1250000 and employee["salary"] <= 1500000:
        print(employee["first_name"] + employee["last_name"] + " ,your tax amount is", d)
    else:
        print(employee["first_name"] + employee["last_name"] + " ,your tax amount is", e)


salary_tax(last_name = "Kedare", first_name = "Sandeep", email = "skedare@gmail", salary = 1000000)
salary_tax(last_name = "Patil", first_name = "Suresh", email = "spatil@gmail.com", salary = 2000000)
salary_tax(last_name = "Singh", first_name = "Deep", email = "dsingh@gmail.com", salary = 2400000)
salary_tax(last_name = "Sawant", first_name = "Mihir", email = "msawant@gmail.com", salary = 2450000)
salary_tax(last_name = "Tripathi", first_name = "Mihir", email = "mtripathi@gmail.com", salary = 1250000)
salary_tax(last_name = "Shah", first_name = "Rajeev", email = "rshah@gmail.com", salary = 1750000)
salary_tax(last_name = "Joshi", first_name = "Girish", email = "gjoshi@gmail.com", salary = 150000)
salary_tax(last_name = "Joshi", first_name = "Hari", email = "hjoshi@gmail.com", salary = 150000)