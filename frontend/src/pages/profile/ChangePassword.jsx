import { useState } from "react";
import axios from "axios";

export default function ChangePassword() {

  const [password, setPassword] = useState("");

  const empId = localStorage.getItem("emp_id");

  // const handleChange = async () => {

  //   try {

  //     await axios.put(
  //       `http://127.0.0.1:8000/api/v1/employees/change-password/${empId}`,
  //       {
  //         password: password
  //       }
  //     );

  //     alert("Password Updated Successfully");

  //     setPassword("");

  //   } catch (err) {

  //     alert("Password Update Failed");
  //   }
  // };
  const handlePasswordChange = async () => {

  try {

    const response = await axios.post(
      "http://127.0.0.1:8000/api/v1/auth/change-password",
      {
        employee_id: localStorage.getItem("employee_id"),
        old_password: oldPassword,
        new_password: newPassword
      }
    );

    alert(response.data.message);

    setOldPassword("");
    setNewPassword("");

  } catch (error) {

    console.log(error);

    if (error.response) {

      alert(error.response.data.detail);

    } else {

      alert("Server Error");
    }
  }
};

  return (

    <div className="p-8">

      <div className="bg-white rounded-2xl shadow-xl p-8 max-w-xl">

        <h1 className="text-3xl font-bold mb-6">
          Change Password
        </h1>

        <input
          type="password"
          placeholder="New Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-4 rounded-xl mb-6"
        />

        <button
          onClick={handleChange}
          className="bg-blue-600 text-white px-8 py-3 rounded-xl font-bold"
        >
          Update Password
        </button>

      </div>

    </div>
  );
}