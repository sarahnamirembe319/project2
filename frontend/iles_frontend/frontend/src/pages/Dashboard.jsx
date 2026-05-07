import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const { user, role } = useAuth();

  const navigate = useNavigate();

  return (
    <div style={{ padding: "30px" }}>
      <h1>ILES Dashboard</h1>

      <hr />

      <h2>
        Welcome, {user?.username}
      </h2>

      <p>Role: {role}</p>

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
    </div>
  );
}

export default Dashboard;