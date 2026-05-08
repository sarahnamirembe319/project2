import { useNavigate } from "react-router-dom";

function Placements() {
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
          background: "#7c3aed",
          color: "white",
          cursor: "pointer",
        }}
      >
        ← Dashboard
      </button>

      <h1 style={{ marginTop: "25px", color: "#6d28d9" }}>
        💼 Placements
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
        <h2>Current Placement</h2>

        <p>
          No placement information has been added yet.
        </p>

        <div
          style={{
            marginTop: "20px",
            display: "grid",
            gridTemplateColumns: "repeat(2, 1fr)",
            gap: "20px",
          }}
        >
          <div
            style={{
              background: "#ede9fe",
              padding: "20px",
              borderRadius: "16px",
            }}
          >
            <h3>🏢 Company</h3>
            <p>Not Assigned</p>
          </div>

          <div
            style={{
              background: "#dbeafe",
              padding: "20px",
              borderRadius: "16px",
            }}
          >
            <h3>👨‍🏫 Supervisor</h3>
            <p>Not Available</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Placements;