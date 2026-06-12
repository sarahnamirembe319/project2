import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Placements from "./pages/Placements";
import Logs from "./pages/Logs";
import Evaluations from "./pages/Evaluations";
import Profile from "./pages/Profile";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/placements" element={<Placements />} />
      <Route path="/logs" element={<Logs />} />
      <Route path="/evaluations" element={<Evaluations />} />
      <Route path="/profile" element={<Profile />} />
    </Routes>
  );
}

export default App;