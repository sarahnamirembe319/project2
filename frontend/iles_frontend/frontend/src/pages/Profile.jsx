import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function Profile() {
  const { user, role } = useAuth();
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
          background: "#f97316",
          color: "white",
          cursor: "pointer",
        }}
      >
        ← Dashboard
      </button>

      <h1 style={{ marginTop: "25px", color: "#f97316" }}>
        👤 Profile
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
        <div
          style={{
            textAlign: "center",
            marginBottom: "30px",
          }}
        >
          <div
            style={{
              fontSize: "70px",
            }}
          >
            👤
          </div>

          <h2>{user?.username}</h2>

          <p style={{ color: "#6b7280" }}>
            Role: {role}
          </p>
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(2, 1fr)",
            gap: "20px",
          }}
        >
          <div
            style={{
              background: "#fff7ed",
              padding: "20px",
              borderRadius: "16px",
            }}
          >
            <h3>📧 Email</h3>
            <p>{user?.email || "No email available"}</p>
          </div>

          <div
            style={{
              background: "#ffedd5",
              padding: "20px",
              borderRadius: "16px",
            }}
          >
            <h3>🪪 Username</h3>
            <p>{user?.username}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile;