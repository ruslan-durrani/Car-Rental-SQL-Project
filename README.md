# Car Rental SQL Database Project
### Author: **Muhammad Ruslan Babar**  
### Student ID: **24079307**  
### Course: **Data Mining and Discovery**  
### University of Hertfordshire  

---

## 📌 About This Project

This project was created for my Data Mining and Discovery module.  
I built a complete **Car Rental Database System** using SQLite.

I chose this topic because I work part-time at *International Herts Rental Car*, so I wanted to design something that feels realistic and is based on real-life rental operations.

This project includes:

- SQL database and schema  
- Python Faker script for generating data  
- Jupyter notebook for analysis  
- SQL and Python tests  
- ERD diagram  
- Data cleaning, filtering, joining, grouping and visualisations  

All data in this project is **fake** and created using the Faker library.

---

## 📁 Structure
<img width="606" height="656" alt="image" src="https://github.com/user-attachments/assets/f395aa3d-2e80-4ebf-b310-fc00da27bb08" />



---

## 🗃️ Database Description

The database contains **six tables**:

1. `Customers`  
2. `Branches`  
3. `Cars`  
4. `Car_Location`  
5. `Rentals`  
6. `Payments`  

Features included:

- Primary keys and foreign keys  
- Composite key (`car_id`, `branch_id`)  
- CHECK constraints  
- 1000+ rows of synthetic data  
- Nominal, ordinal, interval, and ratio data types  

An ERD diagram is included in the `database/` folder.

---

## 🧪 Testing

I used SQL and Python to test:

- Table existence  
- Row counts  
- Foreign key integrity  
- Missing data  
- Orphan rentals  
- Constraint validation  

All tests run inside the Jupyter notebook and in the `tests/` folder.

---

## 📊 Analysis Notebook

The Jupyter notebook includes:

### ✔ SQL Queries  
- Joins  
- Filters  
- Grouping  
- Aggregations  
- Data cleaning  

### ✔ Pandas Analysis  
- DataFrames  
- Merging  
- Filtering  
- Grouping  
- Monthly revenue  
- Popular cars  
- Customer spending  

### ✔ Visualisations  
- Monthly revenue line chart  
- Popular car models bar chart  
- Revenue by branch bar chart  

This makes the project easy to understand even for non-technical readers.

---

## 🧰 Tools Used

- SQLite  
- Python  
- Faker  
- Pandas  
- Matplotlib  
- Jupyter Notebook  
- DB Browser for SQLite  

---

## 🔒 Ethical Notes

All data is completely synthetic.  
No real customer information is used.  
This project follows ethical and GDPR-safe practices.

---

## 📬 Contact

If you want to explore or ask questions, feel free to open an issue.  
Thank you for reading my project!
