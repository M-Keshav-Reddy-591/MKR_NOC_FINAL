import { useEffect, useState } from "react";
import axios from "axios";

export default function LiveAttendancePage() {

  const [attendance, setAttendance] = useState([]);

  useEffect(() => {

    fetchAttendance();

  }, []);

  const fetchAttendance = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/live-attendance/"
      );

      setAttendance(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="p-8">

      <div className="mb-8">

        <h1 className="text-4xl font-bold text-gray-800">
          Live Attendance Monitor
        </h1>

        <p className="text-gray-500 mt-2">
          Real-time employee attendance tracking
        </p>

      </div>

      <div className="grid grid-cols-4 gap-6 mb-8">

        <div className="bg-green-500 text-white p-6 rounded-2xl shadow-lg">
          <h2 className="text-lg font-semibold">Present</h2>
          <p className="text-4xl font-bold mt-2">
            {
              attendance.filter(
                item => item.status === "Present"
              ).length
            }
          </p>
        </div>

        <div className="bg-red-500 text-white p-6 rounded-2xl shadow-lg">
          <h2 className="text-lg font-semibold">Absent</h2>
          <p className="text-4xl font-bold mt-2">
            {
              attendance.filter(
                item => item.status === "Absent"
              ).length
            }
          </p>
        </div>

        <div className="bg-yellow-500 text-white p-6 rounded-2xl shadow-lg">
          <h2 className="text-lg font-semibold">Late</h2>
          <p className="text-4xl font-bold mt-2">
            {
              attendance.filter(
                item => item.status === "Late"
              ).length
            }
          </p>
        </div>

        <div className="bg-blue-500 text-white p-6 rounded-2xl shadow-lg">
          <h2 className="text-lg font-semibold">Total</h2>
          <p className="text-4xl font-bold mt-2">
            {attendance.length}
          </p>
        </div>

      </div>

      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">

        <table className="w-full">

          <thead className="bg-gray-900 text-white">

            <tr>

              <th className="p-4 text-left">Employee</th>
              <th className="p-4 text-left">Department</th>
              <th className="p-4 text-left">Status</th>
              <th className="p-4 text-left">Check In</th>
              <th className="p-4 text-left">Check Out</th>
              <th className="p-4 text-left">Date</th>

            </tr>

          </thead>

          <tbody>

            {
              attendance.map((item, index) => (

                <tr
                  key={index}
                  className="border-b hover:bg-gray-100"
                >

                  <td className="p-4 font-semibold">
                    {item.employee_name}
                  </td>

                  <td className="p-4">
                    {item.department}
                  </td>

                  <td className="p-4">

                    <span className={`px-4 py-2 rounded-full text-white text-sm font-semibold ${
                      item.status === "Present"
                        ? "bg-green-500"
                        : item.status === "Absent"
                        ? "bg-red-500"
                        : "bg-yellow-500"
                    }`}>
                      {item.status}
                    </span>

                  </td>

                  <td className="p-4">
                    {item.check_in}
                  </td>

                  <td className="p-4">
                    {item.check_out}
                  </td>

                  <td className="p-4">
                    {item.attendance_date}
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