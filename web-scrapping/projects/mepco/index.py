import time
from bs4 import BeautifulSoup
import requests
from csv import writer
from constants import *

def get_electricity_bills(reference_number):
    params["reference"] = reference_number
    # Make the GET request
    response = requests.get(base_url, params=params, headers=headers)

    # Check the status of the response
    if response.status_code == 200:
        bill_details = []
        customer_detail = {}

        soup = BeautifulSoup(response.text, 'lxml') # "html.parser"

        tables = soup.find_all('table')
        
        #########################
        table0 = soup.find('table', class_='maintable')
        
        table0_trs = table0.find_all('tr')
        current_bill_month = table0_trs[1].find_all('td')[3].get_text(strip=True)
        bill_issue_date = table0_trs[1].find_all('td')[5].get_text(strip=True)
        bill_due_date = table0_trs[1].find_all('td')[6].get_text(strip=True)
        
        # print("current_bill_month: ", current_bill_month)
        # print("bill_issue_date: ", bill_issue_date)
        # print("bill_due_date: ", bill_due_date)
        #########################
        table1 = soup.find('table', class_='nestable1')
        
        table1_trs = table1.find_all('tr')
        referenceNumber = table1_trs[3].find_all('td')[0].get_text(strip=True)
        noOfAcs = table1_trs[3].find_all('td')[2].get_text(strip=True)
        
        consumerId = table1_trs[1].find_all('td')[0].get_text(strip=True)

        # print("referenceNumber: ", referenceNumber)
        # print("noOfAcs: ", noOfAcs)
        # print("consumerId: ", consumerId)
        #########################
        
        table2 = tables[2]
        table2_trs = table2.find_all('tr')
        division = table2_trs[0].find_all('td')[1].get_text(strip=True)
        subdivision = table2_trs[1].find_all('td')[1].get_text(strip=True)
        feederName = table2_trs[2].find_all('td')[1].get_text(strip=True)
        
        # print("division: ", division)
        # print("subdivision: ", subdivision)
        # print("feederName: ", feederName)

        ##########################
        table3 = soup.find('table', class_='nested4')
        
        table3_trs = table3.find_all('tr')
        name = table3_trs[1].find('td').find_all('span')[1].get_text(strip=True)
        father_name = table3_trs[1].find('td').find_all('span')[2].get_text(strip=True)
        partialAddress1 = table3_trs[1].find('td').find_all('span')[3].get_text(strip=True)
        partialAddress2 = table3_trs[1].find('td').find_all('span')[4].get_text(strip=True)
        partialAddress3 = table3_trs[1].find('td').find_all('span')[5].get_text(strip=True)
        complete_address = partialAddress1 + " " + partialAddress2 + " " + partialAddress3

        # print("name: ", name)
        # print("fatherName: ", father_name)
        # print("completeAddress: ", complete_address)
        
        meter_no = table3_trs[4].find_all('td')[0].get_text(strip=True)
        presentMeterReading = table3_trs[4].find_all('td')[2].get_text(strip=True)
        multiplyFactor = table3_trs[4].find_all('td')[3].get_text(strip=True)

        # print("meter_no: ", meter_no)
        # print("presentMeterReading: ", presentMeterReading)
        # print("multiplyFactor: ", multiplyFactor)

        #############################
        charges_tables = soup.find_all('table', class_='nested7')
        mepco_govt_charges = charges_tables[0]
        total_charges_table = charges_tables[1]

        
        mepco_govt_charges_trs = mepco_govt_charges.find_all('tr')
        current_month_units_consumed = mepco_govt_charges_trs[1].find_all('td')[1].get_text(strip=True)
        cost_of_electricity = mepco_govt_charges_trs[2].find_all('td')[1].get_text(strip=True)
        total_mepco_charges = mepco_govt_charges_trs[9].find_all('td')[1].get_text(strip=True)
        total_govt_charges = mepco_govt_charges_trs[18].find_all('td')[-1].get_text(strip=True)

        total_charges_trs = total_charges_table.find_all('tr')
        current_month_total_charges = total_charges_trs[7].find_all('td')[1].get_text(strip=True)
        
        
        # print("current_month_units_consumed: ", current_month_units_consumed)
        # print("cost_of_electricity: ", cost_of_electricity)
        # print("total_mepco_charges: ", total_mepco_charges)
        # print("total_govt_charges: ", total_govt_charges)
        # print("current_month_total_charges: ", current_month_total_charges)

        ########################################
        past_bills_table = soup.find('table', class_='nested6')
        past_bills_table_trs = past_bills_table.find_all('tr')
        
        ##################### BILL DETAILS #################
        for index in range(1, 13, 1):
            bill_month = past_bills_table_trs[index].find_all('td')[0].get_text(strip=True)
            units = past_bills_table_trs[index].find_all('td')[1].get_text(strip=True)
            units_structured = " ".join(units.replace('\r', '').replace('\n', '').split())
            bill_amount = past_bills_table_trs[index].find_all('td')[2].get_text(strip=True)
            payment_made = past_bills_table_trs[index].find_all('td')[3].get_text(strip=True)
            
            # print("bill_month: ", bill_month)
            # print("units: ", units)
            # print("bill_amount: ", bill_amount)
            # print("payment_made: ", payment_made)
            bill_details.append({"bill_month": bill_month, "units_consumed": units_structured, "bill_amount": bill_amount, "payment_made": payment_made})

        
        # print("bill_month: ", current_bill_month)
        # print("current_month_units_consumed: ", current_month_units_consumed)
        # print("bill_amount: ", current_month_total_charges)
        bill_details.append({"bill_month": current_bill_month, "units_consumed": current_month_units_consumed, "bill_amount": current_month_total_charges})
        
        ##################### Customer details
        # print("referenceNumber: ", referenceNumber)
        # print("consumerId: ", consumerId)
        # print("division: ", division)
        # print("subdivision: ", subdivision)
        # print("feederName: ", feederName)

        # print("name: ", name)
        # print("fatherName: ", father_name)
        # print("completeAddress: ", complete_address)
        # print("meter_no: ", meter_no)
        customer_detail["referenceNumber"] = referenceNumber
        customer_detail["consumerId"] = consumerId
        customer_detail["meter_no"] = meter_no
        customer_detail["division"] = division
        customer_detail["subdivision"] = subdivision
        customer_detail["feederName"] = feederName
        customer_detail["name"] = name
        customer_detail["father_name"] = father_name
        customer_detail["complete_address"] = complete_address

        return { "bill_details": bill_details, "customer_detail": customer_detail }

    else:
        print("Failed to fetch data for reference:", params["reference"])

