from faker import Faker

fake = Faker(['en_AU'])
import random

f = open("DBfeederLast.sql","w")

mac = []
expertIDs = []
clientIDs = []
companyIDs = []
classIDs = []
packageIDs = []
softwareIDs = []
Client_TrainingPackage =[]
TrainingPackage_Software = []
Expert_TrainingPackage = []

companies = [
    "Virtuol Company",
    "InsuranceMeter Company",
    "Titan Eagle Company",
    "VR Alley Company",
    "Ayog Company",
    "Wealth Angle Company",
    "UGJA Company",
    "Oloa Company",
]

packages = [
    "NewStarter Package",
    "Illuminate Package",
    "Professional Package",
    "Package Invent",
    "Edu Package",
    "Transition Package"
]

softwares = [
    "Para Software",
    "Fair Software",
    "Innovative Software",
    "Interface Software",
    "Sparta Software",
    "Circus Software",
    "Software Safeguard",
    "Ascension Software",
    "Loyal Software",
    "BlackStar Software",
    "Crown Software",
    "Hardhat Software"
]

levels = ["Basic",
          "Intermediate",
          " Advance",
          "Customised"]

cities = ["Sydney",
          "Albury",
          "Armidale",
          "Bathurst",
          "Blue Mountains",
          "Broken Hill",
          "Campbelltown",
          "Cessnock",
          "Dubbo",
          "Goulburn",
          "Grafton",
          "Lithgow",
          "Liverpool",
          "Newcastle",
          "Orange",
          "Parramatta",
          "Penrith",
          "Queanbeyan",
          "Tamworth",
          "Wagga Wagga",
          "Wollongong",
          "Blacktown",
          "Canada Bay",
          "Coffs Harbour",
          "Fairfield",
          "Griffith",
          "Hawkesbury",
          "Lake Macquarie",
          "Lismore",
          "Maitland",
          "Randwick",
          "Ryde",
          "Shellharbour",
          "Shoalhaven",
          "Willoughby",
          "Bankstown",
          "Botany Bay",
          "Canterbury",
          "Dubbo",
          "Gosford",
          "Greater Taree",
          "Holroyd",
          "Hurstville",
          "Queanbeyan",
          "Rockdale",
          "Darwin",
          "Palmerston",
          "Brisbane",
          "Bundaberg",
          "Caboolture",
          "Cairns",
          "Caloundra",
          "Gladstone",
          "Gold Coast",
          "Gympie",
          "Hervey Bay",
          "Ipswich",
          "Logan City",
          "Mackay",
          "Maryborough",
          "Mount Isa",
          "Rockhampton",
          "Sunshine Coast",
          "Toowoomba",
          "Townsville",
          "Charters Towers",
          "Redcliffe City",
          "Redland City",
          "Thuringowa",
          "Warwick",
          "Adelaide",
          "Mount Barker",
          "Mount Gambier",
          "Murray Bridge",
          "Port Adelaide",
          "Port Augusta",
          "Port Pirie",
          "Port Lincoln",
          "Victor Harbor",
          "Hobart",
          "Burnie",
          "Devonport",
          "Launceston",
          "Melbourne",
          "Ararat",
          "Bairnsdale",
          "Benalla",
          "Ballarat",
          "Bendigo",
          "Dandenong",
          "Frankston",
          "Geelong",
          "Hamilton",
          "Horsham",
          "Latrobe City",
          "Melton",
          "Mildura",
          "Sale",
          "Shepparton",
          "Swan Hill",
          "Wangaratta",
          "Warrnambool",
          "Wodonga",
          "Perth",
          "Albany",
          "Bunbury",
          "Busselton",
          "Fremantle",
          "Geraldton",
          "Joondalup",
          "Kalgoorlie",
          "Karratha",
          "Mandurah",
          "Rockingh",
          "Armadale",
          "Bayswater",
          "Canning",
          "Cockburn",
          "Gosnells",
          "Kalamunda",
          "Kwinana",
          "Melville",
          "Nedlands",
          "South Perth",
          "Stirling",
          "Subiaco",
          "Swan",
          "Wanneroo"]
