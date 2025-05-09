# restaurant_management_system_using_python_mysql_and_mvc_architecture

 

# **Restaurant Management System (FoodieHub) 🚀**  
A **Python-based restaurant management system** using **MySQL** and the **Model-View-Controller (MVC) architecture**. This system efficiently manages menu items, orders, users, and billing through a **Command Line Interface (CLI)**.  

## 📌 **Project Overview**  
The **FoodieHub Project** aims to streamline restaurant operations by providing an efficient way to **manage orders, menu items, users, and billing**. Designed with scalability in mind, it follows the **MVC architecture** for organized code separation.  

## 🔧 **Tech Stack**  
- **Programming Language:** Python  
- **Database:** MySQL  
- **Architecture:** Model-View-Controller (MVC)  
- **Interface:** Command Line Interface (CLI)  

## 📁 **Project Structure**  
```
foodiehub_project/
│
├── config/
│   └── db_config.py            # DB credentials
│
├── model/
│   ├── database.py             # Database connection handler
│   ├── menu.py                 # Menu item management
│   ├── order.py                # Order creation and management
│   ├── user.py                 # User management
│   └── bill.py                 # Bill generation and management
│
├── controller/
│   └── app_controller.py       # Logic between view and model
│
├── view/
│   └── cli.py                  # Command Line Interface (CLI)
│
└── main.py                     # Entry point
```  

## 🚀 **Features**  
✔ **User Management** – Manage customer and staff information  
✔ **Menu Management** – Add, update, and remove menu items  
✔ **Order Processing** – Create, update, and delete customer orders  
✔ **Billing System** – Generate invoices based on orders  
✔ **Database Integration** – Store and retrieve restaurant data efficiently  
✔ **Role-Based Access** – Restrict functionalities based on user roles  
✔ **Error Handling & Validation** – Ensure data integrity  

## 🎯 **Objectives**  
- Implement a robust **order and menu management** system  
- Utilize **MySQL** for secure **data storage** and retrieval  
- Maintain clear separation of concerns using **MVC architecture**  
- Provide an **intuitive CLI-based interface**  
- Ensure **scalability and maintainability**  

## 🗄️ **Database Schema Overview**  
Here's a **brief description** of the database schema:  
- **Users Table**: Stores user details (ID, name, role, contact info).  
- **Menu Table**: Stores menu items (ID, name, price, category).  
- **Orders Table**: Tracks customer orders (ID, user_id, items, status).  
- **Bills Table**: Stores invoice details for orders.  

_A detailed **ER Diagram** could be included in the repository for better visualization._  

## 📌 **Installation & Setup**  
1️⃣ Clone the repository:  
   ```bash
   git clone https://github.com/Israt1063/FoodieHub_Project.git
   cd FoodieHub_Project
   ```  
2️⃣ Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3️⃣ Set up the database by configuring **config/db_config.py**  
4️⃣ Run the project:  
   ```bash
   python main.py
   ```  


## 🔮 **Future Enhancements**  
✅ **GUI version** – Upgrade the interface to a graphical design  
✅ **Analytics Dashboard** – Provide insights on sales, popular menu items, etc.  
✅ **Online Ordering API** – Integrate with third-party food delivery services  
✅ **Multiple Branch Support** – Extend system functionality for restaurant chains  

## 🔗 **GitHub Repository**  
🔗 [GitHub Repository](https://github.com/Israt1063/FoodieHub_Project)  

---

