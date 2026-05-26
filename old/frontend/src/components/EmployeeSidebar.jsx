import { Link, useLocation } from "react-router-dom";

export default function EmployeeSidebar() {

  const location = useLocation();

  const menu = [

    {
      title: "Employee Dashboard",
      path: "/employee-dashboard"
    },

    {
      title: "Mark Attendance",
      path: "/mark-attendance"
    },

    {
      title: "Attendance History",
      path: "/attendance-history"
    },

    {
      title: "Download Attendance",
      path: "/download-attendance"
    },

    {
      title: "Upcoming Shifts",
      path: "/upcoming-shifts"
    },

    {
      title: "Shift History",
      path: "/shift-history"
    },

    {
      title: "Employee Profile",
      path: "/employee-profile"
    },

    {
      title: "Change Password",
      path: "/change-password"
    }

  ];

  return (

    <div className="w-72 min-h-screen bg-gradient-to-b from-green-950 via-green-900 to-black text-white p-6 flex flex-col justify-between shadow-2xl border-r border-green-800">

      <div>

        <div className="mb-12">

          <div className="bg-green-600 w-16 h-16 rounded-3xl flex items-center justify-center text-3xl font-black shadow-xl mb-4">
            E
          </div>

          <h1 className="text-4xl font-black tracking-wide">
            EMPLOYEE
          </h1>

          <p className="text-green-300 mt-3 text-sm">
            Employee Attendance Portal
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
                    ? "bg-green-600 scale-[1.02]"
                    : "bg-green-800 hover:bg-green-600 hover:translate-x-1"
                }`}
              >

                {item.title}

              </Link>
            ))
          }

        </nav>

      </div>

      <div className="mt-10">

        <div className="bg-green-800 p-4 rounded-2xl mb-5 shadow-xl">

          <h2 className="font-bold text-lg">
            Employee Access
          </h2>

          <p className="text-green-200 text-sm mt-1">
            Attendance and shift tracking enabled
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