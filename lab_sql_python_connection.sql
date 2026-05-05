-- Selecting database
USE sakila;

-- Notes:
-- 1) Will be done in VS Code, stored in the same repo
-- 2) pip install sqlalchemy pymysql // To establish connection with SQL
-- 3) pip install python-dotenv // Installed to save password in .env file and not hard-code it in the notebook
-- 4) echo ".env" >> .gitignore // Ran in GitBash terminal so the .env file is not uploaded to the repo
-- 5) The following line of code needs to be executed if the SQL password contains special characters:

-- from dotenv import load_dotenv
-- import os
-- from urllib.parse import quote_plus
-- load_dotenv(override=True)
-- password = quote_plus(os.getenv("DB_PASSWORD"))
-- engine = create_engine(f"mysql+pymysql://root:{password}@localhost/sakila")
-- print("Connection successful!")