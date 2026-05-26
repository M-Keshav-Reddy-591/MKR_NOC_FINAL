import { useState } from "react";

function EmployeeActivityMonitor() {
  const [employees] = useState([
    {
      id: "EMP001",
      name: "Keshav",
      department: "NOC",
      shift: "Shift 1",
      loginTime: "09:00 AM",
      status: "Online",
      system: "Firewall Monitoring",
      productivity: "98%",
    },
    {
      id: "EMP002",
      name: "Rahul",
      department: "Network",
      shift: "Shift 2",
      loginTime: "02:00 PM",
      status: "Busy",
      system: "VPN Support",
      productivity: "92%",
    },
    {
      id: "EMP003",
      name: "Suresh",
      department: "SOC",
      shift: "Shift 3",
      loginTime: "10:15 PM",
      status: "Offline",
      system: "SIEM Dashboard",
      productivity: "88%",
    },
  ]);

  const getStatusStyle = (status) => {
    switch (status) {
      case "Online":
        return "bg-green-500";

      case "Busy":
        return "bg-yellow-500";

      case "Offline":
        return "bg-red-500";

      default:
        return "bg-gray-500";
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      {/* HEADER */}

      <div className="bg-gradient-to-r from-cyan-900 via-slate-900 to-black rounded-3xl p-8 shadow-xl mb-8">
        <h1 className="text-4xl font-bold">
          Employee Activity Monitor
        </h1>

        <p className="text-gray-400 mt-2">
          Real-time employee monitoring and operations tracking
        </p>
      </div>

      {/* TOP CARDS */}

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 shadow-lg">
          <h2 className="text-gray-400">Total Employees</h2>

          <p className="text-4xl font-bold mt-2">48</p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 shadow-lg">
          <h2 className="text-gray-400">Online</h2>

          <p className="text-4xl font-bold mt-2 text-green-400">
            36
          </p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 shadow-lg">
          <h2 className="text-gray-400">Busy</h2>

          <p className="text-4xl font-bold mt-2 text-yellow-400">
            8
          </p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 shadow-lg">
          <h2 className="text-gray-400">Offline</h2>

          <p className="text-4xl font-bold mt-2 text-red-400">
            4
          </p>
        </div>
      </div>

      {/* EMPLOYEE TABLE */}

      <div className="bg-slate-900 rounded-2xl overflow-hidden border border-slate-800 shadow-lg">
        <div className="p-6 border-b border-slate-800">
          <h2 className="text-2xl font-bold">
            Live Employee Activity
          </h2>
        </div>

        <table className="w-full">
          <thead className="bg-slate-800">
            <tr>
              <th className="p-4 text-left">Employee ID</th>
              <th className="p-4 text-left">Employee</th>
              <th className="p-4 text-left">Department</th>
              <th className="p-4 text-left">Shift</th>
              <th className="p-4 text-left">Login Time</th>
              <th className="p-4 text-left">Current System</th>
              <th className="p-4 text-left">Productivity</th>
              <th className="p-4 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            {employees.map((employee, index) => (
              <tr
                key={index}
                className="border-b border-slate-800 hover:bg-slate-800 transition"
              >
                <td className="p-4">{employee.id}</td>

                <td className="p-4 font-semibold">
                  {employee.name}
                </td>

                <td className="p-4">{employee.department}</td>

                <td className="p-4">{employee.shift}</td>

                <td className="p-4">{employee.loginTime}</td>

                <td className="p-4">{employee.system}</td>

                <td className="p-4 text-cyan-400 font-bold">
                  {employee.productivity}
                </td>

                <td className="p-4">
                  <div className="flex items-center gap-2">
                    <div
                      className={`w-3 h-3 rounded-full ${getStatusStyle(
                        employee.status
                      )} ${
                        employee.status !== "Offline"
                          ? "animate-pulse"
                          : ""
                      }`}
                    ></div>

                    <span>{employee.status}</span>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* FOOTER */}

      <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold mb-2">
            Highest Productivity
          </h2>

          <p className="text-green-400 text-3xl font-bold">
            Keshav - 98%
          </p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold mb-2">
            Active Shift
          </h2>

          <p className="text-cyan-400 text-3xl font-bold">
            Shift 2
          </p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800">
          <h2 className="text-xl font-bold mb-2">
            NOC Health
          </h2>

          <p className="text-green-400 text-3xl font-bold">
            Stable
          </p>
        </div>
      </div>
    </div>
  );
}

export default EmployeeActivityMonitor;