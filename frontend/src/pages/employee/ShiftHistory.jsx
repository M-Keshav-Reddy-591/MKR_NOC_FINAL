import { useEffect, useState } from "react";
import axios from "axios";

export default function ShiftHistory() {

  const [history, setHistory] = useState([]);

  const empId = localStorage.getItem("emp_id");

  useEffect(() => {

    fetchHistory();

  }, []);

  const fetchHistory = async () => {

    try {

      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/shift-assignments/history/${empId}`
      );

      setHistory(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-gray-800">

          Shift History

        </h1>

        <p className="text-gray-500 mt-3 text-lg">

          Completed shift history

        </p>

      </div>

      <div className="bg-white rounded-3xl shadow-xl p-10">

        <table className="w-full">

          <thead>

            <tr className="bg-gray-100">

              <th className="p-5 text-left">
                Shift Name
              </th>

              <th className="p-5 text-left">
                Start Time
              </th>

              <th className="p-5 text-left">
                End Time
              </th>

              <th className="p-5 text-left">
                Date
              </th>

            </tr>

          </thead>

          <tbody>

            {
              history.map((item) => (

                <tr
                  key={item.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-5">
                    {item.shift_name}
                  </td>

                  <td className="p-5">
                    {item.start_time}
                  </td>

                  <td className="p-5">
                    {item.end_time}
                  </td>

                  <td className="p-5">
                    {item.shift_date}
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