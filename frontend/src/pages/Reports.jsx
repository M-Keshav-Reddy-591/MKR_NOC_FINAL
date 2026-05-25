import { useEffect, useState } from "react";
import axios from "axios";

export default function Reports() {

  const [reports, setReports] = useState([]);

  useEffect(() => {

    fetchReports();

  }, []);

  const fetchReports = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/reports/employees"
      );

      setReports(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="p-8 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-10">

        Reports & Analytics

      </h1>

      {/* NORMAL REPORTS */}

      <div className="bg-white rounded-2xl shadow-xl p-6 mb-10">

        <h2 className="text-2xl font-bold mb-6 text-blue-600">

          Employee Reports

        </h2>

        <table className="w-full">

          <thead className="bg-blue-500 text-white">

            <tr>

              <th className="p-4">Employee</th>

              <th className="p-4">Department</th>

              <th className="p-4">Designation</th>

              <th className="p-4">Attendance</th>

            </tr>

          </thead>

          <tbody>

            {reports.map((item, index) => (

              <tr
                key={index}
                className="border-b hover:bg-gray-100"
              >

                <td className="p-4">
                  {item.emp_name}
                </td>

                <td className="p-4">
                  {item.department}
                </td>

                <td className="p-4">
                  {item.designation}
                </td>

                <td className="p-4">
                  {item.attendance_count}
                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

      {/* SPECIAL REPORTS */}

      <div className="bg-white rounded-2xl shadow-xl p-6">

        <h2 className="text-2xl font-bold mb-6 text-purple-600">

          Shift Analytics

        </h2>

        <table className="w-full">

          <thead className="bg-purple-500 text-white">

            <tr>

              <th className="p-4">Employee</th>

              <th className="p-4">Total Shifts</th>

              <th className="p-4">Morning</th>

              <th className="p-4">General</th>

              <th className="p-4">Night</th>

            </tr>

          </thead>

          <tbody>

            {reports.map((item, index) => (

              <tr
                key={index}
                className="border-b hover:bg-gray-100"
              >

                <td className="p-4">
                  {item.emp_name}
                </td>

                <td className="p-4">20</td>

                <td className="p-4">5</td>

                <td className="p-4">8</td>

                <td className="p-4">7</td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

      {/* HOLIDAY SHIFTS */}

      <div className="bg-white rounded-2xl shadow-xl p-6 mt-10">

        <h2 className="text-2xl font-bold mb-6 text-red-600">

          Holiday Shift Reports

        </h2>

        <table className="w-full">

          <thead className="bg-red-500 text-white">

            <tr>

              <th className="p-4">Employee</th>

              <th className="p-4">Holiday Shifts</th>

            </tr>

          </thead>

          <tbody>

            {reports.map((item, index) => (

              <tr
                key={index}
                className="border-b hover:bg-gray-100"
              >

                <td className="p-4">
                  {item.emp_name}
                </td>

                <td className="p-4">
                  4
                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}