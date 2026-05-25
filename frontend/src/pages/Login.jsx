import { useState } from "react";
import axios from "axios";

export default function Login() {

  const [role, setRole] = useState("employee");

  const [empId, setEmpId] = useState("");

  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {

    if (!empId || !password) {

      alert("Please fill all fields");

      return;
    }

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/login",
        {
          emp_id: empId,
          password: password,
          role: role
        }
      );

      console.log(response.data);

      localStorage.setItem(
        "token",
        response.data.access_token
      );

      localStorage.setItem(
        "role",
        response.data.role
      );

      localStorage.setItem(
        "emp_id",
        response.data.emp_id
      );

      localStorage.setItem(
        "emp_name",
        response.data.emp_name
      );

      alert("Login Successful");

      if (response.data.role === "admin") {

        window.location.href = "/admin-dashboard";

      } else {

        window.location.href = "/employee-dashboard";
      }

    } catch (error) {

      console.log(error);

      if (error.response) {

        alert(error.response.data.detail);

      } else {

        alert("Server Error");
      }

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 flex items-center justify-center p-6">

      <div className="bg-white/10 backdrop-blur-lg border border-white/20 shadow-2xl rounded-3xl w-full max-w-md p-10">

        <div className="text-center mb-10">

          <h1 className="text-4xl font-bold text-white mb-3">
            NOC SYSTEM
          </h1>

          <p className="text-slate-300">
            Network Operations Attendance Portal
          </p>

        </div>

        {/* ROLE BUTTONS */}

        <div className="flex gap-4 mb-8">

          <button
            onClick={() => setRole("admin")}
            className={`flex-1 py-3 rounded-2xl font-bold transition-all duration-300 ${
              role === "admin"
                ? "bg-blue-600 text-white shadow-lg"
                : "bg-white/20 text-white"
            }`}
          >
            Admin
          </button>

          <button
            onClick={() => setRole("employee")}
            className={`flex-1 py-3 rounded-2xl font-bold transition-all duration-300 ${
              role === "employee"
                ? "bg-green-600 text-white shadow-lg"
                : "bg-white/20 text-white"
            }`}
          >
            Employee
          </button>

        </div>

        {/* EMPLOYEE ID */}

        <div className="mb-5">

          <label className="text-white block mb-2">
            Employee ID
          </label>

          <input
            type="text"
            placeholder="Enter Employee ID"
            value={empId}
            onChange={(e) => setEmpId(e.target.value)}
            className="w-full p-4 rounded-2xl bg-white/20 border border-white/20 text-white placeholder-gray-300 outline-none focus:ring-2 focus:ring-blue-400"
          />

        </div>

        {/* PASSWORD */}

        <div className="mb-8">

          <label className="text-white block mb-2">
            Password
          </label>

          <input
            type="password"
            placeholder="Enter Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-4 rounded-2xl bg-white/20 border border-white/20 text-white placeholder-gray-300 outline-none focus:ring-2 focus:ring-blue-400"
          />

        </div>

        {/* LOGIN BUTTON */}

        <button
          onClick={handleLogin}
          disabled={loading}
          className={`w-full py-4 rounded-2xl text-white font-bold text-lg transition-all duration-300 ${
            role === "admin"
              ? "bg-blue-600 hover:bg-blue-700"
              : "bg-green-600 hover:bg-green-700"
          }`}
        >

          {loading ? "Logging in..." : `Login as ${role}`}

        </button>

      </div>

    </div>
  );
}