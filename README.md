# Redbus.in-Web-Scraping
*Overview*

This project involves scraping bus schedule information from RedBus.in using Python, storing it in a MySQL database, and displaying/filtering the data using Streamlit. The scraped data includes details such as the number of available states in RedBus, bus routes within each state, and comprehensive information for each bus route (bus name, type, A/C or Non A/C, departure time, travel time, arrival time, star rating, and fare).

*Project Structure*

redbus_webscraping_python.py	: 	Python script for web scraping, data storage, and Streamlit integration.
redbus_data.sql			:	 SQL script for creating necessary tables in MySQL.
redbus_dashboard_python.py	:	Streamlit dashboard created based on the stored MySQL data. 

*Tools Used:*

Python 3.x
Selenium
Requests
MySQL Connector



*Usage*

Customize main.py as needed for specific web scraping logic and MySQL database interaction.
Run redbus_webscraping_python.py to initiate the web scraping process, store data in MySQL, and launch Streamlit for data visualization and filtering.

*Notes:*

Customization: Update sections like Overview, Setup, Dependencies, and Usage with specific details relevant to your implementation.
Database Setup: Include specific instructions for setting up MySQL and executing database.sql for table creation.

![Screenshot 2024-07-18 172711](https://github.com/user-attachments/assets/30b89bb4-99c5-4220-837d-ba436f23f093)
