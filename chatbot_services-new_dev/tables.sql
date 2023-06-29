CREATE DATABASE bondsDB;
CREATE DATABASE convoDB;
CREATE DATABASE globalDB;

USE convoDB;

CREATE TABLE convo (
   unique_id VARCHAR(15) PRIMARY KEY,
   time_stamp DATETIME,
   cum_sum_user VARCHAR(1500),
   cum_sum_bot VARCHAR(1500),
   isResolved BOOLEAN,
   isClosedbyUser BOOLEAN,
   global_hits varchar(100)
);

USE globalDB;

CREATE TABLE global (
   id INT PRIMARY KEY,
   keywords VARCHAR(100),
   expected_response VARCHAR(500),
   probability DECIMAL(2,1)
);

USE bondsDB; 

CREATE TABLE bonds (
   isin VARCHAR(12) PRIMARY KEY,
   category VARCHAR(100),
   currency_of_issue VARCHAR(100),
   coupon_rate DECIMAL(4,1),
   maturity INT,
   isOfferedByGS BOOLEAN
);
