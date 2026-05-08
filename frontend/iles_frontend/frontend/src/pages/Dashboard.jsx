import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function Dashboard() {
  const { user, role, setUser, setToken, setRole } = useAuth();

  const navigate = useNavigate();

  const logout = () => {
    setUser(null);
    setToken(null);
    setRole(null);

    navigate("/");
  };

  return (
    <div style={styles.app}>
      <aside style={styles.sidebar}>
        <div>
          <h1 style={styles.logo}>🎓 ILES</h1>

          <p style={styles.logoText}>
            Industrial Liaison & Evaluation System
          </p>

          <nav style={styles.nav}>
            <button style={styles.activeNav}>
              🏠 Dashboard
            </button>

            <button
              style={styles.navBtn}
              onClick={() => navigate("/placements")}
            >
              💼 Placements
            </button>

            <button
              style={styles.navBtn}
              onClick={() => navigate("/logs")}
            >
              📘 Weekly Logs
            </button>

            <button
              style={styles.navBtn}
              onClick={() => navigate("/evaluations")}
            >
              ⭐ Evaluations
            </button>

            <button
              style={styles.navBtn}
              onClick={() => navigate("/profile")}
            >
              👤 Profile
            </button>
          </nav>
        </div>

        <button style={styles.logout} onClick={logout}>
          🚪 Logout
        </button>
      </aside>

      <main style={styles.main}>
        <div style={styles.topbar}>
          <span style={styles.menu}>☰</span>

          <div style={styles.userBox}>
            <div style={{ position: "relative" }}>
              <button
                onClick={() =>
                  alert(
                    "📢 Notifications\n\n• Weekly log deadline is Friday\n• Profile updated successfully\n• No new evaluations yet"
                  )
                }
                style={{
                  border: "none",
                  background: "transparent",
                  fontSize: "22px",
                  cursor: "pointer",
                }}
              >
                🔔
              </button>

              <span
                style={{
                  position: "absolute",
                  top: "-5px",
                  right: "-5px",
                  background: "red",
                  color: "white",
                  borderRadius: "50%",
                  width: "18px",
                  height: "18px",
                  fontSize: "11px",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                3
              </span>
            </div>

            <span style={styles.avatar}>👤</span>

            <strong>
              {user?.username || "Student"}
            </strong>
          </div>
        </div>

        <section style={styles.hero}>
          <div>
            <p style={styles.small}>
              Welcome back,
            </p>

            <h2 style={styles.name}>
              {user?.username || "Student"} 👋
            </h2>

            <p style={styles.subtitle}>
              Here’s what’s happening with your industrial training.
            </p>

            <p style={{ marginTop: "10px", color: "#6b7280" }}>
              Role: {role || "student"}
            </p>
          </div>

          <div style={styles.illustration}>
            👩‍💻
          </div>
        </section>

        <section style={styles.stats}>
          <Card
            icon="💼"
            title="Placements"
            value="1"
            note="Active Placement"
            color="#7c3aed"
          />

          <Card
            icon="📘"
            title="Weekly Logs"
            value="4"
            note="Logs Submitted"
            color="#2563eb"
          />

          <Card
            icon="⭐"
            title="Evaluations"
            value="0"
            note="Completed"
            color="#16a34a"
          />

          <Card
            icon="👤"
            title="Profile"
            value="100%"
            note="Profile Complete"
            color="#f97316"
          />
        </section>

        <h2 style={styles.sectionTitle}>
          Quick Access
        </h2>

        <section style={styles.quick}>
          <QuickCard
            icon="💼"
            title="Placements"
            text="View your placement details and supervisor information."
            onClick={() => navigate("/placements")}
          />

          <QuickCard
            icon="📘"
            title="Weekly Logs"
            text="Submit and manage your weekly activity logs."
            onClick={() => navigate("/logs")}
          />

          <QuickCard
            icon="⭐"
            title="Evaluations"
            text="View your evaluations and feedback."
            onClick={() => navigate("/evaluations")}
          />

          <QuickCard
            icon="👤"
            title="Profile"
            text="Update your profile information."
            onClick={() => navigate("/profile")}
          />
        </section>

        <div style={styles.reminder}>
          <span style={styles.reminderIcon}>
            📅
          </span>

          <div>
            <h3>Important Reminder</h3>

            <p>
              Make sure to submit your weekly logs on time and keep your profile up to date.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}

function Card({ icon, title, value, note, color }) {
  return (
    <div style={styles.card}>
      <div style={{ ...styles.iconBox, color }}>
        {icon}
      </div>

      <div>
        <p style={styles.cardTitle}>
          {title}
        </p>

        <h2 style={styles.cardValue}>
          {value}
        </h2>

        <p style={{ ...styles.note, color }}>
          {note}
        </p>
      </div>
    </div>
  );
}

function QuickCard({ icon, title, text, onClick }) {
  return (
    <div style={styles.quickCard}>
      <div style={styles.bigIcon}>
        {icon}
      </div>

      <h3>{title}</h3>

      <p>{text}</p>

      <button
        style={styles.arrowBtn}
        onClick={onClick}
      >
        →
      </button>
    </div>
  );
}

const styles = {
  app: {
    minHeight: "100vh",
    display: "flex",
    background: "#f8f7ff",
    fontFamily: "Arial, sans-serif",
    color: "#1f2937",
  },

  sidebar: {
    width: "250px",
    background: "white",
    padding: "28px 18px",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    boxShadow: "2px 0 15px rgba(0,0,0,0.06)",
  },

  logo: {
    color: "#6d28d9",
    margin: 0,
  },

  logoText: {
    fontSize: "13px",
    color: "#6b7280",
    lineHeight: 1.5,
  },

  nav: {
    marginTop: "40px",
    display: "flex",
    flexDirection: "column",
    gap: "12px",
  },

  navBtn: {
    padding: "13px",
    border: "none",
    background: "transparent",
    textAlign: "left",
    fontSize: "15px",
    cursor: "pointer",
    borderRadius: "12px",
  },

  activeNav: {
    padding: "13px",
    border: "none",
    background: "linear-gradient(135deg, #7c3aed, #6d28d9)",
    color: "white",
    textAlign: "left",
    fontSize: "15px",
    cursor: "pointer",
    borderRadius: "12px",
  },

  logout: {
    padding: "13px",
    border: "none",
    background: "#f3e8ff",
    color: "#6d28d9",
    borderRadius: "12px",
    cursor: "pointer",
    fontWeight: "bold",
  },

  main: {
    flex: 1,
    padding: "25px 45px",
  },

  topbar: {
    height: "55px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },

  menu: {
    fontSize: "24px",
  },

  userBox: {
    display: "flex",
    gap: "16px",
    alignItems: "center",
  },

  avatar: {
    background: "#ede9fe",
    color: "#6d28d9",
    padding: "10px",
    borderRadius: "50%",
  },

  hero: {
    marginTop: "30px",
    background: "white",
    padding: "35px",
    borderRadius: "24px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    boxShadow: "0 10px 25px rgba(0,0,0,0.05)",
  },

  small: {
    fontSize: "18px",
    fontWeight: "bold",
  },

  name: {
    fontSize: "36px",
    color: "#6d28d9",
    margin: "8px 0",
  },

  subtitle: {
    color: "#6b7280",
  },

  illustration: {
    fontSize: "95px",
  },

  stats: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "22px",
    marginTop: "28px",
  },

  card: {
    background: "white",
    padding: "24px",
    borderRadius: "20px",
    display: "flex",
    gap: "18px",
    alignItems: "center",
    boxShadow: "0 10px 25px rgba(0,0,0,0.05)",
  },

  iconBox: {
    background: "#f3f4f6",
    padding: "18px",
    borderRadius: "18px",
    fontSize: "28px",
  },

  cardTitle: {
    margin: 0,
    color: "#4b5563",
    fontWeight: "bold",
  },

  cardValue: {
    margin: "8px 0",
    fontSize: "30px",
  },

  note: {
    margin: 0,
    fontSize: "14px",
    fontWeight: "bold",
  },

  sectionTitle: {
    marginTop: "35px",
  },

  quick: {
    display: "grid",
    gridTemplateColumns: "repeat(4, 1fr)",
    gap: "22px",
  },

  quickCard: {
    background: "white",
    padding: "28px",
    borderRadius: "22px",
    textAlign: "center",
    boxShadow: "0 10px 25px rgba(0,0,0,0.05)",
  },

  bigIcon: {
    fontSize: "46px",
  },

  arrowBtn: {
    marginTop: "15px",
    padding: "8px 22px",
    border: "none",
    borderRadius: "12px",
    background: "#ede9fe",
    color: "#6d28d9",
    fontSize: "20px",
    cursor: "pointer",
  },

  reminder: {
    marginTop: "35px",
    background: "#faf5ff",
    border: "1px solid #e9d5ff",
    padding: "22px",
    borderRadius: "20px",
    display: "flex",
    gap: "18px",
    alignItems: "center",
  },

  reminderIcon: {
    fontSize: "42px",
  },
};

export default Dashboard;