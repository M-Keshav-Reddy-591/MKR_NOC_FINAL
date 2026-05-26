export default function EmployeeDashboard() {

  return (

    <div className="p-8">

      <h1 className="text-5xl font-bold mb-10">
        Employee Dashboard
      </h1>

      <div className="grid grid-cols-2 gap-6 mb-10">

        <div className="bg-green-600 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">
            Upcoming Shift
          </h2>

          <p className="text-3xl mt-4">
            Morning Shift
          </p>

        </div>

        <div className="bg-blue-600 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">
            Completed Shifts
          </h2>

          <p className="text-5xl mt-4 font-bold">
            18
          </p>

        </div>

      </div>

      <div className="bg-white p-8 rounded-3xl shadow-xl">

        <h2 className="text-3xl font-bold mb-6">
          Recent Shift History
        </h2>

        <table className="w-full">

          <thead>

            <tr className="bg-gray-100">

              <th className="p-4 text-left">
                Date
              </th>

              <th className="p-4 text-left">
                Shift
              </th>

              <th className="p-4 text-left">
                Status
              </th>

            </tr>

          </thead>

          <tbody>

            <tr className="border-b">

              <td className="p-4">
                2026-05-25
              </td>

              <td className="p-4">
                Morning
              </td>

              <td className="p-4 text-green-600 font-bold">
                Completed
              </td>

            </tr>

          </tbody>

        </table>

      </div>

    </div>
  );
}