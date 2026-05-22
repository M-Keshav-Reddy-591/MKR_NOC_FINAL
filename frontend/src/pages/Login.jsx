import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

export default function Login() {
  const navigate = useNavigate();

  const [employeeId, setEmployeeId] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("employee");

  const loginUser = async (e) => {
    e.preventDefault();

    try {
      const response = await API.post("/auth/login", {
        employee_id: employeeId,
        password: password,
        role: role,
      });

      localStorage.setItem("token", response.data.access_token);

      if (role === "admin") {
        navigate("/admin-dashboard");
      } else {
        navigate("/employee-dashboard");
      }
    } catch (error) {
      console.log(error);
      alert("Invalid Login");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">
      <form
        onSubmit={loginUser}
        className="bg-white p-10 rounded-xl shadow-xl w-[400px]"
      >
        <h1 className="text-3xl font-bold mb-6 text-center">
          NOC Attendance System
        </h1>

        <div className="mb-4">
          <label className="font-semibold">Employee ID</label>
          <input
            type="text"
            className="w-full border p-3 rounded mt-2"
            value={employeeId}
            onChange={(e) => setEmployeeId(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <label className="font-semibold">Password</label>
          <input
            type="password"
            className="w-full border p-3 rounded mt-2"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <div className="mb-6">
          <label className="font-semibold">Login Type</label>

          <select
            className="w-full border p-3 rounded mt-2"
            value={role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option value="employee">Employee Login</option>
            <option value="admin">Admin Login</option>
          </select>
        </div>

        <button className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700">
          Login
        </button>
      </form>
    </div>
  );
}