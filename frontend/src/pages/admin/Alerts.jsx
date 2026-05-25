import { useEffect, useState } from "react";
import axios from "axios";

export default function AlertsPage() {

  const [employees, setEmployees] =
    useState([]);

  useEffect(() => {

    fetchAbsentEmployees();

  }, []);

  const fetchAbsentEmployees = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/api/v1/dashboard/absent-employees"
    );

    setEmployees(response.data);
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Absent Employees
      </h1>

      <div className="bg-white rounded-2xl shadow-lg overflow-hidden">

        <table className="w-full">

          <thead className="bg-red-600 text-white">

            <tr>

              <th className="p-4 text-left">
                Employee ID
              </th>

              <th className="p-4 text-left">
                Employee Name
              </th>

              <th className="p-4 text-left">
                Status
              </th>

            </tr>

          </thead>

          <tbody>

            {employees.map((emp) => (

              <tr
                key={emp.emp_id}
                className="border-b"
              >

                <td className="p-4">
                  {emp.emp_id}
                </td>

                <td className="p-4">
                  {emp.emp_name}
                </td>

                <td className="p-4 text-red-600 font-bold">
                  ABSENT
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}