my_record = ("Pete", 1985, "alma")
print(my_record[0])
my_record[0] = "x"

######
my_record = ("Pete", 1985, "alma")

def foo():
    return 1, 2     # nem lehetnek zárójelben

print(type(foo()))

####
my_record = ("Pete", 1985, "alma")
my_list = list(my_record)
my_list.append('x')
print(my_list)

####
my_list = [1, 2, 3]         # nulladik, első, második elem
my_dict = {"alma": 1}     # alma kulcshoz tartozó 1-es érték pl az alma 1 ft-ba kerül

my_dict2 = dict()


###
my_dict = {"alma": 1, "korte": 12, 1: "citrom"}
print(my_dict["alma"])
if "xxx" in my_dict:            # csak akkor kérdezem le, ha az "xxx" érték benne van
print(my_dict["xxx"])       #nem létező érték lekérdezése - KeyError: 'xxx'

### milyen műveletek vannak még a dict-ben

my_dict = {"alma": 1, "korte": 12, 1: "citrom"}
pritn(my_dict)

del my_dict["alma"]             # törlés a szótárból

my_dict["alma"] += 5            # kiegészítem az alma értékét

###
my_dict = {"alma": 1, "korte": 12, 1: "citrom"}

for i in my_dict:
    print(i)

for i in my_dict.keys():
    print(i)


for i in my_dict.values():
    print(i)

for k, v in my_dict.items():
    print(k, v)

my_list = list(my_dict.keys())

