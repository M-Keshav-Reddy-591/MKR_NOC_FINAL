import { useEffect, useState } from "react";
import axios from "axios";

export default function ShiftManagement() {

  const [shifts, setShifts] = useState([]);

  const [shiftData, setShiftData] = useState({
    shift_name: "",
    start_time: "",
    end_time: ""
  });

  const [csvFile, setCsvFile] = useState(null);

  useEffect(() => {

    fetchShifts();

  }, []);

  const fetchShifts = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/shifts"
      );

      setShifts(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const handleChange = (e) => {

    setShiftData({
      ...shiftData,
      [e.target.name]: e.target.value
    });
  };

  const addShift = async () => {

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/v1/shifts",
        shiftData
      );

      alert("Shift Added");

      fetchShifts();

      setShiftData({
        shift_name: "",
        start_time: "",
        end_time: ""
      });

    } catch (error) {

      console.log(error);
    }
  };

  const deleteShift = async (id) => {

    try {

      await axios.delete(
        `http://127.0.0.1:8000/api/v1/shifts/${id}`
      );

      fetchShifts();

    } catch (error) {

      console.log(error);
    }
  };

  const uploadCSV = async () => {

    if (!csvFile) {

      alert("Select CSV File");

      return;
    }

    const formData = new FormData();

    formData.append("file", csvFile);

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/v1/shifts/upload-csv",
        formData
      );

      alert("CSV Uploaded");

      fetchShifts();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-gray-800">

          Shift Management

        </h1>

        <p className="text-gray-500 mt-3 text-lg">

          Manage employee shifts

        </p>

      </div>

      {/* ADD SHIFT */}

      <div className="bg-white p-10 rounded-3xl shadow-xl mb-10">

        <h2 className="text-3xl font-bold mb-8">

          Add Shift

        </h2>

        <div className="grid grid-cols-3 gap-6">

          <input
            type="text"
            name="shift_name"
            placeholder="Shift Name"
            value={shiftData.shift_name}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="time"
            name="start_time"
            value={shiftData.start_time}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="time"
            name="end_time"
            value={shiftData.end_time}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

        </div>

        <button
          onClick={addShift}
          className="mt-8 bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold"
        >
          Add Shift
        </button>

      </div>

      {/* CSV IMPORT */}

      <div className="bg-white p-10 rounded-3xl shadow-xl mb-10">

        <h2 className="text-3xl font-bold mb-8">

          Upload Shift CSV

        </h2>

        <input
          type="file"
          accept=".csv"
          onChange={(e) => setCsvFile(e.target.files[0])}
          className="mb-6"
        />

        <button
          onClick={uploadCSV}
          className="bg-green-600 text-white px-10 py-4 rounded-2xl font-bold"
        >
          Upload CSV
        </button>

      </div>

      {/* SHIFT TABLE */}

      <div className="bg-white rounded-3xl shadow-2xl p-10">

        <h2 className="text-3xl font-bold mb-8">

          Shift List

        </h2>

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
                Action
              </th>

            </tr>

          </thead>

          <tbody>

            {
              shifts.map((shift) => (

                <tr
                  key={shift.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-5">
                    {shift.shift_name}
                  </td>

                  <td className="p-5">
                    {shift.start_time}
                  </td>

                  <td className="p-5">
                    {shift.end_time}
                  </td>

                  <td className="p-5">

                    <button
                      onClick={() => deleteShift(shift.id)}
                      className="bg-red-600 text-white px-5 py-2 rounded-xl"
                    >
                      Delete
                    </button>

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