import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {

  const navigate = useNavigate();

  const [employeeId, setEmployeeId] = useState("");
  const [password, setPassword] = useState("");
  const [loginType, setLoginType] = useState("employee");

  const handleLogin = async (e) => {

    e.preventDefault();

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/login",
        {
          emp_id: employeeId,
          password: password,
          role: loginType
        }
      );

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      localStorage.setItem(
        "user",
        JSON.stringify(response.data.user)
      );

      if (response.data.user.role === "admin") {

        navigate("/admin-dashboard");

      } else {

        navigate("/employee-dashboard");

      }

    } catch (error) {

      console.log(error);

      alert("Invalid Employee ID or Password");

    }

  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-950 via-blue-950 to-black px-4">

      <div className="w-full max-w-md bg-white/10 backdrop-blur-xl border border-white/20 rounded-3xl shadow-2xl p-8">

        <div className="text-center mb-8">

          <h1 className="text-4xl font-extrabold text-white mb-2">
            NOC Attendance
          </h1>

          <p className="text-gray-300">
            Smart Employee Shift & Attendance System
          </p>

        </div>

        {/* LOGIN TYPE BUTTONS */}

        <div className="flex gap-4 mb-8">

          <button
            onClick={() => setLoginType("admin")}
            className={`w-1/2 py-3 rounded-xl font-bold transition-all duration-300 ${
              loginType === "admin"
                ? "bg-red-600 text-white shadow-lg"
                : "bg-white/10 text-gray-300 border border-white/20"
            }`}
          >
            Admin Login
          </button>

          <button
            onClick={() => setLoginType("employee")}
            className={`w-1/2 py-3 rounded-xl font-bold transition-all duration-300 ${
              loginType === "employee"
                ? "bg-blue-600 text-white shadow-lg"
                : "bg-white/10 text-gray-300 border border-white/20"
            }`}
          >
            Employee Login
          </button>

        </div>

        {/* LOGIN FORM */}

        <form onSubmit={handleLogin} className="space-y-6">

          <div>

            <label className="block text-white mb-2 font-medium">
              Employee ID
            </label>

            <input
              type="text"
              placeholder="Enter Employee ID"
              value={employeeId}
              onChange={(e) => setEmployeeId(e.target.value)}
              className="w-full px-4 py-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />

          </div>

          <div>

            <label className="block text-white mb-2 font-medium">
              Password
            </label>

            <input
              type="password"
              placeholder="Enter Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />

          </div>

          <button
            type="submit"
            className={`w-full py-3 rounded-xl font-bold text-white transition-all duration-300 ${
              loginType === "admin"
                ? "bg-red-600 hover:bg-red-700"
                : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loginType === "admin"
              ? "Login as Admin"
              : "Login as Employee"}
          </button>

        </form>

        <div className="mt-8 text-center text-gray-400 text-sm">
          NOC Monitoring & Shift Management Platform
        </div>

      </div>

    </div>

  );

};

export default Login;