import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";


function Dashboard() {
  const { user, role } = useAuth();
  const navigate = useNavigate();

  return (
    <div style={{ marginTop: "30px" }}>
  <button onClick={() => navigate("/placements")}>
    Placements
  </button>

  <button
    style={{ marginLeft: "10px" }}
    onClick={() => navigate("/logs")}
  >
    Weekly Logs
  </button>

  <button
    style={{ marginLeft: "10px" }}
    onClick={() => navigate("/evaluations")}
  >
    Evaluations
  </button>

  <button
    style={{ marginLeft: "10px" }}
    onClick={() => navigate("/profile")}
  >
    Profile
  </button>
</div>
);
}

export default Dashboard;