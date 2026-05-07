import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const { user, role } = useAuth();

  return (
    <div style={{ padding: "30px" }}>
      <h1>ILES Dashboard</h1>

      <hr />

      <h2>Welcome, {user?.username}</h2>

      <p>Role: {role}</p>

      <div style={{ marginTop: "30px" }}>
        <button>Placements</button>
        <button style={{ marginLeft: "10px" }}>
          Weekly Logs
        </button>
        <button style={{ marginLeft: "10px" }}>
          Evaluations
        </button>
        <button style={{ marginLeft: "10px" }}>
          Profile
        </button>
      </div>
    </div>
  );
}

export default Dashboard;