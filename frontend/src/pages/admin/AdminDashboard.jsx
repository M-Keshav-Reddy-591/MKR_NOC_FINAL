import { useEffect, useState } from "react";
import axios from "axios";

export default function AdminDashboard() {

  const [stats, setStats] = useState({});

  const [attendance, setAttendance] = useState([]);

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const statsResponse = await axios.get(
        "http://127.0.0.1:8000/api/v1/dashboard/stats"
      );

      setStats(statsResponse.data);

      const attendanceResponse = await axios.get(
        "http://127.0.0.1:8000/api/v1/dashboard/recent-attendance"
      );

      setAttendance(attendanceResponse.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      {/* HEADER */}

      <div className="mb-10">

        <h1 className="text-6xl font-bold text-gray-800">

          Admin Dashboard

        </h1>

        <p className="text-gray-500 mt-3 text-xl">

          Real-time NOC Attendance Monitoring

        </p>

      </div>

      {/* STATS */}

      <div className="grid grid-cols-4 gap-8 mb-10">

        <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-10 rounded-3xl shadow-2xl">

          <h2 className="text-2xl font-semibold">
            Total Employees
          </h2>

          <p className="text-6xl font-bold mt-6">
            {stats.total_employees || 0}
          </p>

        </div>

        <div className="bg-gradient-to-r from-green-500 to-green-700 text-white p-10 rounded-3xl shadow-2xl">

          <h2 className="text-2xl font-semibold">
            Present Today
          </h2>

          <p className="text-6xl font-bold mt-6">
            {stats.present_today || 0}
          </p>

        </div>

        <div className="bg-gradient-to-r from-red-500 to-red-700 text-white p-10 rounded-3xl shadow-2xl">

          <h2 className="text-2xl font-semibold">
            Absent Today
          </h2>

          <p className="text-6xl font-bold mt-6">
            {stats.absent_today || 0}
          </p>

        </div>

        <div className="bg-gradient-to-r from-purple-600 to-pink-600 text-white p-10 rounded-3xl shadow-2xl">

          <h2 className="text-2xl font-semibold">
            Shift Assignments
          </h2>

          <p className="text-6xl font-bold mt-6">
            {stats.total_shifts || 0}
          </p>

        </div>

      </div>

      {/* ACTIONS */}

      <div className="grid grid-cols-4 gap-8 mb-10">

        <div className="bg-white p-10 rounded-3xl shadow-xl hover:scale-105 transition">

          <h2 className="text-3xl font-bold text-blue-600">

            Add Employee

          </h2>

          <p className="text-gray-500 mt-4 text-lg">

            Register new employees

          </p>

        </div>

        <div className="bg-white p-10 rounded-3xl shadow-xl hover:scale-105 transition">

          <h2 className="text-3xl font-bold text-green-600">

            Add Shift

          </h2>

          <p className="text-gray-500 mt-4 text-lg">

            Create shift assignments

          </p>

        </div>

        <div className="bg-white p-10 rounded-3xl shadow-xl hover:scale-105 transition">

          <h2 className="text-3xl font-bold text-red-600">

            Alerts

          </h2>

          <p className="text-gray-500 mt-4 text-lg">

            View absent employees

          </p>

        </div>

        <div className="bg-white p-10 rounded-3xl shadow-xl hover:scale-105 transition">

          <h2 className="text-3xl font-bold text-purple-600">

            Reports

          </h2>

          <p className="text-gray-500 mt-4 text-lg">

            Export reports

          </p>

        </div>

      </div>

      {/* RECENT ATTENDANCE */}

      <div className="bg-white rounded-3xl shadow-2xl p-10">

        <div className="flex justify-between items-center mb-8">

          <div>

            <h2 className="text-4xl font-bold">

              Recent Attendance

            </h2>

            <p className="text-gray-500 mt-2 text-lg">

              Latest employee attendance logs

            </p>

          </div>

          <div className="bg-green-100 text-green-700 px-6 py-3 rounded-full font-bold text-lg">

            LIVE

          </div>

        </div>

        <table className="w-full">

          <thead>

            <tr className="bg-gray-100 text-lg">

              <th className="p-5 text-left">
                Employee ID
              </th>

              <th className="p-5 text-left">
                Employee Name
              </th>

              <th className="p-5 text-left">
                Date
              </th>

              <th className="p-5 text-left">
                Status
              </th>

            </tr>

          </thead>

          <tbody>

            {
              attendance.map((item, index) => (

                <tr
                  key={index}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-5 font-semibold">
                    {item.emp_id}
                  </td>

                  <td className="p-5">
                    {item.emp_name}
                  </td>

                  <td className="p-5">
                    {item.date}
                  </td>

                  <td className="p-5">

                    <span className={`px-5 py-2 rounded-full text-white text-sm font-bold ${
                      item.status === "Present"
                        ? "bg-green-500"
                        : "bg-red-500"
                    }`}>

                      {item.status}

                    </span>

                  </td>

                </tr>
              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  );
}