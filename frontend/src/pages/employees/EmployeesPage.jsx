const employees = [
  {
    id: "EMP001",
    name: "Keshav",
    department: "NOC",
    shift: "Shift 1",
    status: "Present",
  },
  {
    id: "EMP002",
    name: "Rahul",
    department: "SOC",
    shift: "Shift 2",
    status: "Absent",
  },
];

export default function EmployeesPage() {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold mb-6">
        Employees
      </h1>

      <div className="bg-white rounded-2xl shadow-xl p-6">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-4 text-left">EMP ID</th>
              <th className="p-4 text-left">Name</th>
              <th className="p-4 text-left">Department</th>
              <th className="p-4 text-left">Shift</th>
              <th className="p-4 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            {employees.map((emp, index) => (
              <tr key={index} className="border-b">
                <td className="p-4">{emp.id}</td>
                <td className="p-4">{emp.name}</td>
                <td className="p-4">{emp.department}</td>
                <td className="p-4">{emp.shift}</td>

                <td className="p-4">
                  <span
                    className={`px-4 py-1 rounded-full text-white ${
                      emp.status === "Present"
                        ? "bg-green-600"
                        : "bg-red-600"
                    }`}
                  >
                    {emp.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}