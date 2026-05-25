export default function AttendanceControlPage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        Attendance Control
      </h1>

      <div className="grid grid-cols-4 gap-5 mb-6">
        <div className="bg-white p-6 rounded-2xl shadow">
          <h2>Total Employees</h2>
          <h1 className="text-4xl font-bold mt-2">
            120
          </h1>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2>Present</h2>
          <h1 className="text-4xl font-bold text-green-600 mt-2">
            98
          </h1>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2>Absent</h2>
          <h1 className="text-4xl font-bold text-red-600 mt-2">
            22
          </h1>
        </div>

        <div className="bg-white p-6 rounded-2xl shadow">
          <h2>Late</h2>
          <h1 className="text-4xl font-bold text-yellow-500 mt-2">
            5
          </h1>
        </div>
      </div>
    </div>
  );
}