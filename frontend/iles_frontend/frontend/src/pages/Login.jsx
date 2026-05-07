import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Login(){
    const [username, setUsername]=useState("");
    const [password, setPassword]=useState("");
    const [error, setError]=useState("");

    
    const { setUser, setToken , setRole }= useAuth();
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();// prevent page reload
        console.log("LOGIN CLICKED");//clears previous errors
        try {
          const response= await fetch("http://127.0.0.1:8000/api/login/",{
            method:"POST",
            headers: {
                "Content-Type":"application/json",
            },
            body: JSON.stringify({ username , password }), 
        });

        const data = await response.json();

        if (!response.ok){
            setError( data?.detail || "Login failed Please check your Credentials");
            return;
        }
        
        
         // Store user + token
         setUser(data.user);
         setToken(data.token);
         setRole(data.role);
         // redirect to dashboard 
         navigate("/dashboard");
        
        }catch (err){
        console.error("Login failed:" , err);
        setError('Failed to log in . Please check your username and password.');
        }
    };
    return (
        <form onSubmit={handleLogin}>
            <input
                type="text"
                placeholder="Username"
                onChange={(e)=> setUsername(e.target.value)}
                />
            <input
                type="password"
                placeholder="password"
                onChange={(e)=> setPassword(e.target.value)}
                />

            <button type="submit">Login</button>
            {error &&<p style={{color:'red' }}>{error}</p>}
        </form>
    );
}

export default Login;