import { Link } from "react-router-dom";

export default function EmployeeSidebar() {

  return (

    <div className="w-72 min-h-screen bg-green-900 text-white p-6">

      <h1 className="text-3xl font-bold mb-10 text-center">
        EMPLOYEE
      </h1>

      <nav className="space-y-4">

        <Link
          to="/employee-dashboard"
          className="block p-4 rounded-xl bg-green-800 hover:bg-green-600 transition"
        >
          Dashboard
        </Link>

        <Link
          to="/mark-attendance"
          className="block p-4 rounded-xl bg-green-800 hover:bg-green-600 transition"
        >
          Mark Attendance
        </Link>

        <Link
          to="/download-attendance"
          className="block p-4 rounded-xl bg-green-800 hover:bg-green-600 transition"
        >
          Download Attendance
        </Link>

        <Link
          to="/employee-profile"
          className="block p-4 rounded-xl bg-green-800 hover:bg-green-600 transition"
        >
          Profile
        </Link>
        <Link
          to="/upcoming-shifts"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-green-600 transition"
        >
          Upcoming Shifts
        </Link>

        <Link
          to="/shift-history"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Shift History
        </Link>        

      </nav>

      <button
        onClick={() => {

          localStorage.clear();

          window.location.href = "/";
        }}
        className="mt-10 w-full bg-red-600 py-3 rounded-xl font-bold"
      >
        Logout
      </button>

    </div>
  );
}