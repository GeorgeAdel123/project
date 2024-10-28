
class mcontact:
    def __init__(self , cname , cemail , phone_number):

         self.cname = cname
         self.cemail = cemail
         self.phone_number = phone_number

    def getname(self): 
        return self.cname
    def setname(self,cname,):
        self.cname = cname
    def getemail(self):
        return self.cemail
    def setemail(self,cemail):
        self.cemail = cemail
    def getnumber(self): 
        return self.phone_number
    def setnumber(self,phone_number): 
        self.phone_number = phone_number
    def describe(self):
        return f"name: {self.cname} , {self.cemail} , {self.phone_number} "
      
creature = mcontact("ashwinder","OMG@gmail.com","+4848588323")
print(creature.getname())
creature.setname("griffin")
print(creature.getname())
print(creature.getemail())
creature.setemail("galhyh@gmail.com")
print(creature.getemail())
print(creature.getnumber())
creature.setnumber("+127465785")
print(creature.getnumber())
print(creature.describe())
print("..................................................")
class magicwizard(mcontact):
    def __init__(self, wname, Wwand, wandcore, wandl, whouse):
        self.wname = wname
        self.Wwand = Wwand
        self.wandcore = wandcore
        self.wandl = wandl
        self.whouse = whouse
        wizard_houses=["slytherin","ravenclaw","hufflepuff","gryffindor"]
        if whouse not in wizard_houses:
            raise ValueError("error 404 house not found")
    def getwand(self):
        return f" wood: {self.Wwand} wandcore: {self.wandcore} wandlength: {self.wandl}"
    def gethouse(self):
        return f"house name: {self.whouse}"
    def describeW(self):
        return f"describtion:{wizard.getwand()}"
    
wizard=magicwizard("harry potter","holly","pheonix feather", "11 inches", "gryffindor")
print(wizard.getwand())
print(wizard.gethouse())
print(wizard.describeW())
print("..................................................")
class magicalcreatures(mcontact):
    def __init__(self, cspecies, tamed):
        self.cspecies = cspecies
        self.tamed = tamed
    def getspecies(self):
        return f" name of species: {self.cspecies}"
    def istamed(self):
        return True 
    def describeSP(self):
        return f"describtion: {species.getspecies()}, {species.istamed()}"
species = magicalcreatures("tawny owl","true")
print(species.getspecies())
print(species.istamed())
print(species.describeSP())
print("..................................................")
class magicalcontactbook:
    def __init__(self,contacts):
        self.contacts = list(contacts)
    def addcontact(self, contact):
        self.contacts.append(contact)
    def printlist(self):
        if len(self.contacts)>0:
            print("contacts list:")
        else :
            print("there are no contacts in this list")
    def find_contact(self,cname):
        for contact in self.contacts:
            if cname == contact.cname:
                return mcontact.describe(contact)
            else:
                print("contact is not found")
    
    
    
       








