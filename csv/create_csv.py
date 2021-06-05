# Create a csv file
import csv

with open("csv/destinations.csv", "w" , newline='') as csv_file:
     csv_writer = csv.writer(csv_file)
     csv_writer.writerow(['department_id','department_name','manager_id','location_id'])
     csv_writer.writerow([10,'Administration',200,1700])
     csv_writer.writerow([20,'Marketing',201,1800])
     csv_writer.writerow([30,'IT',202,1900])
     csv_writer.writerow([40,'Sales',203,2000])
     csv_writer.writerow([50,'Finance',204,2100])
     csv_writer.writerow([60,'Benefit',205,2200])
     csv_writer.writerow([70,'Treasury',206,2300])
     csv_writer.writerow([80,'Deposit',207,2400])

    

