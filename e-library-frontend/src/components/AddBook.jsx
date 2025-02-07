import React, { useState } from "react";

const AddBook = ({ onBookAdded }) => {
  // State for form inputs
  const [book, setBook] = useState({
    title: "",
    author: "",
    published_year: "",
    isbn: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  // Handle input changes
  const handleChange = (e) => {
    setBook({ ...book, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess("");

    try {
      const response = await fetch("http://localhost:8000/books", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
      });

      if (!response.ok) {
        throw new Error("Failed to add book");
      }

      const data = await response.json();
      setSuccess("Book added successfully!");
      setBook({ title: "", author: "", published_year: "", isbn: "" }); // Reset form
      onBookAdded(); // Refresh book list
    } catch (error) {
      setError(error.message);
    }

    setLoading(false);
  };

  return (
    <div>
      <h2>Add a New Book</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {success && <p style={{ color: "green" }}>{success}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="title"
          placeholder="Title"
          value={book.title}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="author"
          placeholder="Author"
          value={book.author}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="published_year"
          placeholder="Published Year"
          value={book.published_year}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="isbn"
          placeholder="ISBN (Optional)"
          value={book.isbn}
          onChange={handleChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Adding..." : "Add Book"}
        </button>
      </form>
    </div>
  );
};

export default AddBook;
