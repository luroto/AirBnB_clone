# 0x00. AirBnB clone - The console

### Description
 This is the repository for an application based on AirBnB. It contains PEP8 compliant code for a console and a structure of classes strongly based on a BaseModel class. Also, it contains a set of UnitTest for each component.

 On this project we're reviewing:
 * How to create a Python package
 * How to create a command interpreter in Python using the cmd module
 * What is Unit testing and how to implement it in a large project
 * How to serialize and deserialize a Class
 * How to write and read a JSON file
 * How to manage datetime
 * What is an UUID
 * What is *args and how to use it
 * What is **kwargs and how to use it
 * How to handle named arguments in a function

 ### The command intepreter:
 Based on the CMD Python module, it handles the basic commands for this object.
 How to start it:
 Do a git clone of this repository, enter it and execute through a ```./console.py```. The basic commands are ```create```, ```show```, ```all```, ```destroy``` and ```update```.
 ##### Examples

 ```python
 (hbnb)create User
 e4e034b1-8f58-403d-a3ff-75e7d0b994c9
 (hbnb)show User e4e034b1-8f58-403d-a3ff-75e7d0b994c9
 [User] (e4e034b1-8f58-403d-a3ff-75e7d0b994c9) {'id': 'e4e034b1-8f58-403d-a3ff-75e7d0b994c9', 'created_at': datetime.datetime(2019, 7, 6, 0, 1, 49, 703586), 'updated_at': datetime.datetime(2019, 7, 6, 0, 1, 49, 703976)}
 (hbnb)update User e4e034b1-8f58-403d-a3ff-75e7d0b994c9 first_name "Nombrecito"
 (hbnb)show User UUID
 [User] (e4e034b1-8f58-403d-a3ff-75e7d0b994c9) {'id': 'e4e034b1-8f58-403d-a3ff-75e7d0b994c9', 'created_at': datetime.datetime(2019, 7, 6, 0, 1, 49, 703586), 'updated_at': datetime.datetime(2019, 7, 6, 0, 1, 49, 703976), 'first_name': '"Nombrecito"'}
 (hbnb)destroy User UUID
 (hbnb)show Use UUID
 ** no instance found **
 ```
 At this moment you're able to print the data of all instances and count them on this way:
 ```python
 (hbnb)create User
 0724a62e-6009-4b64-b365-88481885bf17
 (hbnb)create User
 86139bf9-9c18-4fc1-ac53-d0068db4ce62
 (hbnb)User.count()
 2
 (hbnb)User.all()
 ["[User] (0724a62e-6009-4b64-b365-88481885bf17) {'id': '0724a62e-6009-4b64-b365-88481885bf17', 'created_at': datetime.datetime(2019, 7, 6, 0, 6, 41, 173415), 'updated_at': datetime.datetime(2019, 7, 6, 0, 6, 41, 174107)}", "[User] (86139bf9-9c18-4fc1-ac53-d0068db4ce62) {'id': '86139bf9-9c18-4fc1-ac53-d0068db4ce62', 'created_at': datetime.datetime(2019, 7, 6, 0, 6, 44, 304614), 'updated_at': datetime.datetime(2019, 7, 6, 0, 6, 44, 305160)}"]
 ```
 This way you can check instances: a given one, all of a given classes and all the instances created:

 ```python
 (hbnb)create User
 f82d03e6-690e-4772-933c-4e1bfdce4946
 (hbnb)create User
 fa7d1c21-afc2-41d8-b932-b91e786ac822
 (hbnb)create BaseModel
 ca197229-57a7-490e-bf25-479836c39bd7
 (hbnb)create BaseModel
 000c4a2f-307f-47ca-8a87-e29e248e640b
 (hbnb)create Review
 991bac00-7538-4cb7-b67f-57bc4a1e2d72
 (hbnb)create Amenity
 80a1bf5a-11f2-407c-8436-bedafd517072
 (hbnb)create State
 81c319ba-0d14-4cf8-b5fc-5681f9aca9c0
 (hbnb)create User
 3542e23c-07dc-4c86-8662-1c8f0e41b0e5
 (hbnb)create Review
 47d0904a-4368-43ab-ae6e-35efa674c082
 (hbnb)all
 ["[User] (f82d03e6-690e-4772-933c-4e1bfdce4946) {'id': 'f82d03e6-690e-4772-933c-4e1bfdce4946', 'created_at': datetime.datetime(2019, 7, 6, 0, 8, 31, 101549), 'updated_at': datetime.datetime(2019, 7, 6, 0, 8, 31, 102010)}", "[User] (fa7d1c21-afc2-41d8-b932-b91e786ac822) {'id': 'fa7d1c21-afc2-41d8-b932-b91e786ac822', 'created_at': datetime.datetime(2019, 7, 6, 0, 8, 41, 950948), 'updated_at': datetime.datetime(2019, 7, 6, 0, 8, 41, 951490)}", "[BaseModel] (ca197229-57a7-490e-bf25-479836c39bd7) {'id': 'ca197229-57a7-490e-bf25-479836c39bd7', 'created_at': datetime.datetime(2019, 7, 6, 0, 8, 55, 978651), 'updated_at': datetime.datetime(2019, 7, 6, 0, 8, 55, 979194)}", "[BaseModel] (000c4a2f-307f-47ca-8a87-e29e248e640b) {'id': '000c4a2f-307f-47ca-8a87-e29e248e640b', 'created_at': datetime.datetime(2019, 7, 6, 0, 9, 6, 882913), 'updated_at': datetime.datetime(2019, 7, 6, 0, 9, 6, 883450)}", "[Review] (991bac00-7538-4cb7-b67f-57bc4a1e2d72) {'id': '991bac00-7538-4cb7-b67f-57bc4a1e2d72', 'created_at': datetime.datetime(2019, 7, 6, 0, 9, 23, 191271), 'updated_at': datetime.datetime(2019, 7, 6, 0, 9, 23, 191929)}", "[Amenity] (80a1bf5a-11f2-407c-8436-bedafd517072) {'id': '80a1bf5a-11f2-407c-8436-bedafd517072', 'created_at': datetime.datetime(2019, 7, 6, 0, 9, 35, 353363), 'updated_at': datetime.datetime(2019, 7, 6, 0, 9, 35, 354087)}", "[State] (81c319ba-0d14-4cf8-b5fc-5681f9aca9c0) {'id': '81c319ba-0d14-4cf8-b5fc-5681f9aca9c0', 'created_at': datetime.datetime(2019, 7, 6, 0, 9, 50, 642130), 'updated_at': datetime.datetime(2019, 7, 6, 0, 9, 50, 642747)}", "[User] (3542e23c-07dc-4c86-8662-1c8f0e41b0e5) {'id': '3542e23c-07dc-4c86-8662-1c8f0e41b0e5', 'created_at': datetime.datetime(2019, 7, 6, 0, 10, 2, 128393), 'updated_at': datetime.datetime(2019, 7, 6, 0, 10, 2, 129472)}", "[Review] (47d0904a-4368-43ab-ae6e-35efa674c082) {'id': '47d0904a-4368-43ab-ae6e-35efa674c082', 'created_at': datetime.datetime(2019, 7, 6, 0, 10, 13, 526928), 'updated_at': datetime.datetime(2019, 7, 6, 0, 10, 13, 527754)}"]
 (hbnb)User.count()
 3
 (hbnb)all User
 ["[User] (f82d03e6-690e-4772-933c-4e1bfdce4946) {'id': 'f82d03e6-690e-4772-933c-4e1bfdce4946', 'created_at': datetime.datetime(2019, 7, 6, 0, 8, 31, 101549), 'updated_at': datetime.datetime(2019, 7, 6, 0, 8, 31, 102010)}", "[User] (fa7d1c21-afc2-41d8-b932-b91e786ac822) {'id': 'fa7d1c21-afc2-41d8-b932-b91e786ac822', 'created_at': datetime.datetime(2019, 7, 6, 0, 8, 41, 950948), 'updated_at': datetime.datetime(2019, 7, 6, 0, 8, 41, 951490)}", "[User] (3542e23c-07dc-4c86-8662-1c8f0e41b0e5) {'id': '3542e23c-07dc-4c86-8662-1c8f0e41b0e5', 'created_at': datetime.datetime(2019, 7, 6, 0, 10, 2, 128393), 'updated_at': datetime.datetime(2019, 7, 6, 0, 10, 2, 129472)}"]
 ```
 All commands are case-sensitive.
 ### Features
 This console requires ```python3``` for its execution. It's able to create instances from dictionaries and stores data into a JSON file.

 ### Files and their content:
 |Files| Description|
 |------|------|
 |[README](./README.md)| It contains a description of the project, description of the command interpreter (how to start it, how to use it and examples)|
 |[AUTHORS](./AUTHORS)|A list of creators of this repository|
 | [Unittests](./tests/)| Tests for all classes and files on this repository|
 |[BaseModel](./models/base_model.py) |The BaseModel class defines all common attributes/methods for other classes, on this case its start point contains the id and time of creation and update. It is able to get data from dictionary representation|
 |[FileStorage](./models/engine/file_storage.py)| A class which handles all about storing data.
 |[Console](./console.py)| A command line interpreter with basic commands and a ```help``` option.|
 |[User](./models/user.py)| A class which inherits from BaseModel and handles user data|
 |[Place](./models/place.py)| A class which inherits from BaseModel and handles place data|
 |[State](./models/state.py)| Handles state data|
 |[City](./models/city.py)| Handles city data|
 |[Amenity](./models/amenity.py)| Handles place's amenity data
 |[Review](./models/review.py)| Handles review data|

 #### Commands
 ```create <ClassName>```: Creates any of the supported classes. It prints the created class' instance ID.

 ```show <ClassName> <InstanceID>```: Shows the data in dictionary format for the given class name and instance ID.

 ```all``` or ```all <ClassName>```: On the first case it will print all the instances created at the moment. Using the ClassName will print all the matching cases.

 ```destroy <ClassName> <InstanceID>```: Removes the dictionary entry of the given class name and instance ID and saves the changes in the JSON file.

 ```update <ClassName> <InstanceID> <AttributeName> <AttributeValue>```: Update data entries of the given class name and its instance ID. If the attribute is already created, it will be update, otherwise it will be created and saved.

 ## Author
 * **Alejo-Rey** - [Alejo-Rey](https://github.com/Alejo-Rey)
 * **Lucia-Rodriguez** - [Luroto](https://github.com/luroto)