towns = [
    "Aberdare",
    "Abermain",
    "Adaminaby",
    "Adelong",
    "AgnesBanks",
    "AnnaBay",
    "Ardlethan",
    "AriahPark",
    "Ashford",
    "Austinmer",
    "AvocaBeach",
    "Ballina",
    "Balranald",
    "Bangalow",
    "Baradine",
    "Bargo",
    "Barham",
    "Barraba",
    "BatemansBay",
    "Batlow",
    "Bega",
    "Bellbird",
    "Bellingen",
    "BerkeleyVale",
    "Bermagui",
    "Berridale",
    "Berrigan",
    "Berrima",
    "Berry",
    "Bilpin",
    "Binalong",
    "Bingara",
    "Binnaway",
    "Blackheath",
    "Blaxland",
    "Blayney",
    "Boggabilla",
    "Boggabri",
    "Bolwarra",
    "Bomaderry",
    "Bombala",
    "Bonalbo",
    "BonnellsBay",
    "Bowenfels",
    "Bowraville",
    "Braidwood",
    "Branxton",
    "Brewarrina",
    "Brooklyn",
    "BrunswickHeads",
    "Bulahdelah",
    "Bullaburra",
    "Bulli",
    "Bundarra",
    "Bungendore",
    "Buronga",
    "Burradoo",
    "Canowindra",
    "CaptainsFlat",
    "ClarenceTown",
    "Cobar",
    "Coledale",
    "Collarenebri",
    "Condobolin",
    "Coolamon",
    "Cooma",
    "Coonabarabran",
    "Coonamble",
    "Cooranbong",
    "Cootamundra",
    "Corowa",
    "Cowra",
    "CrescentHead",
    "Crookwell",
    "Cudal",
    "Cumnock",
    "Dapto",
    "Dareton",
    "Deepwater",
    "Delegate",
    "Delungra",
    "Deniliquin",
    "Denman",
    "Dorrigo",
    "Dunedoo",
    "Dungog",
    "Edgeworth",
    "Ellalong",
    "EmuPlains",
    "Eugowra",
    "Euston",
    "EvansHead",
    "Faulconbridge",
    "FingalHead",
    "Forbes",
    "Forster",
    "Frederickton",
    "Galong",
    "Ganmain",
    "Gerringong",
    "Geurie",
    "Gilgandra",
    "GilliestonHeights",
    "Gladstone",
    "GlenInnes",
    "Glenbrook",
    "GolGol",
    "Gorokan",
    "Greenhill",
    "GreenwellPoint",
    "Grenfell",
    "Greta",
    "GroseVale",
    "Gulargambone",
    "Gundagai",
    "Gunnedah",
    "Gunning",
    "Guyra",
    "Harden",
    "HawksNest",
    "Hay",
    "Hazelbrook",
    "HeddonGreta",
    "Helensburgh",
    "Henty",
    "Hexham",
    "Hillston",
    "Holbrook",
    "Huskisson",
    "Inverell",
    "Ivanhoe",
    "Jennings",
    "Jerilderie",
    "Jindabyne",
    "Jugiong",
    "Junee",
    "Kandos",
    "Katoomba",
    "Kearsley",
    "Kempsey",
    "Kimovale",
    "Kinchela",
    "Kurrajong",
    "KurriKurri",
    "Kyogle",
    "LakeCargelligo",
    "LakeIllawarra",
    "Lapstone",
    "Lawson",
    "Leura",
    "LightningRidge",
    "Macksville",
    "Mallanganee",
    "Manildra",
    "Manilla",
    "Marulan",
    "Mathoura",
    "MedlowBath",
    "Mendooran",
    "Menindee"
]

# ------------------------------------------------------------------------

# ------------Class IDs-----------------------------------------------
for i in range(150):
    classID = "CLS{:05d}".format(i)
    classIDs.append(classID)

f.write("USE STHDB;\n\n")

