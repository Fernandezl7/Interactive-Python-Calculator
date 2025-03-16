## Python Interactive Calculator:

This is an interactive calculator that performs various functions. This calculator has the support of dynamic plugin interactions as well as calculator history. This calculator can perfom basic arithmetic operations, store history, get history, delete history, import history from .csv file, and exports history to a .csv file. The calculator application was designed to be user-friendly, implementing key programming concepts including design patterns and development best practices, ensuring efficient error handling, logging ang testing

Menu:

Displays user friendly menu options. 

	Greet : To Perform Greet Operation

	Menu : To List the Menu options

	add : To Perform Addition

	multiply : To Perform Multiplication

	subtract : To Perform Subtraction

	divide : To Perform Division

	history : To load the saved History Data

	clearhistory : Clear the History details

	deletehistory : Delete History from the Dataframe / CSV file

	exit : To Perform Exit Operation

## Usage Information:

1. Git clone "https://github.com/Fernandezl7/Interactive-Python-Calculator"
2. pip install -r requirements.txt

## This calculator runs in two important modes:

i. Interavtive mode: implemeted using plugins to perform arithmentic operations (add, subtract, multiply, and divide) and calculation management

ii. Command line (REPL): using read-evaluate-print-loop to facilitate direct interaction with the calculator to perform add, subtract, multiply and divide. 

python main.py 10 5 add	
python main.py <number1> <number2> add
python main.py <number1> <number2> subtract
python main.py <number1> <number2> multiply
python main.py <number1> <number2> divide

## Main features of the project:

1. REPL Command-Line Interface

    The Read, Evaluate, Print, Loop allows users to execute commands fro add, subtract, multiply, and divide. This supports built-in commands for viewing, importing/exporting, and managing history. 

    A main.py entry point provides eas access to CLI utilities. It implements command patterns for modular and reusable arithmetic operations.
        
2. Plugin Architecture for Extensibility

    Dynamically loads plugins for seamless integration of new commands and features. Includes a Menu command that lists available commands and usage example. It implements additional Greet and Exit commands for better user interaction.

3. Software Design Patterns & Best Practices

    Facade pattern: Simplifies interactions between the application and the pandas data manipulation

    DRY Principle: Ensures reusability and maintainability by eliminating redundat code through function reuse and modular components

    Look Before You Leap (LBYL): Prevents invalid operations by checking conditions before execution.

    Easier to Ask for Forgiveness than Permission (EAFP): Reducess excessive condition-checking, improving performance via exception handling

4. Environment Variable Management & Structured Logging
        * Environment Variables:

        Use a .env file to store configurable settings such as file paths and environment-specific configurations

        * Logging & Error handling:

        Implements structured logging using python's logging module to trace application flow and debug issues. The exception handling covers scenarios like invalid imputs, division by zero, and unregistered commands to prevent system crahes. 

5. Continuous Intergration:

    Usage of Github actions workflwo to run tests directly from Github automatically when new iterms are pushed

6. Calculation History Management:

Usage of pandas library for Dataframe loading, CSV file export and import functions for history management, Functions include loading, saving, clearing and deleting history records through the REPL interface.

7. Version Control Git Best Practices:  

Best practices such as branching for feature development ans using logical, meaningful commits messages are followed throughout this projetc life cycle

8. Testing Coverage

The project was tested through pytest. All modules, functions, and features have been tested using pytest, pylint, and coverage features. 

## Designe Patterns:

### Command design 

This project utilizes the Command design pattern to enhance modularity and flexibility. All the operation functions utilize the command class. 

