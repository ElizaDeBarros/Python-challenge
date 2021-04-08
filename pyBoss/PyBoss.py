import os
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
st_abreviation = []
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


with open(input_file,'r', newline="") as csvfile:
    contents = csv.reader(csvfile)
    # Skips header
    contents_header = next(csvfile, None)

    for rows in contents:
        employee_ID.append(rows[0])
        name_list.append(rows[1])
        dob.append(rows[2])
        ssn.append(rows[3])
        state.append(rows[4])

for i in range(len(name_list)):
    temp_name_list.append(name_list[i].split())
    temp_dob_list.append(dob[i].split("-"))
    temp_ssn_list.append(ssn[i].split("-"))

for name in temp_name_list:
    first_name.append(name[0])
    last_name.append(name[1])

for date in temp_dob_list:
    year.append(date[0])
    month.append(date[1])
    day.append(date[2])

for number in temp_ssn_list:
    ssn4.append(number[2])

for st in state:
    if st == "Alabama":
        st_abreviation.append("AL")
    elif st == "Alaska":
        st_abreviation.append("AK")
    elif st == "Arizona":
        st_abreviation.append("AZ")
    elif st == "California":
        st_abreviation.append("CA")
    elif st == "Colorado":
        st_abreviation.append("CO")
    elif st == "Connecticut":
        st_abreviation.append("CT")
    elif st == "Delaware":
        st_abreviation.append("DE")
    elif st == "Florida":
        st_abreviation.append("FL")
    elif st == "Georgia":
        st_abreviation.append("GA")
    elif st == "Hawaii":
        st_abreviation.append("HI")
    elif st == "Idaho":
        st_abreviation.append("ID")
    elif st == "Illinois":
        st_abreviation.append("IL")
    elif st == "Indiana":
        st_abreviation.append("IN")
    elif st == "Iowa":
        st_abreviation.append("IA")
    elif st == "Kansas":
        st_abreviation.append("KS")
    elif st == "Kentucky":
        st_abreviation.append("KY")
    elif st == "Louisiana":
        st_abreviation.append("LA")
    elif st == "Maine":
        st_abreviation.append("ME")
    elif st == "Maryland":
        st_abreviation.append("MD")
    elif st == "Massachusetts":
        st_abreviation.append("MA")
    elif st == "Michigan":
        st_abreviation.append("MI")
    elif st == "Minnesota ":
        st_abreviation.append("MN")
    elif st == "Mississippi":
        st_abreviation.append("MS")
    elif st == "Missouri":
        st_abreviation.append("MO")
    elif st == "Montana":
        st_abreviation.append("MT")
    elif st == "Nebraska":
        st_abreviation.append("NE")
    elif st == "Nevada":
        st_abreviation.append("NV")
    elif st == "New Hampshire":
        st_abreviation.append("NH")
    elif st == "New Jersey":
        st_abreviation.append("NJ")
    elif st == "New Mexico":
        st_abreviation.append("NM")
    elif st == "New York":
        st_abreviation.append("NY")
    elif st == "North Carolina":
        st_abreviation.append("NC")
    elif st == "North Dakota":
        st_abreviation.append("ND")
    elif st == "Ohio":
        st_abreviation.append("OH")
    elif st == "Oklahoma":
        st_abreviation.append("OK")
    elif st == "Oregon":
        st_abreviation.append("OR")
    elif st == "Pennsylvania":
        st_abreviation.append("PA")
    elif st == "Rhode Island":
        st_abreviation.append("RI")
    elif st == "South Carolina":
        st_abreviation.append("SC")
    elif st == "South Dakota":
        st_abreviation.append("SD")
    elif st == "Tennessee":
        st_abreviation.append("TN")
    elif st == "Texas":
        st_abreviation.append("TX")
    elif st == "Utah":
        st_abreviation.append("UT")
    elif st == "Vermont":
        st_abreviation.append("VT")
    elif st == "Virginia":
        st_abreviation.append("VA")
    elif st == "Washington":
        st_abreviation.append("WA")
    elif st == "West Virginia":
        st_abreviation.append("WV")
    elif st == "Wisconsin":
        st_abreviation.append("WI")
    elif st == "Wyoming":
        st_abreviation.append("WY")

for i in range(len(year)):
    dob_reformat.append(month[i] + "/" + day[i] + "/" + year[i])
    ssn_reformat.append("***-**-" + ssn4[i])

text_list = zip(employee_ID,first_name,last_name,dob_reformat,ssn_reformat,st_abreviation)
print(text_list)

with open('employee_modified.csv', 'w',newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN","State"])
    wr.writerows(text_list)

