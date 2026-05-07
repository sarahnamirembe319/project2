import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const { setUser, setToken, setRole } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("https://iles-i7zm.onrender.com/api/auth/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        setError(data?.error || data?.detail || "Login failed. Please check your credentials.");
        return;
      }

      setUser(data.user);
      setToken(data.access);
      setRole(data.user?.role || null);

      navigate("/dashboard");
    } catch (err) {
      console.error("Login failed:", err);
      setError("Failed to log in. Please check your username and password.");
    }
  };

  return(
  <div>
    <h1>DASHBOARD WORKING</h1>

    <p>User: {user?.username}</p>

    <p>
      Role: {typeof role === "string" ? role : "user"}
    </p>

    <p>
      Token: {token ? "YES" : "NO"}
    </p>
  </div>
);
    
}

export default Login;