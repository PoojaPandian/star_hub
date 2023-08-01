class abc_Bangalore:
    branch_name = "ABC Textiles Bangalore"
    city = "Bangalore"
    pincode = 500411
    state = "Karnataka"
    address = "2nd floor, Prince tech park, Maadeeshwar nagar"

    def abc_1(self):
        self.branch_head = "Mr. Harish Varma"
        print("BRANCH NAME: ", self.branch_name)
        print("BRANCH HEAD: ", self.branch_head)
        print("We are a leading Clothing textile over the country. We are part of ABC Groups & co.")
        print("LOCATION: ", abc_Bangalore.address + "\n           " + abc_Bangalore.city + "\n           " + abc_Bangalore.state + "\n          ", abc_Bangalore.pincode)


class abc_Mumbai:
    branch_name = "ABC Foods Mumbai"
    city = "Mumbai"
    pincode = 890076
    state = "Maharashtra"
    address = "3rd floor, Jawahar street, Mangalore city"

    def abc_2(self):
        self.branch_head = "Mr. John Britten"
        print("BRANCH NAME: ", abc_Mumbai.branch_name)
        print("BRANCH HEAD: ", self.branch_head)
        print("We are a leading food manufacturing industry over the country. We are part of ABC Groups & co.")
        print("LOCATION: ", abc_Mumbai.address + "\n           " + abc_Mumbai.city + "\n           " + abc_Mumbai.state + "\n          ", abc_Mumbai.pincode)


class abc_Chennai:
    branch_name = "ABC Color Paints Chennai"
    city = "Chennai"
    pincode = 600118
    state = "Tamil Nadu"
    address = "MIC street, Manjore"

    def abc_3(self):
        self.branch_head = "Mr. Lokesh Rajan"
        print("BRANCH NAME: ", abc_Chennai.branch_name)
        print("BRANCH HEAD: ", self.branch_head)
        print("We are a leading Paint manufacturing factory across the country. We are part of ABC Groups & co.")
        print("LOCATION: ", abc_Chennai.address + "\n           " + abc_Chennai.city + "\n           " + abc_Chennai.state + "\n          ", abc_Chennai.pincode)


class abc_Hyderabad:
    branch_name = "ABC Steel Hyderabad"
    city = "Hyderabad"
    pincode = 890076
    state = "Andhra Pradesh"
    address = "Sidco industry, VC street"

    def abc_4(self):
        self.branch_head = "Mr. Rakesh Vaithiya"
        print("BRANCH NAME: ", abc_Hyderabad.branch_name)
        print("BRANCH HEAD: ", self.branch_head)
        print("We are a leading steel manufacturing industry across the country. We are part of ABC Groups & co.")
        print("LOCATION: ", abc_Hyderabad.address + "\n           " + abc_Hyderabad.city + "\n           " + abc_Hyderabad.state + "\n          ", abc_Hyderabad.pincode)


class abc(abc_Bangalore, abc_Mumbai, abc_Chennai, abc_Hyderabad):
    def abc_company(self):
        self.head_quarter = "Delhi"
        self.company_name = "ABC GROUPS & CO"
        print("COMPANY NAME: ", self.company_name)
        print("HEAD QUARTER: ", self.head_quarter)

p1= abc()
print()
p1.abc_company()
print()
print()
p1.abc_1()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p1.abc_2()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p1.abc_3()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
p1.abc_4()
