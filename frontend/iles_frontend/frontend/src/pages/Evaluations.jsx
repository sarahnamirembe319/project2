import { useNavigate } from "react-router-dom";

function Evaluations() {
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
          background: "#16a34a",
          color: "white",
          cursor: "pointer",
        }}
      >
        ← Dashboard
      </button>

      <h1 style={{ marginTop: "25px", color: "#16a34a" }}>
        ⭐ Evaluations
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
        <h2>Evaluation Results</h2>

        <p>No evaluations have been completed yet.</p>

        <div
          style={{
            marginTop: "20px",
            background: "#dcfce7",
            padding: "20px",
            borderRadius: "16px",
          }}
        >
          <h3>📊 Performance</h3>
          <p>Awaiting evaluation.</p>
        </div>
      </div>
    </div>
  );
}

export default Evaluations;