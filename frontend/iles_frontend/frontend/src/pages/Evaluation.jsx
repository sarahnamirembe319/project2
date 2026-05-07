import {useEffect , useState} from "react";
import Navbar from "../components/Navbar";
import {useAuth } from "../context/AuthContext";
import {getStudents, getEvaluationCriteria,createEvaluation } from "../services/api";

function Evaluation() {
    const {token,role }=useAuth();
    console.log("EVALUATION ROLE:", role);
    

    const [students,setStudents]=useState([]);
    const [ criteria, setCriteria]=useState([]);

    const [studentId, setStudentId]=useState("");
    const [criteriaId, setCriteriaId]=useState("");
    const [comments, setComments]=useState("");
    const [score, setScore]=useState("");

    const [error, setError]=useState("");
    const [loading, setLoading]=useState(false);
    const [success, setSuccess]=useState("");

    useEffect(()=>{
        async function loadData() {
            try{
                if(!token) return;

                const studentsData = await getStudents(token);
                const criteriaData = await getEvaluationCriteria(token);

                setStudents(studentsData);
                setCriteria(criteriaData);
            } catch (err) {
              setError(err.message || "Failed to load evaluation data");
                
            }
        }
        loadData();
    },[token]);

    const normalizedRole =(role || "").toLowerCase().trim();
    if (normalizedRole!=="supervisor" && normalizedRole !=="admin") {
        return (
            <>
                <Navbar />
                <div style= {styles.container}>
                    <h2>Access denied</h2>
                    <p>Only supervisors/admin can submit evaluations.</p>
                </div>
            </>
        );
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        console.log("SUBMIT CLICKED");
        setError("");
        setSuccess("");
        setLoading(true);

        const evaluationData = {
            student:studentId,
            criteria:criteriaId,
            performance_score:score,
            comments:comments,

        };
        console.log("Evaluation data:", evaluationData);

        try {
            const created = await createEvaluation(token , evaluationData);
            console.log("Evalaution created:", created);

            setSuccess("Evaluation submitted sucessfully");
            setStudentId("");
            setCriteriaId("");
            setScore("");
            setComments("");

        }   catch (err){ 
            console.error(err);
            setError(err.message || "Failed to submit evaluation");

        } finally {
            setLoading(false);
        }

    };
    return (
        <>
            <Navbar />
            
            <div style= {styles.container}>
                <h1>Submit Evaluation</h1>
                <form onSubmit={handleSubmit} style={styles.form}>
                    <label style={styles.label}>
                        Student
                        <select 
                            value={studentId}
                            onChange={(e)=> setStudentId(e.target.value)}
                            required
                            style={styles.input}
                        >
                            <option value="">Select student</option>
                            {students.map((student)=>(
                                <option key={student.id} value={student.id}>
                                    {student.username}
                                </option>
                            ))}
                        </select>
                    </label>

                    <label style={styles.label}>
                        Criteria
                        <select
                            value={criteriaId}
                            onChange={(e)=> setCriteriaId(e.target.value)}
                            required
                            style={styles.input}
                        >
                            <option value=""> Select criteria</option>
                            {criteria.map((item)=> (
                                <option key ={item.id} value={item.id}>
                                    {item.criteria_name}
                                </option>
                            ))}
                        </select>
                    </label>

                    <label style={styles.label}>
                        Score / 100
                        <input
                            type="number"
                            min="0"
                            max="100"
                            value={score}
                            onChange={(e)=> setScore(e.target.value)}
                            required
                            style={styles.input}
                        />
                    </label>

                    <label style = {styles.label}>
                        Comments
                        <textarea 
                        value={comments}
                        onChange={(e)=> setComments(e.target.value)}
                        placeholder="Enter evaluation comments..."
                        />
                    </label>
                    <button type="submit" style={styles.button} disabled={loading}>
                        {loading? "Submitting...":"Submit Evaluation"}
                    </button>

                    {success && <p style={{color:"green"}}>{success}</p>}
                    {error && <p style={{color:"red"}}>{error}</p>}
                </form>
            </div>
        </>               
    );

}
const styles={
    container:{
        padding:20,
        maxWidth:600,
        margin:"0 auto",
        fontFamily:"Arial, sans-serif",
    },
    form:{
        display:"flex",
        flexDirection:"column",
        gap:15,
        background:"#f8f9fa",
        padding:20,
        borderRadius:8,
    },
    labe:{
        display:"flex",
        flexDirection:"column",
        fontWeight:"bold",
    },
    input:{
        marginTop:5,
        padding:20,
        border:"1px solid #ccc",
        borderRadius:4,
    },
    button:{
        padding:"10px 16px",
        border:"none",
        background:"blue",
        color:"white",
        fontWeight:"bold",
        cursor:"pointer",
        borderRadius:4
    },
};
export default Evaluation;