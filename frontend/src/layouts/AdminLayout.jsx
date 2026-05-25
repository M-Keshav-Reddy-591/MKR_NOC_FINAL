import { Outlet, Link, useNavigate } from "react-router-dom";

export default function AdminLayout() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* SIDEBAR */}
      <div className="w-64 bg-[#1E1B4B] text-white p-5">
        <h1 className="text-3xl font-bold mb-10">
          NOC System
        </h1>

        <div className="space-y-4">
          <Link to="/admin-dashboard" className="block">
            Dashboard
          </Link>

          <Link to="/employee-dashboard" className="block">
            Employee Dashboard
          </Link>

          <Link to="/alerts" className="block">
            Alerts
          </Link>

          <Link to="/reports" className="block">
            Reports
          </Link>

          <Link to="/analytics" className="block">
            Analytics
          </Link>

          <Link to="/shift-calendar" className="block">
            Shift Calendar
          </Link>
          <Link to="/leaves" className="block">
  Leaves
</Link>
<Link to="/employees" className="block">
  Employees
</Link>

<Link to="/attendance-control" className="block">
  Attendance Control
</Link>
<Link to="/profile" className="block">
  Profile
</Link>
        </div>

        <button
          onClick={logout}
          className="mt-10 bg-red-500 px-4 py-2 rounded-lg"
        >
          Logout
        </button>
      </div>

      {/* PAGE CONTENT */}
      <div className="flex-1 p-6">
        <Outlet />
      </div>
    </div>
  );
}