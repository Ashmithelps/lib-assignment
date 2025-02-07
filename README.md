# 📚 Books Collection App

Welcome to the **Books Collection App**, a full-stack web application that allows users to manage their book collection seamlessly. This project is built using **React.js** for the frontend and **FastAPI** for the backend, providing a smooth and efficient user experience.

---

## 🚀 Features
- 📖 **View all books**: Fetch and display books dynamically from the backend.
- ➕ **Add new books**: Users can add books with a title, author, published year, and ISBN.
- ✏️ **Edit books**: Modify book details with ease.
- 🗑 **Delete books**: Remove unwanted books from the collection.
- 🔄 **Real-time updates**: Automatically refresh the book list upon any changes.

---

## 🛠 Tech Stack
### **Frontend (React.js) 📟**
- React Hooks (`useState`, `useEffect`)
- React Router for navigation
- Fetch API for backend communication

### **Backend (FastAPI) ⚡**
- Python FastAPI for handling RESTful APIs
- SQLAlchemy for database management
- Pydantic for data validation

---

## 📂 Project Structure
```
📁 books-collection-app
│── 📁 backend       # FastAPI backend
│    ├── main.py     # API routes and logic
│    ├── models.py   # Database models
│    ├── database.py # Database connection
│
│── 📁 frontend      # React.js frontend
│    ├── src
│    │   ├── components
│    │   │   ├── AddBook.jsx  # Add new books
│    │   │   ├── BookList.jsx # List all books
│    │   ├── pages
│    │   │   ├── Books.jsx    # Books page
│    │   ├── App.js          # Main application
│    ├── package.json        # Dependencies
│
│── README.md       # Project documentation
```

---

## 🔧 Setup Instructions
### **Backend (FastAPI)**
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/books-collection-app.git
   cd books-collection-app/backend
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv env
   source env/bin/activate  # (On Windows use `env\Scripts\activate`)
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
4. **Access API Documentation**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### **Frontend (React.js)**
1. **Navigate to the frontend directory**
   ```bash
   cd ../frontend
   ```
2. **Install dependencies**
   ```bash
   npm install
   ```
3. **Start the React development server**
   ```bash
   npm run dev
   ```
4. **Open in browser**
   - Navigate to: [http://localhost:5173](http://localhost:5173)

---

## 🎯 API Endpoints
| Method | Endpoint         | Description                |
|--------|-----------------|----------------------------|
| GET    | `/books`        | Fetch all books            |
| POST   | `/books`        | Add a new book             |
| PUT    | `/books/{id}`   | Update a book by ID        |
| DELETE | `/books/{id}`   | Delete a book by ID        |

---

## 🤝 Contribution
Want to improve this project? Follow these steps:
1. **Fork the repository**
2. **Create a new branch** (`feature-xyz`)
3. **Commit your changes**
4. **Push and create a Pull Request**

---

## 📜 License
This project is licensed under the **MIT License**.

📩 **For any queries, feel free to reach out!** 🚀
email- thakurashmit20@gmail.com
phone- +91 9056041020
