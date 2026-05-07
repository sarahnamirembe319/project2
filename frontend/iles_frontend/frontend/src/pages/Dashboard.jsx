import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const { user, role, token } = useAuth();

  return (
    <div style={{ padding: "40px" }}>
      <h1>DASHBOARD WORKING</h1>

      <p>
        Username: {user?.username || "No User"}
      </p>

      <p>
        Role: {role || "No Role"}
      </p>

      <p>
        Token: {token ? "YES" : "NO"}
      </p>
    </div>
  );
}

export default Dashboard;