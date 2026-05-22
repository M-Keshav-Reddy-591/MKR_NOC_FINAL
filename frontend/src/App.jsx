import {

    BrowserRouter,

    Routes,

    Route,

    Navigate

} from "react-router-dom";

import Login from "./pages/auth/Login";

import AdminDashboard from "./pages/dashboard/AdminDashboard";

import EmployeeDashboard from "./pages/dashboard/EmployeeDashboard";


import AttendanceManagement from "./pages/attendance/AttendanceManagement";

import LeaveManagement from "./pages/leaves/LeaveManagement";

import ShiftSwapManagement from "./pages/swaps/ShiftSwapManagement";

import ReportsManagement from "./pages/reports/ReportsManagement";

import AdminRoute from "./routes/AdminRoute";

import EmployeeRoute from "./routes/EmployeeRoute";
import ProfileManagement from "./pages/profile/ProfileManagement";
import EmployeeManagement from "./pages/admin/EmployeeManagement";
import AdminAttendanceManagement from "./pages/admin/AdminAttendanceManagement";
import ShiftAllocation from "./pages/admin/ShiftAllocation";
export default function App() {

    const token = localStorage.getItem(
        "token"
    );

    const role = localStorage.getItem(
        "role"
    );


    return (

        <BrowserRouter>

            <Routes>

                {/* LOGIN */}

                <Route
                    path="/"
                    element={

                        token

                        ?

                        role === "admin"

                        ?

                        <Navigate to="/admin-dashboard" />

                        :

                        <Navigate to="/employee-dashboard" />

                        :

                        <Login />
                    }
                />


                {/* DASHBOARDS */}

                <Route
                    path="/admin-dashboard"
                    element={

                        <AdminRoute>

                            <AdminDashboard />

                        </AdminRoute>
                    }
                />

                <Route
                    path="/employee-dashboard"
                    element={

                        <EmployeeRoute>

                            <EmployeeDashboard />

                        </EmployeeRoute>
                    }
                />


                {/* EMPLOYEES */}

                <Route
                    path="/employees"
                    element={

                        <AdminRoute>

                            <EmployeeManagement />

                        </AdminRoute>
                    }
                />


                {/* ATTENDANCE */}

                <Route
                    path="/attendance"
                    element={

                        <EmployeeRoute>

                            <AttendanceManagement />

                        </EmployeeRoute>
                    }
                />
                <Route
                    path="/admin-attendance"
                    element={
                        <AdminRoute>
                            <AdminAttendanceManagement />
                        </AdminRoute>
                    }
                />


                {/* LEAVES */}

                <Route
                    path="/leaves"
                    element={

                        <EmployeeRoute>

                            <LeaveManagement />

                        </EmployeeRoute>
                    }
                />


                {/* SWAPS */}

                <Route
                    path="/swaps"
                    element={

                        <EmployeeRoute>

                            <ShiftSwapManagement />

                        </EmployeeRoute>
                    }
                />


                {/* REPORTS */}

                <Route
                    path="/reports"
                    element={

                        <AdminRoute>

                            <ReportsManagement />

                        </AdminRoute>
                    }
                />
                <Route
                    path="/profile"
                    element={

                    <EmployeeRoute>

                        <ProfileManagement />

                    </EmployeeRoute>
                }
                />
                <Route
                    path="/shift-allocation"
                    element={
                        <AdminRoute>
                            <ShiftAllocation />
                        </AdminRoute>
                    }
                />
            </Routes>
            

        </BrowserRouter>
    );
}