import { useNavigate } from "react-router-dom";

function Logs() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f8f7ff",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <button
        onClick={() => navigate("/dashboard")}
        style={{
          padding: "10px 18px",
          border: "none",
          borderRadius: "10px",
          background: "#2563eb",
          color: "white",
          cursor: "pointer",
        }}
      >
        ← Dashboard
      </button>

      <h1 style={{ marginTop: "25px", color: "#2563eb" }}>
        📘 Weekly Logs
      </h1>

      <div
        style={{
          marginTop: "25px",
          background: "white",
          padding: "30px",
          borderRadius: "20px",
          boxShadow: "0 10px 25px rgba(0,0,0,0.05)",
        }}
      >
        <h2>Submitted Logs</h2>

        <p>You have not submitted any weekly logs yet.</p>

        <div
          style={{
            marginTop: "20px",
            background: "#dbeafe",
            padding: "20px",
            borderRadius: "16px",
          }}
        >
          <h3>📝 Log Status</h3>
          <p>No logs available.</p>
        </div>
      </div>
    </div>
  );
}

export default Logs;