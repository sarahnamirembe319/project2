// the main user inetrface
import {BrowserRouter, Routes , Route} from "react-router-dom";
import Login from "./pages/Login"
import Dashboard from "./pages/Dashboard"
import AuthProvider  from "./context/AuthContext";
import ProtectedRoute from "./routes/ProtectedRoute";
import SubmitLog from "./pages/SubmitLog";

function App(){
  return(
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          {/* Public route - anyone can access */}
          <Route path="/" element={<Login/>} />
          {/* Protected route - only logged in users */}
          <Route 
            path="/dashboard" 
            element={
              <ProtectedRoute>

                <Dashboard/>
              </ProtectedRoute>
            }
          />  
          <Route 
            path="/submit-log" 
            element={
              <ProtectedRoute>
                <SubmitLog/>
              </ProtectedRoute>
            }
          />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
export default App;