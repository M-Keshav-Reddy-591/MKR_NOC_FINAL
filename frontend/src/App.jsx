import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

/* LAYOUTS */

import AdminLayout from "./layouts/AdminLayout";
import EmployeeLayout from "./layouts/EmployeeLayout";

/* PROTECTED ROUTE */

import ProtectedRoute from "./components/ProtectedRoute";
import ChangePassword from "./pages/profile/ChangePassword";

/* ADMIN PAGES */

import AdminDashboard from "./pages/admin/AdminDashboard";
import ManualAttendance from "./pages/admin/ManualAttendance";
import Reports from "./pages/admin/Reports";
import Alerts from "./pages/admin/Alerts";
import ExportReports from "./pages/admin/ExportReports";
import ShiftManagement from "./pages/admin/ShiftManagement";
import EmployeeManagement from "./pages/admin/EmployeeManagement";
import AdminProfile from "./pages/admin/Profile";
import RosterUpload from "./pages/admin/RosterUpload";

/* EMPLOYEE PAGES */

import EmployeeDashboard from "./pages/employee/EmployeeDashboard";
import MarkAttendance from "./pages/employee/MarkAttendance";
import DownloadAttendance from "./pages/employee/DownloadAttendance";
import EmployeeProfile from "./pages/employee/Profile";
import UpcomingShifts from "./pages/employee/UpcomingShifts";
import ShiftHistory from "./pages/employee/ShiftHistory";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        {/* LOGIN */}

        <Route path="/" element={<Login />} />

        {/* ADMIN */}

        <Route
          element={
            <ProtectedRoute allowedRole="admin">
              <AdminLayout />
            </ProtectedRoute>
          }
        >

          <Route
            path="/admin-dashboard"
            element={<AdminDashboard />}
          />

          <Route
            path="/manual-attendance"
            element={<ManualAttendance />}
          />

          <Route
            path="/reports"
            element={<Reports />}
          />

          <Route
            path="/alerts"
            element={<Alerts />}
          />

          <Route
            path="/export-reports"
            element={<ExportReports />}
          />

          <Route
            path="/shifts"
            element={<ShiftManagement />}
          />

          <Route
            path="/employees"
            element={<EmployeeManagement />}
          />

          <Route
            path="/admin-profile"
            element={<AdminProfile />}
          />
          <Route
            path="/change-password"
            element={<ChangePassword />}
          />
          <Route
            path="/roster-upload"
            element={<RosterUpload />}
          />
        </Route>

        {/* EMPLOYEE */}

        <Route
          element={
            <ProtectedRoute allowedRole="employee">
              <EmployeeLayout />
            </ProtectedRoute>
          }
        >

          <Route
            path="/employee-dashboard"
            element={<EmployeeDashboard />}
          />

          <Route
            path="/mark-attendance"
            element={<MarkAttendance />}
          />

          <Route
            path="/download-attendance"
            element={<DownloadAttendance />}
          />

          <Route
            path="/employee-profile"
            element={<EmployeeProfile />}
          />
          <Route
          path="/upcoming-shifts"
          element={<UpcomingShifts />}
        />

        <Route
          path="/shift-history"
          element={<ShiftHistory />}
        />
        <Route
          path="/change-password"
          element={<ChangePassword />}
        />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;