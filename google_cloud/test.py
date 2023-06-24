import requests
import sys
import time


examples = [
    {
        "db_id": "station_weather",
        "create_table_sql": 
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE "train" (
                "id" int,
                "train_number" int,
                "name" text,
                "origin" text,
                "destination" text,
                "time" text,
                "interval" text,
                primary key ("id")
            );

            CREATE TABLE "station" (
                "id" int,
                "network_name" text,
                "services" text,
                "local_authority" text,
                primary key ("id")
            );

            CREATE TABLE "route" (
                "train_id" int,
                "station_id" int,
                primary key ("train_id", "station_id"),
                foreign key ("train_id") references `train`("id"),
                foreign key ("station_id") references `station`("id")
            );

            CREATE TABLE "weekly_weather" (
                "station_id" int,
                "day_of_week" text,
                "high_temperature" int,
                "low_temperature" int,
                "precipitation" real,
                "wind_speed_mph" int,
                primary key ("station_id", "day_of_week"),
                foreign key ("station_id") references "station"("id")
            );

            INSERT INTO  "train" VALUES ("1","16724","Ananthapuri Express","Trivandrum","Chennai","17:15","Daily");
            INSERT INTO  "train" VALUES ("2","16127","Guruvayur Express","Chennai","Guruvayur","22:10","Daily");
            INSERT INTO  "train" VALUES ("3","16128","Guruvayur Express","Guruvayur","Chennai","4:49","Daily");
            INSERT INTO  "train" VALUES ("4","16723","Ananthapuri Express","Chennai","Trivandrum","11:35","Daily");
            INSERT INTO  "train" VALUES ("5","16382","Jayanthi Janatha Express","Kanniyakumari","Mumbai","06:30","Daily");
            INSERT INTO  "train" VALUES ("6","16525","Island Express","Kanniyakumari","Bangalore","11:15","Daily");
            INSERT INTO  "train" VALUES ("7","56701","Madurai Fast Passenger","Quilon","Madurai","21:49","Daily");
            INSERT INTO  "train" VALUES ("8","56700","Quilon Fast Passenger","Madurai","Quilon Junction","04:55","Daily");
            INSERT INTO  "train" VALUES ("9","16526","Island Express","Bangalore","Kanniyakumari","16:59","Daily");
            INSERT INTO  "train" VALUES ("10","16381","Jayanthi Janatha Express","Mumbai","Kanniyakumari","10:38","Daily");
            INSERT INTO  "train" VALUES ("11","16650","Parasuram Express","Nagercoil","Mangalore","04:20","Daily");

            INSERT INTO  "station" VALUES (1, "Amersham","Metropolitan line and Chiltern Railways","Chiltern");
            INSERT INTO  "station" VALUES (2, "Bushey","London Overground and London Midland","Watford");
            INSERT INTO  "station" VALUES (3, "Brentwood","Greater Anglia","Brentwood");
            INSERT INTO  "station" VALUES (4, "Broxbourne","Greater Anglia","Broxbourne");
            INSERT INTO  "station" VALUES (5, "Carpenders Park","London Overground","Three Rivers");
            INSERT INTO  "station" VALUES (6, "Chafford Hundred","c2c","Thurrock");
            INSERT INTO  "station" VALUES (7, "Chalfont & Latimer","Metropolitan line and Chiltern Railways","Chiltern");
            INSERT INTO  "station" VALUES (8, "Chesham","Metropolitan line","Chiltern");
            INSERT INTO  "station" VALUES (9, "Cheshunt","Greater Anglia","Broxbourne");
            INSERT INTO  "station" VALUES (10, "Chorleywood","Metropolitan line and Chiltern Railways","Three Rivers");
            INSERT INTO  "station" VALUES (11, "Croxley","Metropolitan line","Three Rivers");

            INSERT INTO "weekly_weather" VALUES (1, "Monday", 59, 54, "90", 13);
            INSERT INTO "weekly_weather" VALUES (1, "Tuesday",  66, 55, "20", 12);
            INSERT INTO "weekly_weather" VALUES (1, "Wednesday", 60, 52, "10", 14);
            INSERT INTO "weekly_weather" VALUES (1, "Thursday",  55, 50, "30", 13);
            INSERT INTO "weekly_weather" VALUES (1, "Friday",  55, 52, "50", 17);
            INSERT INTO "weekly_weather" VALUES (1, "Saturday",  55, 52, "50", 14);
            INSERT INTO "weekly_weather" VALUES (1, "Sunday",  54, 52, "50", 12);
            INSERT INTO "weekly_weather" VALUES (2, "Monday",  58, 54, "60", 20);
            INSERT INTO "weekly_weather" VALUES (2, "Tuesday", 57, 54, "80", 22);
            INSERT INTO "weekly_weather" VALUES (2, "Wednesday",  59, 55, "90", 23);
            INSERT INTO "weekly_weather" VALUES (2, "Thursday",  59, 56, "70", 24);
            INSERT INTO "weekly_weather" VALUES (3, "Monday", 49, 46, "30", 10);
            INSERT INTO "weekly_weather" VALUES (3, "Tuesday",  50, 49, "50", 9);
            INSERT INTO "weekly_weather" VALUES (3, "Wednesday",  55, 54, "60", 8);
            INSERT INTO "weekly_weather" VALUES (4, "Monday", 58, 54, "70", 7);
            INSERT INTO "weekly_weather" VALUES (10, "Tuesday", 59, 52, "90", 22);

            INSERT INTO "route" VALUES (1,1);
            INSERT INTO "route" VALUES (1,2);
            INSERT INTO "route" VALUES (1,3);
            INSERT INTO "route" VALUES (2,1);
            INSERT INTO "route" VALUES (2,3);
            INSERT INTO "route" VALUES (2,7);
            INSERT INTO "route" VALUES (3,4);
            INSERT INTO "route" VALUES (4,6);
            INSERT INTO "route" VALUES (4,2);
            INSERT INTO "route" VALUES (5,1);
            INSERT INTO "route" VALUES (6,5);
            INSERT INTO "route" VALUES (7,4);
            INSERT INTO "route" VALUES (7,5);
            INSERT INTO "route" VALUES (7,8);
            INSERT INTO "route" VALUES (8,8);
            INSERT INTO "route" VALUES (9,7);
            INSERT INTO "route" VALUES (9,8);
            INSERT INTO "route" VALUES (10,9);
            """,
            "question": "list the local authorities and services provided by all stations.",
            #"query": "SELECT local_authority ,  services FROM station",

    },
    {
        "db_id": "entrepreneur",
        "create_table_sql": 
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE "entrepreneur" (
            "Entrepreneur_ID" int,
            "People_ID" int,
            "Company" text,
            "Money_Requested" real,
            "Investor" text,
            PRIMARY KEY ("Entrepreneur_ID"),
            FOREIGN KEY ("People_ID") REFERENCES "people"("People_ID")
            );

            CREATE TABLE "people" (
            "People_ID" int,
            "Name" text,
            "Height" real,
            "Weight" real,
            "Date_of_Birth" text,
            PRIMARY KEY ("People_ID")
            );


            INSERT INTO  "people" VALUES (1,"Francesco Postiglione",1.9,80,"1972-04-29");
            INSERT INTO  "people" VALUES (2,"Leonardo Binchi",1.86,57,"1975-08-27");
            INSERT INTO  "people" VALUES (3,"Fabrizio Buonocore",1.83, 45, "1977-04-28");
            INSERT INTO  "people" VALUES (4,"Marco Gerini",1.72, 75,"1971-08-05");
            INSERT INTO  "people" VALUES (5,"Roberto Calcaterra",1.75, 67, "1972-02-06");
            INSERT INTO  "people" VALUES (6,"Goran Fiorentini",1.78, 89, "1981-11-21");
            INSERT INTO  "people" VALUES (7,"Alberto Angelini",1.82,58, "1974-09-28");
            INSERT INTO  "people" VALUES (8,"Maurizio Felugo",1.95,76, "1981-03-04");

            INSERT INTO  "entrepreneur" VALUES (1,1,"Umbrolly","150000","Duncan Bannatyne");
            INSERT INTO  "entrepreneur" VALUES (2,2,"Grails Ltd","120000","Doug Richard");
            INSERT INTO  "entrepreneur" VALUES (3,3,"Le Beanock","54000","Rachel Elnaugh");
            INSERT INTO  "entrepreneur" VALUES (4,5,"IV Cam","50000","Peter Jones");
            INSERT INTO  "entrepreneur" VALUES (5,6,"Mycorrhizal Systems","75000","Simon Woodroffe");
            INSERT INTO  "entrepreneur" VALUES (6,8,"Elizabeth Galton Ltd","110000","Duncan Bannatyne");
            """,
        "question": "How many entrepreneurs are there?",
        #"query": "SELECT train_number ,  name FROM train ORDER BY TIME"
    },
    {
        'db_id': "customer_complaints",
        'create_table_sql': 
            """
            PRAGMA foreign_keys = ON;


            CREATE TABLE `Staff` (
            `staff_id` INTEGER PRIMARY KEY,
            `gender` VARCHAR(1),
            `first_name` VARCHAR(80),
            `last_name` VARCHAR(80),
            `email_address` VARCHAR(255),
            `phone_number` VARCHAR(80)
            );
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (114, '0', 'Ward', 'Boehm', 'marcelle.ritchie@example.com', '(379)551-0838x146');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (115, '1', 'Lucie', 'Lowe', 'ohintz@example.org', '142-311-6503x206');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (116, '0', 'Dagmar', 'Erdman', 'wrau@example.com', '345-656-5571');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (117, '0', 'Bradly', 'Hahn', 'brett99@example.net', '1-132-839-9409x288');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (118, '0', 'Austin', 'Zieme', 'reichel.armani@example.org', '(383)553-1035x20399');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (119, '0', 'Dorian', 'Oberbrunner', 'richard.gutkowski@example.com', '155-811-6153');
            INSERT INTO Staff (`staff_id`, `gender`, `first_name`, `last_name`, `email_address`, `phone_number`) VALUES (120, '0', 'Mikel', 'Lynch', 'glen.borer@example.com', '751-262-8424x575');


            CREATE TABLE `Customers` (
            `customer_id` INTEGER PRIMARY KEY,
            `customer_type_code` VARCHAR(20) NOT NULL,
            `address_line_1` VARCHAR(80),
            `address_line_2` VARCHAR(80),
            `town_city` VARCHAR(80),
            `state` VARCHAR(80),
            `email_address` VARCHAR(255),
            `phone_number` VARCHAR(80)
            );
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (113, 'Good Credit Rating', '144 Legros Landing', 'Apt. 551', 'Maryamport', 'Kansas', 'hsteuber@example.org', '06963347450');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (114, 'Good Credit Rating', '039 Jedidiah Estate Suite 537', 'Apt. 245',  'Sauerberg', 'Hawaii', 'cayla.satterfield@example.net', '470-803-0244');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (115, 'Good Credit Rating', '92189 Gulgowski Ranch Apt. 683', 'Apt. 828', 'Tyreekhaven', 'Tennessee', 'vida86@example.com', '997.698.4779x882');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (116, 'Good Credit Rating', '72144 Katlynn Flat Suite 512', 'Suite 959','Hansenbury', 'Tennessee', 'vbogisich@example.org', '548.373.3603x59134');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (117, 'Good Credit Rating', '1566 Ramona Overpass Apt. 464', 'Suite 151',  'North Alisaville', 'Florida', 'ubeier@example.org', '044-468-4549');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (118, 'Defaults on payments', '425 Roman Tunnel', 'Apt. 495',  'Funkstad', 'Colorado', 'lavonne.frami@example.com', '+38(3)9011433816');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (119, 'Good Credit Rating', '05355 Marcelle Radial', 'Suite 054',  'Port Joshuah', 'Pennsylvania', 'paige.hyatt@example.com', '1-369-302-7623x576');
            INSERT INTO Customers (`customer_id`, `customer_type_code`, `address_line_1`, `address_line_2`,  `town_city`, `state`, `email_address`, `phone_number`) VALUES (120, 'Defaults on payments', '518 Mann Park', 'Suite 035',  'West Annamariestad', 'Iowa', 'rzulauf@example.org', '578.019.7943x328');


            CREATE TABLE `Products` (
            `product_id` INTEGER PRIMARY KEY,
            `parent_product_id` INTEGER,
            `product_category_code` VARCHAR(20) NOT NULL,
            `date_product_first_available` DATETIME,
            `date_product_discontinued` DATETIME,
            `product_name` VARCHAR(80),
            `product_description` VARCHAR(255),
            `product_price` DECIMAL(19,4)
            );
            INSERT INTO Products (`product_id`, `parent_product_id`, `product_category_code`, `date_product_first_available`, `date_product_discontinued`, `product_name`, `product_description`,  `product_price`) VALUES (117, 4, 'Food', '1988-09-29 17:54:50', '1987-12-20 13:46:16', 'Chocolate', 'Handmade chocolate', '2.8800');
            INSERT INTO Products (`product_id`, `parent_product_id`, `product_category_code`, `date_product_first_available`, `date_product_discontinued`, `product_name`, `product_description`,  `product_price`) VALUES (118, 3, 'Book', '1974-06-25 12:26:47', '1991-08-20 05:22:31', 'The Great Gatsby', 'American novel','35.0000');
            INSERT INTO Products (`product_id`, `parent_product_id`, `product_category_code`, `date_product_first_available`, `date_product_discontinued`, `product_name`, `product_description`,  `product_price`) VALUES (119, 8, 'Hardware', '1994-12-18 15:13:19', '1997-07-02 18:26:16', 'Keyboard', 'Designed for games', '109.9900');
            INSERT INTO Products (`product_id`, `parent_product_id`, `product_category_code`, `date_product_first_available`, `date_product_discontinued`, `product_name`, `product_description`,  `product_price`) VALUES (120, 9, 'Hardware', '1998-06-20 15:04:11', '1980-06-26 10:40:19', 'Mouse', 'Blue tooth mouse', '23.3500');


            CREATE TABLE `Complaints` (
            `complaint_id` INTEGER NOT NULL ,
            `product_id` INTEGER NOT NULL,
            `customer_id` INTEGER NOT NULL,
            `complaint_outcome_code` VARCHAR(20) NOT NULL,
            `complaint_status_code` VARCHAR(20) NOT NULL,
            `complaint_type_code` VARCHAR(20) NOT NULL,
            `date_complaint_raised` DATETIME,
            `date_complaint_closed` DATETIME,
            `staff_id` INTEGER NOT NULL ,
            FOREIGN KEY (`staff_id` ) REFERENCES `Staff`(`staff_id` ),
            FOREIGN KEY (`product_id` ) REFERENCES `Products`(`product_id` ),
            FOREIGN KEY (`customer_id` ) REFERENCES `Customers`(`customer_id` )
            );
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (1, 117, 120, 'OK', 'Closed', 'Product Failure', '2002-07-18 10:59:35', '1976-04-19 11:03:06', 114);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (2, 118, 113, 'OK', 'New', 'Product Unusable', '1973-02-10 22:55:56', '2013-09-14 02:59:10', 120);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (3, 119, 114, 'OK', 'New', 'Product Unusable', '2006-10-29 07:08:46', '1995-09-11 14:48:46', 115);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (4, 120, 114, 'OK', 'Closed', 'Product Unusable', '1977-08-06 00:31:19', '1970-10-14 00:57:25', 114);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (5, 117, 118, 'OK', 'Open', 'Product Failure', '2007-10-14 21:50:43', '2000-08-17 17:02:48', 116);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (6, 118, 114, 'OK', 'Open', 'Product Unusable', '1987-07-11 14:40:30', '1975-10-11 05:54:30', 114);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (7, 117, 117, 'OK', 'New', 'Product Unusable', '2002-07-18 10:59:35', '1976-04-19 11:03:06', 118);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (8, 117, 114, 'OK', 'New', 'Product Unusable', '1973-02-10 22:55:56', '2013-09-14 02:59:10', 117);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (9, 117, 116, 'OK', 'New', 'Product Unusable', '2006-10-29 07:08:46', '1995-09-11 14:48:46', 120);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (10, 118, 115, 'OK', 'New', 'Product Unusable', '1977-08-06 00:31:19', '1970-10-14 00:57:25', 114);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (11, 118, 116, 'OK', 'Open', 'Product Unusable', '2007-10-14 21:50:43', '2000-08-17 17:02:48', 115);
            INSERT INTO Complaints (`complaint_id`, `product_id`, `customer_id`, `complaint_outcome_code`, `complaint_status_code`, `complaint_type_code`, `date_complaint_raised`, `date_complaint_closed`, `staff_id`) VALUES (12, 117, 116, 'OK', 'Open', 'Product Unusable', '1987-07-11 14:40:30', '1975-10-11 05:54:30', 114);


            """,
            "question": "Give the state that has the most customers."
    }
]


if __name__ == "__main__":
    url = "https://test2sql-s4vjhcroda-ue.a.run.app"
    if len(sys.argv) >= 2:
        url = sys.argv[1]
    cur_time = 0
    for example in examples:
        cur_time = time.time()
        x = requests.post(url, json = example)
        print(f"[Runtime: {time.time() - cur_time}s]", x.text)
         