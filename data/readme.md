# Database

## MYSQL as database
MySQL offers unmatched scalability to facilitate the management of deeply embedded apps using a smaller footprint even in massive warehouses that stack terabytes of data.<br>
MySQL features a distinct storage-engine framework that facilitates system administrators to configure the MySQL database server for a flawless performance.
![image](https://github.com/szyszy315/picture/blob/master/hw6p1.png)

## setup the db locally
mysql -uroot -p hw5DB < dumpfilename.sql

## operations
### input
write new data to DB
```
writetomysql.inserttoDB(input content)
```
### output function
#### read all the content in DB
```
readfrommysql.read()
```
![image](https://github.com/szyszy315/picture/blob/master/read.png)
#### get the record of high blood pressure
```
readfrommysql.highbp()
```
#### get the record of low blood pressure
```
readfrommysql.lowbp()
```
![image](https://github.com/szyszy315/picture/blob/master/lowhighbp.png)
#### get all the record of a person
```
readfrommysql.findhistory(name of person)
```
#### get the latest health status of a person
```
readfrommysql.lateststatus(name of person)
```
![image](https://github.com/szyszy315/picture/blob/master/latest.png)
#### get the evaluation of overall health status of someone 
```
readfrommysql.recordofpatient(name of person)
```
![image](https://github.com/szyszy315/picture/blob/master/overa%3B%3B.png)
