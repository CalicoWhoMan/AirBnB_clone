# AIRBNB clone

A command interpreter used to manage AirBnB clone objects. 

## Description

From this command interpreter you can save and reload AirBnB objects to and from a .json file. You can update attributes as well as create and delete objects. 

## Execution


### Running the console

 * Run the console
```
./console
```
 * Example:
 ```
 (hbnb)
 ```
 
 ### Quit - Quits the Console
 * Use 'quit'
 ```
 (hbnb) quit
 ```

### Help - Lists all Commands used in the Console

* Use 'help'
```
(hbnb) help
```
* Example:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```
### Destroy - Deletes an Instance Based on 'Class Name' & 'ID'

* Use destroy 'class name' 'id'
```
(hbnb) destroy BaseModel 26edbf21-1127-4db6-b66f-10e37b002886
```
### Show - Prints a String Representation  of an Instance based on 'Class Name' & 'ID'

* Use show 'class name' 'id'
```
(hbnb) show BaseModel ebad8c68-6584-4417-a7ec-6430aeb987de
```
* Example:
```
[BaseModel] (ebad8c68-6584-4417-a7ec-6430aeb987de) {'id': 'ebad8c68-6584-4417-a7ec-6430aeb987de', 'created_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799454), 'updated_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799474)}
```
### Update - Updates an Instance Based on 'Class Name' & 'ID'

* Use update 'class name' 'id' 'attribute value'
```
(hbnb) update BaseModel ebad8c68-6584-4417-a7ec-6430aeb987de `email "aibnb@mail.com"`
```
* Example:
```
(hbnb) show BaseModel ebad8c68-6584-4417-a7ec-6430aeb987de
```
```
[BaseModel] (ebad8c68-6584-4417-a7ec-6430aeb987de) {'id': 'ebad8c68-6584-4417-a7ec-6430aeb987de', 'created_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799454), 'updated_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799474), '`email': 'aibnb@mail.com"'}
```
### All - Prints All String Representations of All Instances

* Use 'all' or all 'class name' 'id'
```
(hbnb) all
```
```
(hbnb) all BaseModel 26edbf21-1127-4db6-b66f-10e37b002886
```
*Example
```
[BaseModel] (26edbf21-1127-4db6-b66f-10e37b002886) {'id': '26edbf21-1127-4db6-b66f-10e37b002886', 'created_at': datetime.datetime(2022, 2, 10, 12, 34, 22, 855286), 'updated_at': datetime.datetime(2022, 2, 10, 12, 34, 22, 855548)}
[BaseModel] (ebad8c68-6584-4417-a7ec-6430aeb987de) {'id': 'ebad8c68-6584-4417-a7ec-6430aeb987de', 'created_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799454), 'updated_at': datetime.datetime(2022, 2, 10, 12, 37, 18, 799474), '`email': 'aibnb@mail.com"'}
```