import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import { useAuth } from "../context/AuthContext";
import { getLogs, updateLogStatus } from "../services/api";

function ReviewLog(){
    const {token, role }= useAuth();
    const {id} = useParams();
    const navigate = useNavigate();

    const [log, setLog] = useState(null);
    const [comment , setComment] = useState("");
    const [error, setError]   = useState("");
    const [loading, setLoading] = useState(false);

    const userRole = (role || "").toLowerCase().trim();

    useEffect(()=>{
        async function loadLog(){
            try {
                if (!token) return;
                const logs=await getLogs(token);
                const foundLog = logs.find((item)=> String(item.id)=== String(id));

                if (!foundLog){
                    setError("Log not found or you are not allowed to review this log.");
                    return;
                }

                setLog(foundLog);
                setComment(foundLog.review_comment || "");

            } catch (err) {
                console.error("Failed to load log:",err);
                setError(err.message || "Failed to load log.");
            }
        }
        loadLog();

    }, [token , id]);

    if (userRole !=="supervisor" && userRole !=="admin") {
        return (
            <>
                <Navbar />
                <div style={styles.container}>
                    <h2>Access denied</h2>
                    <p>Only supervisors / admins can review logs.</p>

                </div>
            </>
        );
    }
    const handleReview = async (newState)=>{
        if (!comment.trim()) {
            setError("Please enter a review comment.");
            return;
        }
        setLoading(true);
        setError("");

        try {
            await updateLogStatus(token, id , newState, comment);
            navigate("/dashboard");

        } catch (err){
            console.error("Review error:",err);
            setError(err.message || "Failed to review log.");
        } finally {
            setLoading(false);
        }
    };
    return (
        <>
            <Navbar/>
            <div style={styles.container}>
                <h1>Review WeeklyLog</h1>

                {error && <p style={styles.error}>{error}</p>}
                {!log ?(
                    <p>Loading log...</p>
                ) : (
                    <div style={styles.card}>
                        <div style={styles.section}>
                            <h2>Log Details</h2>

                            <p>
                                <strong>Student:</strong>{""}
                                {log.student_name || log.student || "-"}
                            </p>
                            <p>
                                <strong>Week:</strong> Week {log.week_number}
                            </p>
                            <p>
                                <strong>Start Date:</strong> {log.start_date}
                            </p>
                            <p>
                                <strong>End Date:</strong> {log.end_date}
                            </p>
                            <p>
                                <strong>Status:</strong>{" "}
                                <span style={getStatusStyle(log.state)}>{log.state}</span>
                            </p>

                        </div>
                        <div style={styles.section}>
                            <label style={styles.label}>
                                Review Comment
                                <textarea
                                    value={comment}
                                    onChange={(e)=> setComment(e.target.value)} 
                                    placeholder="Enter feedback for the student..."
                                    style={styles.textarea}
                                />
                            </label>
                        </div>

                        {log.state==="submitted"? (
                            <div style={styles.actions}>
                                <button
                                    onClick={()=>handleReview("Approved")}
                                    disabled={loading}
                                    style={styles.approveButton}
                                >
                                    {loading? "Processing...":"Approve"}
                                </button>
                                <button 
                                    onClick={()=>handleReview("Rejected")}
                                    style={styles.cancelButton}
                                >
                                    Cancel
                                </button>
                            </div>
                        ):(
                            <div style={styles.lockedBox}>
                                <p>
                                    This log is already <strong>{log.state}</strong>. No further action is allowed

                                </p>

                                <button
                                    onClick={()=> navigate("/dashboard")}
                                    style={styles.cancelButton}
                                >
                                    Back to Dashboard
                                </button>
                        </div> 

                        )}
                    </div>
                )}
            </div>
        </>
    );
}
function getStatusStyle(state){
    const base={
        color:"white",
        padding:"4px 10px",
        borderRadius:"12px",
        fontWeight:"bold",
        fontSize:"13px",
    };
    const colors={
        Draft:"gray",
        submitted:"orange",
        Approved:"green",
        Rejected:"crismson",
        Reviewed:"steelblue",
    };
    return {
        ...base,
        background:colors[state] || "gray",
    };
}
const styles={
    container:{
        padding:20,
        maxWidth:700,
        margin:"0 auto",
        fontFamily:"Arial, sans-serif",
    },
    card:{
        background:"white",
        padding:24,
        borderRadius:12,
        boxShadow:"0 2px 8px rgba(0,0,0,0.12)",
    },
    section:{
        marginBottom:20,
    },
    label:{
        display:"flex",
        flexDirection:"column",
        fontWeight:"bold",
    },
    textarea:{
        marginTop:8,
        minHeight:120,
        padding:12,
        border:"1px solid #ccc",
        borderRadius:6,
        resize:"vertical",
        fontFamily:"Arial, sans-serif",
    },
    actions:{

        display:"flex",
        gap:10,
        flexWrap:"wrap",

    },
    approveButton:{
        background:"green",
        color:"white",
        border:"none",
        padding:"10px 16px",
        borderRadius:6,
        cursor:"pointer",
        fontWeight:"bold",
    },
    rejectButton: {
    background: "crimson",
    color: "white",
    border: "none",
    padding: "10px 16px",
    borderRadius: 6,
    cursor: "pointer",
    fontWeight: "bold",
  },

  cancelButton: {
    background: "gray",
    color: "white",
    border: "none",
    padding: "10px 16px",
    borderRadius: 6,
    cursor: "pointer",
    fontWeight: "bold",
  },

  lockedBox: {
    background: "#f8f9fa",
    padding: 15,
    borderRadius: 8,
    color: "#555",
  },

  error: {
    color: "red",
    background: "#ffeaea",
    padding: 10,
    borderRadius: 6,
  },

}
export default ReviewLog;