# ------------Expert Table-----------------------------------------------
for _ in range(30):
    expertID = "EXP{:03d}".format(_)
    expertIDs.append(expertID)
    expertTelNo = fake.phone_number()
    while len(expertTelNo) != 15:
        expertTelNo = fake.phone_number()

    f.write('INSERT INTO Expert VALUES("{}", "{}", "{}", "{}", "{}", {});'.format(
        expertID,
        fake.first_name(),
        fake.last_name(),
        expertTelNo,
        fake.free_email(),
        # salary
        fake.random_int(0, 9999)
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------Company Table-----------------------------------------------
for _ in range(8):
    companyID = "CMP{:05d}".format(_)
    companyIDs.append(companyID)
    clientTelNo = fake.phone_number()

    f.write('INSERT INTO Company VALUES("{}", "{}", "{}", "{}", "{}", "{}");'.format(
        companyID,
        companies[_],
        fake.random_int(0,9999),
        random.choice(towns),
        random.choice(cities),
        fake.free_email()
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------Client Table-----------------------------------------------
for _ in range(100):
    clientID = "CLI{:05d}".format(_)
    clientIDs.append(clientID)
    clientTelNo = fake.phone_number()
    while len(clientTelNo) != 15:
        clientTelNo = fake.phone_number()

    f.write('INSERT INTO Client VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(
        clientID,
        random.choice(companyIDs),
        classIDs[_],
        fake.first_name(),
        fake.last_name(),
        clientTelNo,
        fake.free_email()
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------TrainingPackage Table-----------------------------------------------
for _ in range(len(packages)):
    packageID = "PKG{:02d}".format(_)
    packageIDs.append(packageID)

    f.write('INSERT INTO TrainingPackage VALUES("{}", "{}");'.format(
        packageID,
        packages[_]
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------PaymentRecord Table-----------------------------------------------
for _ in range(50):
    f.write('INSERT INTO PaymentRecord VALUES("{}", "{}", {}, "{}");'.format(
        fake.mac_address(),
        random.choice(companyIDs),
        random.randint(100, 999),
        fake.date_time_this_year()
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------Software Table-----------------------------------------------
for _ in range(len(softwares)):
    softwareID = "SW{:02d}".format(_)
    softwareIDs.append(softwareID)

    f.write('INSERT INTO Software VALUES("{}", "{}");'.format(
        softwareID,
        softwares[_]
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------Class Table-----------------------------------------------
for clzID in classIDs:
    packageLevel = random.choice(levels)
    if packageLevel == "Basic":
        packageCost = 200
    elif packageLevel == "Intermediate":
        packageCost = 500
    elif packageLevel == "Advance":
        packageCost = 1000
    elif packageLevel == "Customised":
        packageCost = random.randint(1000, 3000)

    # Startinng Date and Ending Date-------------------------
    startDate = str(fake.date_time_this_year())
    startDateList = startDate.split("-")
    years = ["2021", "2022", "2023", "2024"]
    endDate = random.choice(years)
    startDateList.pop(0)
    for i in startDateList:
        endDate += "-" + i

    # Temporaries-----------------------------------------------
    tempAddress = ["Client Premises", "SHT Labs"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    tempTimeSeconds = fake.time()
    tempStartTime =(tempTimeSeconds[:2])
    tempEndTime =int(tempStartTime)+2

    f.write('INSERT INTO Class VALUES("{}", "{}", "{}", "{}", {},"{}", "{}", "{}", "{}", "{}", "{}");'.format(
        clzID,
        random.choice(expertIDs),
        random.choice(packageIDs),
        packageLevel,
        packageCost,
        startDate,
        endDate,
        random.choice(tempAddress),
        random.choice(days),
        tempStartTime+":00:00",
        str(tempEndTime)+":00:00"
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------TrainingPackage_Software------------------------------------
TrainingPackage_Software2 = []
for _ in range(len(classIDs)*10):
    x = '"{}", "{}"'.format(
        random.choice(packageIDs),
        random.choice(softwareIDs)
    )
    TrainingPackage_Software2.append(x)
    TrainingPackage_Software = list(set(TrainingPackage_Software2))

for _ in range(len(TrainingPackage_Software)):
    f.write('INSERT INTO TrainingPackage_Software VALUES({});'.format(
        TrainingPackage_Software[_]
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------


# ------------Client_TrainingPackage--------------------------------------
Client_TrainingPackage2 =[]
for _ in range(len(classIDs)*10):
    x = '"{}", "{}"'.format(
        random.choice(clientIDs),
        random.choice(packageIDs)
    )
    Client_TrainingPackage2.append(x)
    Client_TrainingPackage = list(set(Client_TrainingPackage2))

for _ in range(len(Client_TrainingPackage)):
    f.write('INSERT INTO Client_TrainingPackage VALUES({});'.format(
        Client_TrainingPackage[_]
    ))
    f.write("\n")
f.write("\n")

# for _ in range(len(classIDs)*5):
#     f.write('INSERT INTO Client_TrainingPackage VALUES("{}", "{}");'.format(
#         random.choice(clientIDs),
#         random.choice(packageIDs)
#     ))
#     f.write("\n")
# f.write("\n")
# ------------------------------------------------------------------------


# ------------Expert_TrainingPackage--------------------------------------
Expert_TrainingPackage2 =[]
for _ in range(len(classIDs)*10):
    x = '"{}", "{}"'.format(
        random.choice(expertIDs),
        random.choice(packageIDs)
    )
    Expert_TrainingPackage2.append(x)
    Expert_TrainingPackage = list(set(Expert_TrainingPackage2))

for _ in range(len(Expert_TrainingPackage)):
    f.write('INSERT INTO Expert_TrainingPackage VALUES({});'.format(
        Expert_TrainingPackage[_]
    ))
    f.write("\n")
f.write("\n")
# ------------------------------------------------------------------------

f.close()
