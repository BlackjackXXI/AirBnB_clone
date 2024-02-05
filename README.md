# AirBnb Clone - The Console
---
## Description
##### The command interpreter will be used in subsequent AirBnb projects to manage objects of our classes. This console will allow us to do the following:
  *  Create new objects
  *  Retrieve an object
  *  Do operations on an object
  *  Change and update object attributes
  *  Destroy an object
## Usage
The console can be run in interactive and non-interactive mode.
### Non-Interactive Mode

To run a command in non-interactive mode, echo the desired command and pipe it into the console like so:
``` 
echo "<command>" | ./console.py 
```
##### Examples (syntax)
```
echo "create BaseModel" | ./console.py
```

``` 
echo "all" | ./console.py
```

```
echo "show BaseModel 1123-2312312-241214-213134" | ./console.py
```

### Interactive Mode

To run in interactive mode:

``` 
./console.py 
```
Then type the desired commands inside of the program.

##### Examples (syntax)

```
(hbnb) create BaseModel
```

```
(hbhb) all
```

```
(hbnhb) show BaseModel 1123-2312312-241214-213134"
```

## Commands

Command | Description
--- | --- 
`quit` | Exit the program
`EOF` | Exit the program
`create <class>` | Create an instance of a class
`show <class> <id>` | Print the string representation of an instance of a class
`destroy <class> <id>` | Delete instance of a class
`update <class> <id> <attribute name> "<attribute value>"` | Update an attribute of an instance
`all` | Print all string representations of all instances
`all <class>` | Print all string representations of all instances of a class 
`<class>.all()` | See `all`
`<class>.count()` | Return number of instances of a class
`<class>.show(<id>)` | See `show`
`<class>.destroy(<id>)` | See `destroy`
`<class>.update(<id>, <attribute name>, <attribute value>)` | See `update`

##### Examples (output)

```
(hbnb) create User
8cf6930e-da38-4ecb-887a-841d7de188cb
```

```
(hbnb) show User 8cf6930e-da38-4ecb-887a-841d7de188cb
[BaseModel] (8cf6930e-da38-4ecb-887a-841d7de188cb) {'id': '8cf6930e-da38-4ecb-887a-841d7de188cb', 'updated_at': datetime.datetime(2019, 7, 3, 22, 37, 53, 44113), 'created_at': datetime.datetime(2019, 7, 3, 22, 37, 53, 44069)}
```

```
(hbnb) User.count()
1
```

## Files

File Name | Description
--- | ---
`console.py` | Program for running the HBNB console
`models/basemodel.py` | Defines the BaseModel class 
`models/engine/file_storage.py` | Defines the FileStorage class, handles the database
`models/user.py` | Defines the User class, subclass of BaseModel
`models/city.py` | Defines the City  class, subclass of BaseModel
`models/state.py` | Defines the User class, subclass of BaseModel
`models/amenity.py` | Defines the Amenity class, subclass of BaseModel
`models/review.py` | Defines the Review class, subclass of BaseModel
`models/place.py` | defines the place class, subclass of basemodel
`tests/` | the test directory contains all unittest files for each class, separated by class name

---

## About
This project was created by
* **Jason Cortella** - [GitHub - jasoncortella](https://github.com/jasoncortella) | [LinkedIn](https://www.linkedin.com/in/jcortella/) at [Holberton
School](http://holbertonschool.com).
* **Josef Goodyear** - [GitHub - JosefGoodyear](https://github.com/josefgoodyear) | [LinkedIn](https://www.linkedin.com/in/josefgoodyear/) at [Holberton
School](http://holbertonschool.com).