def create_csv_of_bills():
    with open('web-scrapping/mepco/bills.csv', 'w', encoding='utf8') as file:
        reference_number = "11156420655116"

        the_writer = writer(file)
        header = ['Reference Number', 'Bill Month', 'Units Consumed', 'Bill Amount', 'Payment Made']
        the_writer.writerow(header)
        detail = get_electricity_bills(reference_number)
        for bill in detail["bill_details"]:
            print(bill)
            info = [reference_number, bill['bill_month'], bill['units_consumed'], bill['bill_amount'], bill.get('payment_made', None)]
            the_writer.writerow(info)
        
        # print(detail["customer_detail"])
    


def create_csv_of_customers():
    with open('web-scrapping/mepco/customers.csv', 'w', encoding='utf8') as file:
        reference_number = "11156420655116"

        the_writer = writer(file)
        header = ['Reference Number', 'Consumer Id', 'Meter No', 'Name', 'Father Name', 'Address', 'Division', 'Sub Division', 'Feeder Name']
        the_writer.writerow(header)
        detail = get_electricity_bills(reference_number)
        customer = detail["customer_detail"]
        info = [customer['referenceNumber'],customer['consumerId'],customer['meter_no'],customer['name'], customer['father_name'],customer['complete_address'],customer['division'],customer['subdivision'],customer['feederName']]
        the_writer.writerow(info)

# create_csv_of_bills()
create_csv_of_customers()