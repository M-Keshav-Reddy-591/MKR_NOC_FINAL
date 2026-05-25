import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

import AdminDashboard from "./pages/dashboard/AdminDashboard";
import EmployeeDashboard from "./pages/dashboard/EmployeeDashboard";

import AnalyticsDashboard from "./pages/analytics/AnalyticsDashboard";
import AnalyticsPage from "./pages/analytics/AnalyticsPage";

import PerformancePage from "./pages/performance/PerformancePage";
import EmployeePerformanceTracker from "./pages/performance/EmployeePerformanceTracker";

import SystemLogsPage from "./pages/logs/SystemLogsPage";

import AlertsPage from "./pages/alerts/AlertsPage";

import ReportsPage from "./pages/reports/ReportsPage";

import ShiftCalendar from "./pages/calendar/ShiftCalendar";

import LeavePage from "./pages/leaves/LeavePage";

import ProfilePage from "./pages/profile/ProfilePage";

import AdminLayout from "./layouts/AdminLayout";

import ShiftAllocationPage from "./pages/shifts/ShiftAllocationPage";

import ShiftSwapPage from "./pages/swaps/ShiftSwapPage";

import LiveShiftBoard from "./pages/shifts/LiveShiftBoard";

import EmployeesPage from "./pages/employees/EmployeesPage";

import AttendanceControlPage from "./pages/attendance/AttendanceControlPage";

import NOCStatusPage from "./pages/noc/NOCStatusPage";

import NOCOperationsCenter from "./pages/noc/NOCOperationsCenter";

import SettingsPage from "./pages/settings/SettingsPage";

import SystemHealthPage from "./pages/system/SystemHealthPage";

import IncidentManagementPage from "./pages/incidents/IncidentManagementPage";

import EmployeeActivityMonitor from "./pages/monitoring/EmployeeActivityMonitor";

import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* LOGIN */}

        <Route path="/" element={<Login />} />

        {/* MAIN LAYOUT */}

        <Route element={<AdminLayout />}>

          {/* ================= ADMIN ROUTES ================= */}

          <Route
            path="/admin-dashboard"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <AdminDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/employees"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <EmployeesPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/alerts"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <AlertsPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/reports"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <ReportsPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/analytics"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <AnalyticsPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/analytics-dashboard"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <AnalyticsDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/performance"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <PerformancePage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/employee-performance"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <EmployeePerformanceTracker />
              </ProtectedRoute>
            }
          />

          <Route
            path="/system-logs"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <SystemLogsPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/system-health"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <SystemHealthPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/shift-allocation"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <ShiftAllocationPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/shift-swaps"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <ShiftSwapPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/live-shift-board"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <LiveShiftBoard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/shift-calendar"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <ShiftCalendar />
              </ProtectedRoute>
            }
          />

          <Route
            path="/noc-status"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <NOCStatusPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/noc-operations"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <NOCOperationsCenter />
              </ProtectedRoute>
            }
          />

          <Route
            path="/incidents"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <IncidentManagementPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/employee-monitor"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <EmployeeActivityMonitor />
              </ProtectedRoute>
            }
          />

          <Route
            path="/settings"
            element={
              <ProtectedRoute allowedRoles={["admin"]}>
                <SettingsPage />
              </ProtectedRoute>
            }
          />

          {/* ================= EMPLOYEE ROUTES ================= */}

          <Route
            path="/employee-dashboard"
            element={
              <ProtectedRoute allowedRoles={["employee"]}>
                <EmployeeDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/attendance-control"
            element={
              <ProtectedRoute allowedRoles={["employee"]}>
                <AttendanceControlPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/profile"
            element={
              <ProtectedRoute allowedRoles={["employee", "admin"]}>
                <ProfilePage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/leaves"
            element={
              <ProtectedRoute allowedRoles={["employee"]}>
                <LeavePage />
              </ProtectedRoute>
            }
          />

        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;