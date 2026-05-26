import { useState } from "react";
import axios from "axios";

export default function Login() {

  const [role, setRole] = useState("employee");

  const [empId, setEmpId] = useState("");

  const [password, setPassword] = useState("");

  const handleLogin = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/login",
        {
          emp_id: empId,
          password: password,
          role: role
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      localStorage.setItem(
        "role",
        role
      );

      alert("Login Successful");

      if (role === "admin") {

        window.location.href = "/admin-dashboard";

      } else {

        window.location.href = "/employee-dashboard";
      }

    } catch (error) {

      alert("Invalid Credentials");
    }
  };

  return (

    <div className="min-h-screen bg-gray-900 flex items-center justify-center">

      <div className="bg-white p-10 rounded-2xl shadow-2xl w-[420px]">

        <h1 className="text-3xl font-bold text-center mb-8 text-gray-800">

          NOC Attendance System

        </h1>

        {/* LOGIN BUTTONS */}

        <div className="flex gap-4 mb-8">

          <button
            onClick={() => setRole("admin")}
            className={`flex-1 py-3 rounded-xl font-semibold transition-all ${
              role === "admin"
                ? "bg-blue-600 text-white"
                : "bg-gray-200"
            }`}
          >
            Admin Login
          </button>

          <button
            onClick={() => setRole("employee")}
            className={`flex-1 py-3 rounded-xl font-semibold transition-all ${
              role === "employee"
                ? "bg-green-600 text-white"
                : "bg-gray-200"
            }`}
          >
            Employee Login
          </button>

        </div>

        {/* FORM */}

        <input
          type="text"
          placeholder="Employee ID"
          value={empId}
          onChange={(e) => setEmpId(e.target.value)}
          className="w-full border p-3 rounded-xl mb-4"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full border p-3 rounded-xl mb-6"
        />

        <button
          onClick={handleLogin}
          className={`w-full py-3 rounded-xl text-white font-bold text-lg ${
            role === "admin"
              ? "bg-blue-600"
              : "bg-green-600"
          }`}
        >
          Login as {role}
        </button>

      </div>
    </div>
  );
}