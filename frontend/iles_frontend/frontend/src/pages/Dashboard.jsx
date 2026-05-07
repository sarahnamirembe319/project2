import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";
import { getPlacements, getLogs, updateLogStatus } from "../services/api";
import Navbar from "../components/Navbar";

function Dashboard() {
  const auth = useAuth();
  const token = auth?.token;
  const user = auth?.user;
  const role = auth?.role;

  const [placements, setPlacements] = useState([]);
  const [logs, setLogs] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        setError("");

        if (!token) return;

        const placementsData = await getPlacements(token);
        const logsData = await getLogs(token);

        setPlacements(Array.isArray(placementsData) ? placementsData : []);
        setLogs(Array.isArray(logsData) ? logsData : []);
      } catch (e) {
        console.error("Dashboard fetch error:", e);
        setError(e.message || String(e));
      }
    }

    if (token) load();
  }, [token]);

  const total = logs.length;
  const pending = logs.filter(
    (log) => log.state === "submitted" || log.state === "Reviewed"
  ).length;
  const approved = logs.filter((log) => log.state === "Approved").length;
  const rejected = logs.filter((log) => log.state === "Rejected").length;

  let subtitle = "Your Internship Progress";

  if (role === "admin") {
    subtitle = "Admin Dashboard";
  } else if (role === "supervisor") {
    subtitle = "Supervisor Dashboard";
  }

  const handleStatusChange = async (logId, newState) => {
    const comment = prompt(`Enter comment for ${newState}:`);
    if (comment === null) return;

    try {
      const updatedLog = await updateLogStatus(token, logId, newState, comment);

      setLogs((prev) =>
        prev.map((log) => (log.id === logId ? updatedLog : log))
      );
    } catch (e) {
      alert("Error: " + e.message);
    }
  };

  return (
    <>
      <Navbar />

      <div style={styles.page}>
        <h2 style={styles.welcome}>
          Welcome,{" "}
          <span style={{ color: "crimson" }}>
            {user?.username || user?.first_name || "User"}
          </span>
          <span style={{ color: "gray", fontSize: "14px", marginLeft: "10px" }}>
            ({role || "no role"})
          </span>
        </h2>

        <p style={styles.subtitle}>{subtitle}</p>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <div style={styles.cards}>
          <Card label="Total Logs" value={total} color="#2e7d32" />
          <Card label="Pending Reviews" value={pending} color="#f9a825" />
          <Card label="Approved Logs" value={approved} color="#1565c0" />
          <Card label="Rejected Logs" value={rejected} color="#c62828" />
        </div>

        <h3>
          {role === "student"
            ? "My Internship Logs"
            : role === "supervisor"
            ? "Logs Awaiting Your Review"
            : "All Internship Logs"}
        </h3>

        <div style={styles.tableWrap}>
          <table style={styles.table}>
            <thead>
              <tr style={styles.headRow}>
                {role !== "student" && <th style={styles.th}>Student</th>}
                <th style={styles.th}>Week</th>
                <th style={styles.th}>Start Date</th>
                <th style={styles.th}>End Date</th>
                <th style={styles.th}>Status</th>
                <th style={styles.th}>Feedback</th>
                {role !== "student" && <th style={styles.th}>Action</th>}
              </tr>
            </thead>

            <tbody>
              {logs.length === 0 ? (
                <tr>
                  <td
                    colSpan={role === "student" ? 5 : 7}
                    style={styles.empty}
                  >
                    No logs yet. Submit your first log!
                  </td>
                </tr>
              ) : (
                logs.map((log) => (
                  <tr key={log.id}>
                    {role !== "student" && (
                      <td style={styles.td}>
                        {typeof log.student === "object"
                          ? log.student?.username || log.student?.id || "-"
                          : log.student || "-"}
                      </td>
                    )}

                    <td style={styles.td}>Week {log.week_number}</td>
                    <td style={styles.td}>{log.start_date || "-"}</td>
                    <td style={styles.td}>{log.end_date || "-"}</td>

                    <td style={styles.td}>
                      <StatusBadge state={log.state} />
                    </td>

                    <td style={styles.td}>{log.review_comment || "-"}</td>

                    {role !== "student" && (
                      <td style={styles.td}>
                        {log.state === "submitted" ? (
                          <>
                            <button
                              onClick={() =>
                                handleStatusChange(log.id, "Approved")
                              }
                              style={styles.approveButton}
                            >
                              Approve
                            </button>

                            <button
                              onClick={() =>
                                handleStatusChange(log.id, "Rejected")
                              }
                              style={styles.rejectButton}
                            >
                              Reject
                            </button>
                          </>
                        ) : (
                          <span style={{ color: "gray" }}>No action</span>
                        )}
                      </td>
                    )}
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

function Card({ label, value, color }) {
  return (
    <div style={{ ...styles.card, background: color }}>
      <div style={styles.cardValue}>{value}</div>
      <div style={styles.cardLabel}>{label}</div>
    </div>
  );
}

function StatusBadge({ state }) {
  const colors = {
    Draft: "#9e9e9e",
    submitted: "#f9a825",
    Reviewed: "#1565c0",
    Approved: "#2e7d32",
    Rejected: "#c62828",
  };

  return (
    <span
      style={{
        background: colors[state] || "#9e9e9e",
        color: "white",
        padding: "4px 10px",
        borderRadius: 12,
        fontSize: 12,
        fontWeight: "bold",
        textTransform: "capitalize",
      }}
    >
      {state || "Unknown"}
    </span>
  );
}

const styles = {
  page: {
    padding: 20,
    fontFamily: "Arial, sans-serif",
  },
  welcome: {
    textAlign: "center",
    marginBottom: 0,
  },
  subtitle: {
    textAlign: "center",
    color: "#555",
    marginTop: 5,
  },
  cards: {
    display: "flex",
    gap: 20,
    justifyContent: "center",
    marginTop: 20,
    flexWrap: "wrap",
  },
  card: {
    color: "white",
    padding: "20px 28px",
    borderRadius: 12,
    minWidth: 150,
    textAlign: "center",
    boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
  },
  cardValue: {
    fontSize: 26,
    fontWeight: "bold",
  },
  cardLabel: {
    fontSize: 14,
    marginTop: 5,
  },
  tableWrap: {
    background: "white",
    borderRadius: 12,
    padding: 20,
    boxShadow: "0 2px 6px rgba(0,0,0,0.08)",
    overflowX: "auto",
  },
  table: {
    width: "100%",
    borderCollapse: "collapse",
  },
  headRow: {
    background: "#f5f5f5",
    textAlign: "left",
  },
  th: {
    padding: 10,
    borderBottom: "1px solid #ddd",
  },
  td: {
    padding: 10,
    borderBottom: "1px solid #eee",
  },
  empty: {
    textAlign: "center",
    padding: 20,
    color: "#999",
  },
  approveButton: {
    background: "green",
    color: "white",
    marginRight: 5,
    border: "none",
    padding: "4px 10px",
    borderRadius: 4,
    cursor: "pointer",
  },
  rejectButton: {
    background: "red",
    color: "white",
    border: "none",
    padding: "4px 10px",
    borderRadius: 4,
    cursor: "pointer",
  },
};

export default Dashboard;