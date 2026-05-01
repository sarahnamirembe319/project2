import  {useNavigate , Link } from  "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {useState , useEffect } from "react";
import {getNotifications, markNotificationRead } from "../services/api";

function Navbar(){
    const { user, setUser, setToken, token } = useAuth();
    const navigate = useNavigate();
    const [notifications , setNotifications] = useState([]);
    const [open, setOpen] = useState(false);

    useEffect(() => {
        async function load() {
            try {
                if (!token) return;
                const data = await getNotifications(token);
                setNotifications(data);
            } catch (e) {
                console.error("Notification fetch error:", e);
            }
            
        }
        load();
    }, [token]);

    const unreadCount = notifications.filter((notification) => !notification.is_read).length;

    const handleBellClick = async () => {
        setOpen(!open);

        const unreadNotifications = notifications.filter((notification) => !notification.is_read);
        if (unreadNotifications.length === 0) return;

        try {
            await Promise.all(
                unreadNotifications.map((notification) =>
                    markNotificationRead(token, notification.id)
                )
            );
            setNotifications((prev) =>
                prev.map((notification) => ({
                    ...notification,
                    is_read: true,
                }))
            );
        } catch (err) {
            console.error("Failed to mark notifications as read:", err);
        }
    };

    const handleLogout = () => {
        setUser(null);
        setToken(null);
        navigate("/");

    };

    return (
        <nav style={styles.nav}>
            {/*Log */}
            <div style={styles.logo}>
              🎓 ILES
            </div>  

            {/* Links */}
            <div style={styles.links}>
                <Link to ="/dashboard" style={styles.link}>Dashboard</Link>
                <Link to ="/submit-log" style={styles.link}>Submit Log</Link>

                {/* 🔔 Notification bell */}
                <div style={{ position: "relative"}}>
                    <button onClick={handleBellClick} style={styles.bell}>
                        🔔
                        {unreadCount > 0 && (
                            <span style= {styles.badge}>{unreadCount}</span>
                        )}
                    </button>

                    {open && (
                        <div style={styles.dropdown}>
                            {notifications.length === 0 ? (
                                <p style={{ padding: 10 }}>No notifications</p>
                            ) : (
                                notifications.map((notification) => (
                                    <div key={notification.id}
                                    onClick={() => handleNotificationClick(notification)}
                                    style={{
                                        padding: 10,
                                        borderBottom: "1px solid #eee",
                                        background: notification.is_read ? "white" : "#f0f7ff"
                                    }}>
                                        {notification.message}
                                    </div>
                                ))
                            )}
                        </div>
                    )}
                </div>


                {user && <span style={styles.user}>👤 {user}</span>} 
                <button onClick={handleLogout} style={styles.logout}>
                    Logout
                </button>
            </div>
        </nav> 
                    
    );
}
//Basic styles
const styles={
    nav: {
        backgroundColor: "#f0f0f0",
        padding: "1rem",
        borderBottom: "1px solid #ccc",
        display: "flex",
        justifyContent: "space-between",
        alignItems:"center",
    },
    logo: {
        fontSize: "1.5rem",
        fontWeight: "bold"
    },
    links: {
        display: "flex",
        alignItems: "center",
        gap: "1rem"
    },
    link: {
        textDecoration: "none",
        color: "#333"
    },
    user: {
        marginRight: "1rem"
    },
    logout: {
        backgroundColor: "#dc3545",
        color: "#fff",
        border: "none",
        padding: "0.5rem 1rem",
        cursor: "pointer"
    },
    bell:{
        background: "transparent",
        border: "none",
        fontSize: 22,
        position: "relative",
        cursor: "pointer"
    },
    badge: {
    position: "absolute",
    top: -2,
    right: -6,
    background: "red",
    color: "white",
    borderRadius: "50%",
    fontSize: 10,
    width: 16,
    height: 16,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  dropdown: {
    position: "absolute",
    top: 35,
    right: 0,
    width: 280,
    background: "white",
    border: "1px solid #ddd",
    boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
    borderRadius: 6,
    zIndex: 10,},
};


export default Navbar;