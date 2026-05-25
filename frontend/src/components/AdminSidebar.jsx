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
      title: "Reports",
      path: "/reports"
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
      title: "Profile",
      path: "/admin-profile"
    }
  ];

  return (

    <div className="w-72 min-h-screen bg-gray-900 text-white p-6 flex flex-col justify-between">

      <div>

        <div className="mb-10">

          <h1 className="text-4xl font-extrabold">

            ADMIN PANEL

          </h1>

          <p className="text-gray-400 mt-2">

            NOC Attendance System

          </p>

        </div>

        <nav className="space-y-4">

          {
            menu.map((item, index) => (

              <Link
                key={index}
                to={item.path}
                className={`block p-4 rounded-2xl transition font-semibold ${
                  location.pathname === item.path
                    ? "bg-blue-600"
                    : "bg-gray-800 hover:bg-blue-500"
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
        className="w-full bg-red-600 py-4 rounded-2xl font-bold hover:bg-red-700 transition"
      >

        Logout

      </button>

    </div>
  );
}