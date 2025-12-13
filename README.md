# Redcat-Restaurant_Order_Processor

Project Overview
This project implements a backend logic processor for Redcat Restaurant orders, calculating the total price and  GST, and integrates this logic with an interactive web front-end using the Streamlit framework.

Features:
-Core Logic: calculation of order subtotal and GST (10%) calculation on the inclusive price.
-Web UI: Interactive interface built with Streamlit .
-Unit Testing: Comprehensive unit tests using the standard Python unittest module 

 Getting Started
 Prerequisites
 -Python3.
 -Streamlit

-Clone the Repository:git clone https://github.com/eldhoaleyas/Redcat-Restaurant_Order_Processor.git
-Create and Activate Virtual Environment:It is crucial to work inside a virtual environment to manage dependencies.
-Create the environment:python3 -m venv .venv
-Activate the environment: source .venv/bin/activate
-Install Dependencies:pip install -r requirements.txt

Running the Application
-To run the app : streamlit run app.py
-Access: The command will launch the application, 
-Running Unit Tests:The core calculation logic is verified using Python's unittest framework
-Ensure Environment is Active: Make sure (.venv) is visible in your terminal prompt.
-Execute the Test Script: python3 test_app.py

Project Structure: 
Redcat-Restaurant_Order_Processor/
├── app.py             # Contains the Streamlit UI and the core calculation logic.
├── test_app.py        # Unit tests for the calculate_order function.
├── requirements.txt   # List of Python dependencies (including Streamlit).
└── README.md         
