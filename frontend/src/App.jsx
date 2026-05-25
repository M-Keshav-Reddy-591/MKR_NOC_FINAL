import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

import AdminDashboard from "./pages/dashboard/AdminDashboard";
import EmployeeDashboard from "./pages/dashboard/EmployeeDashboard";

import AlertsPage from "./pages/alerts/AlertsPage";
import ReportsPage from "./pages/reports/ReportsPage";
import AnalyticsPage from "./pages/analytics/AnalyticsPage";

import LeavePage from "./pages/leaves/LeavePage";

import ShiftAllocationPage from "./pages/shifts/ShiftAllocationPage";
import ShiftSwapPage from "./pages/swaps/ShiftSwapPage";

import EmployeesPage from "./pages/employees/EmployeesPage";

import AttendanceControlPage from "./pages/attendance/AttendanceControlPage";

import ProfilePage from "./pages/profile/ProfilePage";

import ShiftCalender from "./pages/calendar/ShiftCalender";

import AdminLayout from "./layouts/AdminLayout";
import LiveAttendancePage from "./pages/attendance/LiveAttendancePage";
import ServerStatusPage from "./pages/noc/ServerStatusPage";
function App() {

  return (

    <BrowserRouter>

      <Routes>

        {/* LOGIN */}

        <Route path="/" element={<Login />} />

        {/* ADMIN LAYOUT */}

        <Route element={<AdminLayout />}>

          <Route
            path="/admin-dashboard"
            element={<AdminDashboard />}
          />

          <Route
            path="/employee-dashboard"
            element={<EmployeeDashboard />}
          />

          <Route
            path="/alerts"
            element={<AlertsPage />}
          />

          <Route
            path="/reports"
            element={<ReportsPage />}
          />

          <Route
            path="/analytics"
            element={<AnalyticsPage />}
          />

          <Route
            path="/leaves"
            element={<LeavePage />}
          />

          <Route
            path="/shift-allocation"
            element={<ShiftAllocationPage />}
          />

          <Route
            path="/shift-swaps"
            element={<ShiftSwapPage />}
          />

          <Route
            path="/employees"
            element={<EmployeesPage />}
          />

          <Route
            path="/attendance-control"
            element={<AttendanceControlPage />}
          />

          <Route
            path="/profile"
            element={<ProfilePage />}
          />

          <Route
            path="/shift-calendar"
            element={<ShiftCalender />}
          />
          <Route
            path="/live-attendance"
            element={<LiveAttendancePage />}
          />

          <Route
            path="/server-status"
            element={<ServerStatusPage />}
          />
        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default App;