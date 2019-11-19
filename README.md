# Installation instructions

This assumes MySql is set up in an Ubuntu environment and that the database and schema have already been imported. I have not tested it on other environments as of yet (Dont have a Mac to test from) but if you have Windows, you can use the Windows Subsystem for Linux feature to follow along. This also assumes python and pip are already installed. 

1. Clone this directory somewhere on your environment and take note of the directory
2. Browse to that directory from Step 1 using the command line.
3. Run the following command to install all requirements for the script 
    ```pip3 install --user --requirement requirements.txt```
4. Once all requirements are installed, use the following command to create a .dotenv file. This is needed to connect to your MySQL database. 
    ```touch .env```
5. open the .env file in either an code editor or using nano if you're on linux and add the following to the .env file and save
```
DB_HOSTNAME=[The computer name that your mySQL server resides on]
DB_USERNAME=[your mySQL user's name]
DB_PASSWORD=[your mySQL user's password]
DB_NAME=[database name that the script will be connecting to]
```
6. you should be able to run the script from the command line using the following command from the directory where you cloned the project
```python3 script.py```

I've also included the raw SQL script if, for some reason, you're not able to get configured and I'm not available to help. 


