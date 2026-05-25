function LiveShiftBoard() {
  const shiftData = [
    {
      shift: "Shift 1",
      employees: 12,
      status: "Active",
    },
    {
      shift: "Shift 2",
      employees: 10,
      status: "Running",
    },
    {
      shift: "Shift 3",
      employees: 8,
      status: "Upcoming",
    },
  ];

  const employeeData = [
    {
      name: "Keshav",
      shift: "Shift 1",
      login: "09:01 AM",
      status: "Online",
    },
    {
      name: "Rahul",
      shift: "Shift 2",
      login: "02:00 PM",
      status: "Active",
    },
    {
      name: "Suresh",
      shift: "Shift 1",
      login: "09:15 AM",
      status: "Offline",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      {/* HEADER */}

      <div className="bg-gradient-to-r from-blue-900 via-slate-900 to-black rounded-3xl p-8 mb-8 shadow-xl">
        <h1 className="text-4xl font-bold">
          Live Shift Monitoring Board
        </h1>

        <p className="text-gray-400 mt-2">
          Real-time NOC shift operations and employee activity
        </p>
      </div>

      {/* SHIFT CARDS */}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {shiftData.map((shift, index) => (
          <div
            key={index}
            className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg hover:scale-105 transition"
          >
            <h2 className="text-2xl font-bold mb-4">
              {shift.shift}
            </h2>

            <p className="text-gray-400">
              Employees: {shift.employees}
            </p>

            <div className="flex items-center gap-2 mt-4">
              <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>

              <span>{shift.status}</span>
            </div>
          </div>
        ))}
      </div>

      {/* EMPLOYEE TABLE */}

      <div className="bg-slate-900 rounded-2xl overflow-hidden border border-slate-800 shadow-lg">
        <div className="p-6 border-b border-slate-800">
          <h2 className="text-2xl font-bold">
            Active Employees
          </h2>
        </div>

        <table className="w-full">
          <thead className="bg-slate-800">
            <tr>
              <th className="p-4 text-left">Employee</th>
              <th className="p-4 text-left">Shift</th>
              <th className="p-4 text-left">Login Time</th>
              <th className="p-4 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            {employeeData.map((employee, index) => (
              <tr
                key={index}
                className="border-b border-slate-800 hover:bg-slate-800 transition"
              >
                <td className="p-4">{employee.name}</td>

                <td className="p-4">{employee.shift}</td>

                <td className="p-4">{employee.login}</td>

                <td className="p-4">
                  <div className="flex items-center gap-2">
                    {employee.status === "Offline" ? (
                      <div className="w-3 h-3 rounded-full bg-red-500"></div>
                    ) : (
                      <div className="w-3 h-3 rounded-full bg-green-500 animate-pulse"></div>
                    )}

                    <span>{employee.status}</span>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default LiveShiftBoard;