![Image](https://github.com/user-attachments/assets/11d1b8b6-90ba-43d9-97be-327ddd24d134)

### Factory Design Pattern

The Factory Design Pattern enhances flexibility and decoupling by delegating object creation to a separate method. This approach allows for modifications in the instantiation process without impacting client code, making it easier to manage and extend.

A common use case is loading plugins dynamically from designated directories and creating instances of their classes without explicitly specifying their concrete implementations.

<img width="759" alt="Image" src="https://github.com/user-attachments/assets/842d441d-42f2-41d9-8b6c-88bc8309cf34" />

### Facade Design Pattern

The Facade Design Pattern provides a simplified interface to complex subsystems. It is particularly useful for handling intricate operations such as:

Writing history data to a CSV file
Importing data from a CSV file
Interacting with Pandas DataFrames
This pattern abstracts away the complexities of data handling, allowing client code to work with a single, unified interface instead of dealing with multiple subsystems.

<img width="764" alt="Image" src="https://github.com/user-attachments/assets/9d381d46-9577-4605-8e84-8c29c5c51ac2" />

### Singleton Patter

The Singleton Design Pattern ensures that only one instance of a class exists and provides a global access point to it. In the context of managing a history of calculations, the Singleton pattern enforces a single source of truth, preventing multiple instances from creating inconsistent states.

<img width="751" alt="Image" src="https://github.com/user-attachments/assets/b2244212-e82f-4d2b-abbc-689cf818b534" />

### DRY / LBYL / EAFP

There are many cases where DRY,LBYL and EAFP design principles are used in this project.

Below are some examples:

i. DRY (Don't Repeat Yourself):

The DRY principle ensures that repetitive code is extracted into reusable functions, reducing redundancy and improving maintainability. Below is an example where a common function for loading plugins is created and called multiple times throughout the project.

<img width="544" alt="Image" src="https://github.com/user-attachments/assets/9f82cfc2-ed02-42d9-8fb4-dc97ad4cc0ba" />

ii. LBYL (Look Before you Leap):

The LBYL (Look Before You Leap) programming style checks ahead of time whether an operation is safe to perform, rather than assuming it will work and handling exceptions. 

<img width="544" alt="Image" src="https://github.com/user-attachments/assets/9f82cfc2-ed02-42d9-8fb4-dc97ad4cc0ba" />

iii. EAFP (Easier to Ask for Forgiveness than Permission):

The EAFP principle allows the code to attempt an operation first without checking conditions upfront and handle exceptions if they occur. This is different from LBYL (Look Before You Leap), where checks are performed before execution.

<img width="670" alt="Image" src="https://github.com/user-attachments/assets/62531a8b-b8b6-4295-a73f-0f7b41c24bb5" />

## Environment Variables

At application startup, environmental variables are loaded from a .env file using python-dotenv. These variables are then used to configure logging, ensuring that the logging configuration path (logging_conf_path) is dynamically set.

<img width="515" alt="Image" src="https://github.com/user-attachments/assets/83509b8d-4be6-4d05-b81b-9cf15a6a11d0" />

## Logging

Logging is essential for debugging, runtime monitoring, and operational tracking. Below are examples demonstrating how logging is used to:

✔ Inform users about interactive calculator operations (INFO).
✔ Warn users when they enter invalid commands (WARNING).
✔ Capture critical errors (ERROR).

<img width="592" alt="Image" src="https://github.com/user-attachments/assets/75c7ff0e-4114-49d4-a78d-3a6823631df4" />

## Testing:

### Test Commands:

1. pytest

2. pytest --pylint

3. pytest --pylint --cov

### Test Results:

![Image](https://github.com/user-attachments/assets/3c2e1707-6c9b-4606-9397-b1159e3850cd)
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a9985ec4-4d5f-4b08-9818-3ff68740b87f" />
<img width="1177" alt="Image" src="https://github.com/user-attachments/assets/d49ff527-c8ef-4582-bcd0-0dae641e440f" />
<img width="1146" alt="Image" src="https://github.com/user-attachments/assets/17936b16-6dca-405f-b2ec-b592b88e417a" />

### Log file output

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/cffc604d-3a65-4451-ba91-4ba3916ccf06" />

## My Calculator App Video:
