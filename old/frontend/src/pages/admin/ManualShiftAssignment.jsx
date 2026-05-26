import { useEffect, useState } from "react";
import API from "../../api/axios";

export default function ManualShiftAssignment() {

  const [employees, setEmployees] = useState([]);

  const [form, setForm] = useState({

    employee_id: "",
    shift_date: "",
    shift_name: "Morning",
    is_holiday: false,
    holiday_note: ""

  });

  useEffect(() => {

    fetchEmployees();

  }, []);

  const fetchEmployees = async () => {

    try {

      const response = await API.get("/employees");

      setEmployees(response.data);

    } catch (error) {

      console.log(error);

    }

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    try {

      await API.post(
        "/shifts/manual-assign",
        form
      );

      alert("Shift Assigned Successfully");

      setForm({

        employee_id: "",
        shift_date: "",
        shift_name: "Morning",
        is_holiday: false,
        holiday_note: ""

      });

    } catch (error) {

      console.log(error);

      alert("Failed to assign shift");

    }

  };

  return (

    <div className="p-10">

      <div className="mb-8">

        <h1 className="text-5xl font-black text-gray-800">

          Manual Shift Assignment

        </h1>

        <p className="text-gray-500 mt-3">

          Assign shifts and manage holiday work

        </p>

      </div>

      <div className="bg-white rounded-3xl shadow-2xl p-10 border border-gray-100">

        <form
          onSubmit={handleSubmit}
          className="space-y-8"
        >

          <div>

            <label className="block mb-3 font-bold text-gray-700">

              Select Employee

            </label>

            <select
              value={form.employee_id}
              onChange={(e) =>
                setForm({
                  ...form,
                  employee_id: e.target.value
                })
              }
              className="w-full p-5 rounded-2xl border border-gray-300 focus:outline-none focus:ring-4 focus:ring-blue-300"
              required
            >

              <option value="">
                Choose Employee
              </option>

              {
                employees.map((emp) => (

                  <option
                    key={emp.id}
                    value={emp.id}
                  >

                    {emp.emp_id} - {emp.emp_name}

                  </option>

                ))
              }

            </select>

          </div>

          <div>

            <label className="block mb-3 font-bold text-gray-700">

              Shift Date

            </label>

            <input
              type="date"
              value={form.shift_date}
              onChange={(e) =>
                setForm({
                  ...form,
                  shift_date: e.target.value
                })
              }
              className="w-full p-5 rounded-2xl border border-gray-300 focus:outline-none focus:ring-4 focus:ring-blue-300"
              required
            />

          </div>

          <div>

            <label className="block mb-3 font-bold text-gray-700">

              Shift Type

            </label>

            <select
              value={form.shift_name}
              onChange={(e) =>
                setForm({
                  ...form,
                  shift_name: e.target.value
                })
              }
              className="w-full p-5 rounded-2xl border border-gray-300 focus:outline-none focus:ring-4 focus:ring-blue-300"
            >

              <option>Morning</option>

              <option>Afternoon</option>

              <option>Night</option>

              <option>Holiday</option>

              <option>Week Off</option>

            </select>

          </div>

          <div className="flex items-center gap-4">

            <input
              type="checkbox"
              checked={form.is_holiday}
              onChange={(e) =>
                setForm({
                  ...form,
                  is_holiday: e.target.checked
                })
              }
              className="w-6 h-6"
            />

            <label className="font-bold text-gray-700">

              Employee working on Holiday

            </label>

          </div>

          {
            form.is_holiday && (

              <div>

                <label className="block mb-3 font-bold text-gray-700">

                  Holiday Work Note

                </label>

                <textarea
                  rows="5"
                  value={form.holiday_note}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      holiday_note: e.target.value
                    })
                  }
                  className="w-full p-5 rounded-2xl border border-gray-300 focus:outline-none focus:ring-4 focus:ring-blue-300"
                  placeholder="Reason for working on holiday..."
                />

              </div>

            )
          }

          <button
            type="submit"
            className="w-full py-5 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-700 text-white font-black text-lg shadow-2xl hover:scale-105 transition-all duration-300"
          >

            ASSIGN SHIFT

          </button>

        </form>

      </div>

    </div>
  );
}