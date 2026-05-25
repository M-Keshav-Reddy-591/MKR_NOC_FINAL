import { useEffect, useState } from "react";
import axios from "axios";

export default function ManualAttendance() {

  const [employees, setEmployees] = useState([]);

  const [attendanceLogs, setAttendanceLogs] = useState([]);

  const [attendanceData, setAttendanceData] = useState({
    emp_id: "",
    status: "Present"
  });

  useEffect(() => {

    fetchEmployees();

    fetchAttendance();

  }, []);

  const fetchEmployees = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/employees"
      );

      setEmployees(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const fetchAttendance = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/attendance"
      );

      setAttendanceLogs(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const markAttendance = async () => {

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/v1/attendance",
        attendanceData
      );

      alert("Attendance Marked");

      fetchAttendance();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-gray-800">

          Manual Attendance

        </h1>

        <p className="text-gray-500 mt-3 text-lg">

          Mark employee attendance manually

        </p>

      </div>

      {/* MARK ATTENDANCE */}

      <div className="bg-white rounded-3xl shadow-xl p-10 mb-10">

        <h2 className="text-3xl font-bold mb-8">

          Mark Attendance

        </h2>

        <div className="grid grid-cols-3 gap-6">

          <select
            value={attendanceData.emp_id}
            onChange={(e) =>
              setAttendanceData({
                ...attendanceData,
                emp_id: e.target.value
              })
            }
            className="p-4 rounded-xl border"
          >

            <option value="">
              Select Employee
            </option>

            {
              employees.map((emp) => (

                <option
                  key={emp.id}
                  value={emp.emp_id}
                >
                  {emp.emp_name}
                </option>
              ))
            }

          </select>

          <select
            value={attendanceData.status}
            onChange={(e) =>
              setAttendanceData({
                ...attendanceData,
                status: e.target.value
              })
            }
            className="p-4 rounded-xl border"
          >

            <option>
              Present
            </option>

            <option>
              Absent
            </option>

          </select>

        </div>

        <button
          onClick={markAttendance}
          className="mt-8 bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold"
        >
          Mark Attendance
        </button>

      </div>

      {/* ATTENDANCE TABLE */}

      <div className="bg-white rounded-3xl shadow-xl p-10">

        <h2 className="text-3xl font-bold mb-8">

          Attendance Logs

        </h2>

        <table className="w-full">

          <thead>

            <tr className="bg-gray-100">

              <th className="p-5 text-left">
                Employee ID
              </th>

              <th className="p-5 text-left">
                Status
              </th>

              <th className="p-5 text-left">
                Date
              </th>

            </tr>

          </thead>

          <tbody>

            {
              attendanceLogs.map((log) => (

                <tr
                  key={log.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-5">
                    {log.emp_id}
                  </td>

                  <td className="p-5">

                    <span className={`px-4 py-2 rounded-full text-white ${
                      log.status === "Present"
                        ? "bg-green-600"
                        : "bg-red-600"
                    }`}>

                      {log.status}

                    </span>

                  </td>

                  <td className="p-5">
                    {log.date}
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