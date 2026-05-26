import { useState } from "react";
import axios from "axios";

export default function LeaveManagement() {

  const [form, setForm] = useState({

    employee_id: "",

    leave_type: "",

    start_date: "",

    end_date: "",

    reason: ""
  });

  const applyLeave = async () => {

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/v1/leaves/apply",
        form
      );

      alert("Leave Applied");

    } catch (error) {

      alert("Error");
    }
  };

  return (

    <div className="min-h-screen bg-gray-100 p-10">

      <div className="max-w-2xl mx-auto bg-white p-10 rounded-3xl shadow-2xl">

        <h1 className="text-4xl font-bold mb-10 text-center text-blue-600">

          Leave Management

        </h1>

        <div className="space-y-5">

          <input
            type="number"
            placeholder="Employee ID"
            className="w-full border p-4 rounded-xl"
            onChange={(e) =>
              setForm({
                ...form,
                employee_id: e.target.value
              })
            }
          />

          <select
            className="w-full border p-4 rounded-xl"
            onChange={(e) =>
              setForm({
                ...form,
                leave_type: e.target.value
              })
            }
          >

            <option>Select Leave Type</option>

            <option>Sick Leave</option>

            <option>Casual Leave</option>

            <option>Emergency Leave</option>

          </select>

          <input
            type="date"
            className="w-full border p-4 rounded-xl"
            onChange={(e) =>
              setForm({
                ...form,
                start_date: e.target.value
              })
            }
          />

          <input
            type="date"
            className="w-full border p-4 rounded-xl"
            onChange={(e) =>
              setForm({
                ...form,
                end_date: e.target.value
              })
            }
          />

          <textarea
            placeholder="Reason"
            className="w-full border p-4 rounded-xl"
            onChange={(e) =>
              setForm({
                ...form,
                reason: e.target.value
              })
            }
          />

          <button
            onClick={applyLeave}
            className="w-full bg-blue-600 text-white py-4 rounded-xl font-bold text-lg"
          >
            Apply Leave
          </button>

        </div>

      </div>
    </div>
  );
}