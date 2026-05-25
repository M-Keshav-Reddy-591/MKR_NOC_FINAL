import { useState } from "react";
import axios from "axios";

export default function ChangePassword() {

  const [password, setPassword] = useState("");

  const updatePassword = async () => {

    const empId = localStorage.getItem("emp_id");

    await axios.put(
      `http://127.0.0.1:8000/api/v1/employees/change-password/${empId}`,
      {
        password: password
      }
    );

    alert("Password Updated");
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Change Password
      </h1>

      <div className="bg-white p-8 rounded-2xl shadow-lg">

        <input
          type="password"
          placeholder="New Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          className="w-full border p-4 rounded-xl mb-6"
        />

        <button
          onClick={updatePassword}
          className="bg-green-600 text-white px-8 py-4 rounded-xl font-bold"
        >
          Update Password
        </button>

      </div>

    </div>
  );
}