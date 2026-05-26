import { useEffect, useState } from "react";
import axios from "axios";

export default function UpcomingShifts() {

  const [shifts, setShifts] = useState([]);

  const empId = localStorage.getItem("emp_id");

  useEffect(() => {

    fetchShifts();

  }, []);

  const fetchShifts = async () => {

    try {

      const response = await axios.get(
        `http://127.0.0.1:8000/api/v1/shift-assignments/${empId}`
      );

      setShifts(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-gray-800">

          Upcoming Shifts

        </h1>

        <p className="text-gray-500 mt-3 text-lg">

          View your assigned shifts

        </p>

      </div>

      <div className="grid grid-cols-3 gap-8">

        {
          shifts.map((shift) => (

            <div
              key={shift.id}
              className="bg-white rounded-3xl shadow-xl p-8 hover:scale-105 transition"
            >

              <div className="flex justify-between items-center mb-6">

                <h2 className="text-3xl font-bold text-blue-600">

                  {shift.shift_name}

                </h2>

                <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full font-bold">

                  ACTIVE

                </span>

              </div>

              <p className="text-gray-600 text-lg mb-3">

                Start Time:
                <span className="font-bold ml-2">
                  {shift.start_time}
                </span>

              </p>

              <p className="text-gray-600 text-lg mb-3">

                End Time:
                <span className="font-bold ml-2">
                  {shift.end_time}
                </span>

              </p>

              <p className="text-gray-600 text-lg">

                Date:
                <span className="font-bold ml-2">
                  {shift.shift_date}
                </span>

              </p>

            </div>
          ))
        }

      </div>

    </div>
  );
}