const stats = [
  {
    title: "Present Days",
    value: 24,
    color: "bg-green-600",
  },
  {
    title: "Absent Days",
    value: 2,
    color: "bg-red-600",
  },
  {
    title: "Shift 1",
    value: 12,
    color: "bg-blue-600",
  },
  {
    title: "Shift 2",
    value: 10,
    color: "bg-purple-600",
  },
];

export default function EmployeeDashboard() {
  const empName =
    localStorage.getItem("emp_name") || "Employee";

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="bg-gradient-to-r from-blue-700 to-indigo-800 text-white rounded-3xl p-8 shadow-2xl">
        <h1 className="text-5xl font-bold">
          Welcome {empName}
        </h1>

        <p className="mt-3 text-xl opacity-90">
          Employee Attendance Portal
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10">
        {stats.map((item, index) => (
          <div
            key={index}
            className={`${item.color} text-white rounded-2xl p-6 shadow-xl`}
          >
            <h2 className="text-2xl font-semibold">
              {item.title}
            </h2>

            <p className="text-5xl font-bold mt-4">
              {item.value}
            </p>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-3xl shadow-2xl mt-10 p-8">
        <h2 className="text-3xl font-bold mb-6">
          Today's Shift
        </h2>

        <div className="grid grid-cols-2 gap-6">
          <div className="bg-blue-100 rounded-2xl p-6">
            <p className="text-gray-600">
              Shift Name
            </p>

            <h3 className="text-3xl font-bold mt-2">
              Shift 1
            </h3>
          </div>

          <div className="bg-green-100 rounded-2xl p-6">
            <p className="text-gray-600">
              Timing
            </p>

            <h3 className="text-3xl font-bold mt-2">
              6 AM - 2 PM
            </h3>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-3xl shadow-2xl mt-10 p-8">
        <h2 className="text-3xl font-bold mb-6">
          Attendance Status
        </h2>

        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-600 text-xl">
              Today
            </p>

            <h2 className="text-4xl font-bold text-green-600 mt-2">
              PRESENT
            </h2>
          </div>

          <button className="bg-blue-700 hover:bg-blue-800 text-white px-8 py-4 rounded-2xl text-xl font-bold transition-all">
            Mark Attendance
          </button>
        </div>
      </div>
    </div>
  );
}