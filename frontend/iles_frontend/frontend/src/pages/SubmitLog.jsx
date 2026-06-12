
import { use, useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { useNavigate } from "react-router-dom";
import {useAuth} from "../context/AuthContext";
import {createLog , getSupervisors} from "../services/api";

function SubmitLog() {
    const { token , role } = useAuth();
    const navigate = useNavigate();

    // 1. STATE for each form field
    const [weekNumber, setWeekNumber]= useState("");
    const [startDate, setStartDate] = useState("")
    const [endDate, setEndDate] = useState("");
    const [supervisorId,setSupervisorId]= useState("");
    const [studentId, setStudentId]= useState("");
    const [message, setMessage]=useState("");
    const [supervisors, setSupervisors]=useState([]);

    const [error, setError]= useState("");
    const [loading, setLoading]= useState("false");

    useEffect(() => {
        async function loadSupervisors() {
            try {
                if (!token) return ;

                const data = await getSupervisors(token);
                setSupervisors(data);

            } catch (err) {
                console.error("Failed to load supervisors:", err);
                setError("Failed to load supervisors");
            }
        }
        loadSupervisors();
    }, [token]);
    

    // 2. SUBMIT HANDLER (just logs for now)
    const handleSubmit= async (e)=>{
        e.preventDefault();
        setError("");
        setLoading(true);
        
        const newLog = {
            week_number:weekNumber,
            start_date: startDate,
            end_date: endDate,
            supervisor: supervisorId,
            student: studentId,
        };
        console.log ("Submitting Log:", newLog)

        try {
            const created= await createLog(token, newLog);
            console.log("Log Created:", created);
            navigate("/dashboard"); // Redirect to dashboard after successful submission
        } catch (err) {
            console.error(err);
            setError(err.message || "Failed to submit log");

        } finally {
            setLoading(false);
        }
        
    };

    if (role !=="student"){
        return (
            <>
              <Navbar />
              <div  style={{padding: 20, textAlign:"center"}}>
                <h2>Access denied</h2>
                <p> Only students can submit weekly logs.</p>
              </div>
           </>
        );
    }

    return (
        <>
            <Navbar  />
            <div style={styles.container}>
                <h1>Submit Weekly Log</h1>

                <form onSubmit={handleSubmit} style={styles.form}>
                    {/* Week Number */}
                    <label style = {styles.label}>
                        Week Number
                        <input
                            type="number"
                            value={weekNumber}
                            onChange={(e) => setWeekNumber(e.target.value)}
                            required
                            style={styles.input}

                        />
                    </label>
                    
                    {/* Start Date */}
                    <label style={styles.label}>
                        Start Date 
                        <input
                            type="date"
                            value={startDate}
                            onChange={(e)=> setStartDate(e.target.value)}
                            required
                            style={styles.input}
                        />   
                    </label>
                    
                    {/* End Date */}
                    <label style={styles.label}>
                        End Date 
                        <input
                            type="date"
                            value={endDate}
                            onChange={(e)=> setEndDate(e.target.value)}
                            required
                            style={styles.input} 
                        />
                    </label>

                    {/* Supervisor (manual ID for now) */}
                    <label style={styles.label}>
                        Supervisor ID 
                        <select
                            value={supervisorId}
                            onChange={(e)=> setSupervisorId(e.target.value)}
                            required
                            style={styles.input}
                        >
                            <option value="">select supervisor</option>
                            {supervisors.map((supervisor) => (
                                <option key= {supervisor.id} value={supervisor.id}>
                                    {supervisor.username}
                                </option>
                            ))}
                        </select>
                    </label>

                    <button type="submit" style={styles.button}>
                        Submit Log
                    </button>
                </form>

                {message &&<p style ={{marginTop:10}}>{message}</p>}
            </div>
        </>
    );
}
const styles={
    container:{
        padding:20,
        maxWidth:600,
        margin:"0 auto",
    },

    form:{
        display:"flex",
        flexDirection:"column",
        gap:15,
        background:"#f8f9fa",
        padding:20,
        borderRadius:8,
    },
    label:{
        display:"flex",
        flexDirection:"column",
        fontWeight:"bold",
    },
    input:{
        marginTop:5,
        padding:8,
        border:"1px solid #ccc",
        borderRadius:4,
    },
    button:{
        padding:"10px 16px",
        border:"none",
        background:"#1565c0",
        color:"white",
        fontWeight:"bold",
        cursor:"pointer",
    },

};


export default SubmitLog;