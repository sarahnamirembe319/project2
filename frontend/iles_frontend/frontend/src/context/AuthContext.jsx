import { createContext, useState , useContext } from "react";

const AuthContext=createContext(null);

export function AuthProvider({children}) {
    const [user , setUser]=useState(null);
    const [token, setToken]=useState(null);
    const [role, setRole]=useState(null);

    const value={user, token,role,  setUser, setToken,setRole};

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );    
}
export default AuthProvider;
export function useAuth(){
    return useContext(AuthContext);
}