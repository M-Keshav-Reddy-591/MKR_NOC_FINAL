import { Link, useLocation } from "react-router-dom";

export default function AdminSidebar() {

  const location = useLocation();

  const menu = [

    {
      title: "Dashboard",
      path: "/admin-dashboard"
    },

    {
      title: "Manual Attendance",
      path: "/manual-attendance"
    },

    {
      title: "Manual Shift Assignment",
      path: "/manual-shift-assignment"
    },

    {
      title: "CSV Shift Upload",
      path: "/csv-shift-upload"
    },

    {
      title: "Reports",
      path: "/reports"
    },

    {
      title: "Analytics",
      path: "/analytics"
    },

    {
      title: "Alerts",
      path: "/alerts"
    },

    {
      title: "Export Reports",
      path: "/export-reports"
    },

    {
      title: "Shift Management",
      path: "/shifts"
    },

    {
      title: "Employee Management",
      path: "/employees"
    },

    {
      title: "Holiday Work Log",
      path: "/holiday-work-log"
    },

    {
      title: "Profile",
      path: "/admin-profile"
    }

  ];

  return (

    <div className="w-72 min-h-screen bg-gradient-to-b from-gray-950 via-gray-900 to-black text-white p-6 flex flex-col justify-between shadow-2xl border-r border-gray-800">

      <div>

        <div className="mb-10">

          <h1 className="text-4xl font-black tracking-wide leading-tight">

            ADMIN PANEL

          </h1>

          <p className="text-gray-400 mt-3 text-sm">

            NOC Attendance Management

          </p>

        </div>

        <nav className="space-y-4">

          {
            menu.map((item, index) => (

              <Link
                key={index}
                to={item.path}
                className={`block p-4 rounded-2xl transition-all duration-300 font-semibold shadow-lg ${
                  location.pathname === item.path
                    ? "bg-gradient-to-r from-blue-600 to-indigo-600 scale-105"
                    : "bg-gray-800 hover:bg-blue-600 hover:scale-105"
                }`}
              >

                {item.title}

              </Link>
            ))
          }

        </nav>

      </div>

      <button
        onClick={() => {

          localStorage.clear();

          window.location.href = "/";
        }}
        className="w-full bg-red-600 py-4 rounded-2xl font-bold hover:bg-red-700 transition shadow-xl"
      >

        Logout

      </button>

    </div>
  );
}