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
      title: "Attendance Reports",
      path: "/reports"
    },

    {
      title: "Absent Alerts",
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
      title: "Roster Upload",
      path: "/roster-upload"
    },

    {
      title: "Employee Management",
      path: "/employees"
    },

    {
      title: "Monthly Analytics",
      path: "/monthly-analytics"
    },

    {
      title: "System Analytics",
      path: "/analytics"
    },

    {
      title: "Admin Profile",
      path: "/admin-profile"
    },

    {
      title: "Change Password",
      path: "/change-password"
    }

  ];

  return (

    <div className="w-72 min-h-screen bg-gradient-to-b from-gray-950 via-gray-900 to-black text-white p-6 flex flex-col justify-between shadow-2xl border-r border-gray-800">

      <div>

        <div className="mb-12">

          <div className="bg-blue-600 w-16 h-16 rounded-3xl flex items-center justify-center text-3xl font-black shadow-xl mb-4">
            N
          </div>

          <h1 className="text-4xl font-black tracking-wide">
            ADMIN PANEL
          </h1>

          <p className="text-gray-400 mt-3 text-sm">
            NOC Attendance Management System
          </p>

        </div>

        <nav className="space-y-3">

          {
            menu.map((item, index) => (

              <Link
                key={index}
                to={item.path}
                className={`block p-4 rounded-2xl transition-all duration-300 font-semibold text-[15px] shadow-lg ${
                  location.pathname === item.path
                    ? "bg-blue-600 scale-[1.02]"
                    : "bg-gray-800 hover:bg-blue-500 hover:translate-x-1"
                }`}
              >

                {item.title}

              </Link>
            ))
          }

        </nav>

      </div>

      <div className="mt-10">

        <div className="bg-gray-800 p-4 rounded-2xl mb-5 shadow-xl">

          <h2 className="font-bold text-lg">
            Admin Access
          </h2>

          <p className="text-gray-400 text-sm mt-1">
            Full system management enabled
          </p>

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

    </div>
  );
}