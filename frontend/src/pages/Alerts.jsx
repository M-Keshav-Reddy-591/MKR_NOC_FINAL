import { useEffect, useState } from "react";
import axios from "axios";

export default function Alerts() {

  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    fetchAlerts();

  }, []);

  const fetchAlerts = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/attendance/all"
      );

      const absentEmployees = response.data.filter(
        (item) => item.status === "Absent"
      );

      setAlerts(absentEmployees);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="p-8">

      <h1 className="text-3xl font-bold mb-8 text-red-600">

        Employee Alerts

      </h1>

      <div className="overflow-x-auto bg-white rounded-2xl shadow-lg">

        <table className="w-full">

          <thead className="bg-red-500 text-white">

            <tr>

              <th className="p-4">Employee ID</th>

              <th className="p-4">Date</th>

              <th className="p-4">Status</th>

            </tr>

          </thead>

          <tbody>

            {alerts.map((alert) => (

              <tr
                key={alert.id}
                className="border-b hover:bg-gray-100"
              >

                <td className="p-4">
                  {alert.employee_id}
                </td>

                <td className="p-4">
                  {alert.date}
                </td>

                <td className="p-4 text-red-600 font-bold">
                  {alert.status}
                </td>

              </tr>
            ))}

          </tbody>

        </table>

      </div>
    </div>
  );
}