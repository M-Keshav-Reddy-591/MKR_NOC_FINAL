import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";

function AdminDashboard() {
  return (
    <div className="p-10 text-3xl font-bold">
      Admin Dashboard Working
    </div>
  );
}

function EmployeeDashboard() {
  return (
    <div className="p-10 text-3xl font-bold">
      Employee Dashboard Working
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />

        <Route
          path="/admin-dashboard"
          element={<AdminDashboard />}
        />

        <Route
          path="/employee-dashboard"
          element={<EmployeeDashboard />}
        />
      </Routes>
    </BrowserRouter>
  );
}