import { useNavigate } from "react-router-dom";

export default function Topbar() {

  const navigate = useNavigate();

  const handleLogout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("role");

    navigate("/");

  };

  return (

    <div className="bg-white shadow-md rounded-2xl p-4 mb-6 flex justify-between items-center">

      <div>

        <h1 className="text-2xl font-bold text-blue-800">
          NOC Attendance System
        </h1>

        <p className="text-gray-500">
          Employee Monitoring & Shift Management
        </p>

      </div>

      <button
        onClick={handleLogout}
        className="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-xl transition-all duration-300"
      >
        Logout
      </button>

    </div>

  );

}