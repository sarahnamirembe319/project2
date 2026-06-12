//Connect to your Django API
export async function loginUser(credentials) {
    const response=await fetch("http://127.0.0.1:8000/api/token/", {
        method:"POST",
        headers:{
            "Content-Type": "application/json",
        },
        body:JSON.stringify(credentials),
        
        });

        // If login fails, throw the server message (if any
        const data = await response.json();
        if (! response.ok){
            throw new Error(data?.detail || data?.error || "Login failed");
        }
        return data;
        //return response.json();
}

export async function getLogs(token){
    const response= await fetch("http://127.0.0.1:8000/api/logs/" , {
        method: "GET" ,
        headers:{
            Authorization: `Token ${token}`,
            "Content-Type":"application/json",
        },


    });

    const data= await response.json();
    if (! response.ok) {
        throw new Error(data?.detail || "Failed to fetch logs");
    }
    return data;
}

export async function getPlacements(token) {
    const response= await fetch("http://127.0.0.1:8000/api/placements/" , {
        method:"GET",
        headers:{
            Authorization:`Token ${token}`,
            "Content-Type": "application/json",
        },
    });
    const data = await response.json();
    if(!response.ok){
        throw new Error (data?.detail || "Failed to fetch placements");
    }
    return data;
}
export async function createLog(token, logData) {
    const response = await fetch("http://127.0.0.1:8000/api/log/create/", {
        method:"POST",
        headers:{
            Authorization:`Token ${token}`,
            "Content-Type":"application/json",
        },
        body:JSON.stringify(logData),

        });

        const data= await response.json();
        if (!response.ok) {
            throw new Error(data?.detail || "Failed to create log");
        }
        return data;
    }

export async function updateLogStatus(token, logId, newState, reviewComment) {
    const response = await fetch (`http://127.0.0.1:8000/api/logs/${logId}/status/`,
        {
            method:"PATCH",
            headers:{
                Authorization:`Token ${token}`,
                "Content-Type":"application/json",
            },
            body:JSON.stringify({
                state:newState,
            review_comment: reviewComment
        }),
    
    });
    

        const data = await response.json();
        if (!response.ok) {
            throw new Error(data?.detail || "Failed to update log");
        }
        return data;
    
}
export async function getNotifications(token) {
    const response = await fetch("http://127.0.0.1:8000/api/notifications/",{
        method: "GET",
        headers: {
            Authorization:`Token ${token}`,
            "Content-Type": "application/json",

        },
    });
    const data = await response.json();
    if(! response.ok){
        throw new Error(data?.detail || "Failed to fetch notifications");

    }
    return data;
}
export async function markNotificationRead(token, notificationId) {
    const response = await fetch (`http://127.0.0.1:8000/api/notifications/${notificationId}/read/`, {
        method:"PATCH",
        headers:{
            Authorization:`Token ${token}`,
            "Content-Type": "application/json",
        },
    }
    );
    const data = await response.json();
    if (!response.ok){
        throw new Error(data?.detail || "Failed to mark notification as read");
    }  
    return data;
}
export async function getSupervisors(token) {
    const response = await fetch ("http://127.0.0.1:8000/api/supervisors/", {
        method:"GET",
        headers:{
            Authorization:`Token ${token}`,
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    if (!response.ok){
        throw new Error(data?.detail|| "Failed to load supervisors");
    }
    return data;
}