import { Link } from "react-router-dom";

export default function Sidebar() {

  return (

    <div className="w-72 min-h-screen bg-gray-900 text-white p-6">

      <h1 className="text-3xl font-bold mb-10 text-center">

        NOC SYSTEM

      </h1>

      <nav className="space-y-4">

        <Link
          to="/dashboard"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Dashboard
        </Link>

        <Link
          to="/employees"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Employees
        </Link>

        <Link
          to="/attendance"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Attendance
        </Link>

        <Link
          to="/shifts"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Shifts
        </Link>

        <Link
          to="/leaves"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Leaves
        </Link>

        <Link
          to="/reports"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-blue-600 transition"
        >
          Reports
        </Link>

        <Link
          to="/alerts"
          className="block p-4 rounded-xl bg-gray-800 hover:bg-red-600 transition"
        >
          Alerts
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