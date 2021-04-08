import csv

input_file = "employee_data.csv"

employee_ID = []
name_list = []
dob = []
ssn = []
state = []
first_name = []
last_name = []
dob_reformat = []
ssn_reformat = []
st_abbreviation = []
contents = []
csvwriter = []
temp_name_list = []
temp_dob_list = []
temp_ssn_list = []
year = []
month = []
day = []
ssn4 = []
text_list = []

# Open input file
with open(input_file,'r', newline="") as csvfile:
    # reads and stores rows of the file in the contents list
    contents = csv.reader(csvfile)
    # Skips header
    contents_header = next(csvfile, None)

    # stores each column of the file in a list
    for rows in contents:
        employee_ID.append(rows[0])
        name_list.append(rows[1])
        dob.append(rows[2])
        ssn.append(rows[3])
        state.append(rows[4])

# split the lists name, dob and ssn by either space or "-" and stores its sublists in the respectives temp lists
for i in range(len(name_list)):
    temp_name_list.append(name_list[i].split())
    temp_dob_list.append(dob[i].split("-"))
    temp_ssn_list.append(ssn[i].split("-"))

# add the sublists of the temp_name_list to first_name and last-name lists
for name in temp_name_list:
    first_name.append(name[0])
    last_name.append(name[1])

# add the sublists of the temp_dob_list to year, month and day lists
for date in temp_dob_list:
    year.append(date[0])
    month.append(date[1])
    day.append(date[2])

# add the last sublist of temp_ssn_list to the list ssn4
for number in temp_ssn_list:
    ssn4.append(number[2])

# look for the state name in the "state list" and stores the respective abbreviation to the list st_abbrevisation
for st in state:
    if st == "Alabama":
        st_abbreviation.append("AL")
    elif st == "Alaska":
        st_abbreviation.append("AK")
    elif st == "Arizona":
        st_abbreviation.append("AZ")
    elif st == "California":
        st_abbreviation.append("CA")
    elif st == "Colorado":
        st_abbreviation.append("CO")
    elif st == "Connecticut":
        st_abbreviation.append("CT")
    elif st == "Delaware":
        st_abbreviation.append("DE")
    elif st == "Florida":
        st_abbreviation.append("FL")
    elif st == "Georgia":
        st_abbreviation.append("GA")
    elif st == "Hawaii":
        st_abbreviation.append("HI")
    elif st == "Idaho":
        st_abbreviation.append("ID")
    elif st == "Illinois":
        st_abbreviation.append("IL")
    elif st == "Indiana":
        st_abbreviation.append("IN")
    elif st == "Iowa":
        st_abbreviation.append("IA")
    elif st == "Kansas":
        st_abbreviation.append("KS")
    elif st == "Kentucky":
        st_abbreviation.append("KY")
    elif st == "Louisiana":
        st_abbreviation.append("LA")
    elif st == "Maine":
        st_abbreviation.append("ME")
    elif st == "Maryland":
        st_abbreviation.append("MD")
    elif st == "Massachusetts":
        st_abbreviation.append("MA")
    elif st == "Michigan":
        st_abbreviation.append("MI")
    elif st == "Minnesota ":
        st_abbreviation.append("MN")
    elif st == "Mississippi":
        st_abbreviation.append("MS")
    elif st == "Missouri":
        st_abbreviation.append("MO")
    elif st == "Montana":
        st_abbreviation.append("MT")
    elif st == "Nebraska":
        st_abbreviation.append("NE")
    elif st == "Nevada":
        st_abbreviation.append("NV")
    elif st == "New Hampshire":
        st_abbreviation.append("NH")
    elif st == "New Jersey":
        st_abbreviation.append("NJ")
    elif st == "New Mexico":
        st_abbreviation.append("NM")
    elif st == "New York":
        st_abbreviation.append("NY")
    elif st == "North Carolina":
        st_abbreviation.append("NC")
    elif st == "North Dakota":
        st_abbreviation.append("ND")
    elif st == "Ohio":
        st_abbreviation.append("OH")
    elif st == "Oklahoma":
        st_abbreviation.append("OK")
    elif st == "Oregon":
        st_abbreviation.append("OR")
    elif st == "Pennsylvania":
        st_abbreviation.append("PA")
    elif st == "Rhode Island":
        st_abbreviation.append("RI")
    elif st == "South Carolina":
        st_abbreviation.append("SC")
    elif st == "South Dakota":
        st_abbreviation.append("SD")
    elif st == "Tennessee":
        st_abbreviation.append("TN")
    elif st == "Texas":
        st_abbreviation.append("TX")
    elif st == "Utah":
        st_abbreviation.append("UT")
    elif st == "Vermont":
        st_abbreviation.append("VT")
    elif st == "Virginia":
        st_abbreviation.append("VA")
    elif st == "Washington":
        st_abbreviation.append("WA")
    elif st == "West Virginia":
        st_abbreviation.append("WV")
    elif st == "Wisconsin":
        st_abbreviation.append("WI")
    elif st == "Wyoming":
        st_abbreviation.append("WY")

# appends the lists month, day and year and the character "/" to the dob_reformat list. Appends the list ssn4 and the characters "***-**- " to the ssn_reformat list
for i in range(len(year)):
    dob_reformat.append(month[i] + "/" + day[i] + "/" + year[i])
    ssn_reformat.append("***-**-" + ssn4[i])

# stores the list in order as required by the assignment in a list "text_list"
text_list = zip(employee_ID,first_name,last_name,dob_reformat,ssn_reformat,st_abbreviation)

# creates and writes the text_list to a file "employee_modified.csv"
with open('employee_modified.csv', 'w',newline='') as myfile:
    wf = csv.writer(myfile)
    wf.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN","State"])
    wf.writerows(text_list)

