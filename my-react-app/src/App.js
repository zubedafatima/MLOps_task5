import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/store-data", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
      });

      if (!response.ok) {
        throw new Error("Failed to store data");
      }

      // Reset form fields after successful submission
      setName("");
      setEmail("");
      alert("Data stored successfully");
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to store data");
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>MLOps Task 5</h1>
      </header>
      <body>
        <h2>Enter data</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(event) => setName(event.target.value)}
          />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
          <button type="submit">Submit</button>
        </form>
      </body>
    </div>
  );
}

export default App;
