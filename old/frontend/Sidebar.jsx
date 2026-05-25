import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();

  const role = localStorage.getItem("role");

  const adminMenus = [
    {
      name: "Admin Dashboard",
      path: "/admin-dashboard",
    },
    {
      name: "Employees",
      path: "/employees",
    },
    {
      name: "Attendance",
      path: "/attendance-control",
    },
    {
      name: "Shift Allocation",
      path: "/shift-allocation",
    },
    {
      name: "Shift Swaps",
      path: "/shift-swaps",
    },
    {
      name: "Live Shift Board",
      path: "/live-shift-board",
    },
    {
      name: "Shift Calendar",
      path: "/shift-calendar",
    },
    {
      name: "Reports",
      path: "/reports",
    },
    {
      name: "Analytics",
      path: "/analytics",
    },
    {
      name: "Analytics Dashboard",
      path: "/analytics-dashboard",
    },
    {
      name: "Performance",
      path: "/employee-performance",
    },
    {
      name: "Employee Monitor",
      path: "/employee-monitor",
    },
    {
      name: "Incidents",
      path: "/incidents",
    },
    {
      name: "Alerts",
      path: "/alerts",
    },
    {
      name: "NOC Operations",
      path: "/noc-operations",
    },
    {
      name: "NOC Status",
      path: "/noc-status",
    },
    {
      name: "System Health",
      path: "/system-health",
    },
    {
      name: "System Logs",
      path: "/system-logs",
    },
    {
      name: "Settings",
      path: "/settings",
    },
    {
      name: "Profile",
      path: "/profile",
    },
  ];

  const employeeMenus = [
    {
      name: "Employee Dashboard",
      path: "/employee-dashboard",
    },
    {
      name: "Attendance",
      path: "/attendance-control",
    },
    {
      name: "Leaves",
      path: "/leaves",
    },
    {
      name: "Profile",
      path: "/profile",
    },
  ];

  const menus = role === "admin" ? adminMenus : employeeMenus;

  return (
    <div className="w-72 min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-black text-white p-6 border-r border-slate-800">

      {/* LOGO */}

      <div className="mb-10">
        <h1 className="text-3xl font-bold text-center text-cyan-400">
          NOC SYSTEM
        </h1>

        <p className="text-center text-gray-400 text-sm mt-2">
          Enterprise Monitoring Panel
        </p>
      </div>

      {/* MENU */}

      <nav className="space-y-3 overflow-y-auto h-[75vh] pr-2">

        {menus.map((menu, index) => (
          <Link
            key={index}
            to={menu.path}
            className={`block p-4 rounded-2xl transition-all duration-300 font-medium ${
              location.pathname === menu.path
                ? "bg-cyan-600 shadow-lg shadow-cyan-900"
                : "bg-slate-800 hover:bg-cyan-700"
            }`}
          >
            {menu.name}
          </Link>
          
        ))}
        <Link
        to="/live-attendance"
        className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
        Live Attendance
        </Link>

        <Link
        to="/server-status"
        className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
        Server Status
        </Link>

      </nav>

      {/* LOGOUT */}

      <button
        onClick={() => {
          localStorage.clear();
          window.location.href = "/";
        }}
        className="mt-6 w-full bg-red-600 hover:bg-red-700 py-4 rounded-2xl font-bold transition"
      >
        Logout
      </button>
    </div>
  );
}