import { useEffect, useState } from "react";
import axios from "axios";

export default function AdminDashboard() {

  const [stats, setStats] = useState({});

  const [attendanceLogs, setAttendanceLogs] = useState([]);

  useEffect(() => {

    fetchDashboard();

  }, []);

  const fetchDashboard = async () => {

    try {

      const statsResponse = await axios.get(
        "http://127.0.0.1:8000/api/v1/dashboard/stats"
      );

      const attendanceResponse = await axios.get(
        "http://127.0.0.1:8000/api/v1/dashboard/recent-attendance"
      );

      setStats(statsResponse.data);

      setAttendanceLogs(attendanceResponse.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="p-8 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">

        NOC Admin Dashboard

      </h1>

      {/* STATS */}

      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-6 gap-6 mb-10">

        <div className="bg-blue-600 text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Employees</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.total_employees}
          </p>
        </div>

        <div className="bg-green-600 text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Present</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.present_today}
          </p>
        </div>

        <div className="bg-red-600 text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Absent</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.absent_today}
          </p>
        </div>

        <div className="bg-yellow-500 text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Leaves</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.total_leaves}
          </p>
        </div>

        <div className="bg-purple-600 text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Shifts</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.total_shifts}
          </p>
        </div>

        <div className="bg-black text-white rounded-2xl p-6 shadow-xl">
          <h2 className="text-lg">Attendance %</h2>
          <p className="text-4xl font-bold mt-2">
            {stats.attendance_percentage}%
          </p>
        </div>

      </div>

      {/* RECENT ATTENDANCE */}

      <div className="bg-white rounded-2xl shadow-xl p-8">

        <h2 className="text-2xl font-bold mb-6">

          Recent Attendance Logs

        </h2>

        <table className="w-full">

          <thead>

            <tr className="bg-gray-200">

              <th className="p-4 text-left">Employee ID</th>

              <th className="p-4 text-left">Employee Name</th>

              <th className="p-4 text-left">Status</th>

              <th className="p-4 text-left">Date</th>

            </tr>

          </thead>

          <tbody>

            {attendanceLogs.map((log, index) => (

              <tr
                key={index}
                className="border-b"
              >

                <td className="p-4">
                  {log.emp_id}
                </td>

                <td className="p-4">
                  {log.emp_name}
                </td>

                <td className="p-4">

                  <span
                    className={`px-4 py-2 rounded-full text-white ${
                      log.status === "Present"
                        ? "bg-green-600"
                        : "bg-red-600"
                    }`}
                  >
                    {log.status}
                  </span>

                </td>

                <td className="p-4">
                  {log.date}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}