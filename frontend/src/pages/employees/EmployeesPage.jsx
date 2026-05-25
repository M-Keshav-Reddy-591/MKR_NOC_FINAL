export default function EmployeesPage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        Employees
      </h1>

      <div className="bg-white rounded-2xl shadow-lg p-6">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-3 text-left">EMP ID</th>
              <th className="p-3 text-left">Name</th>
              <th className="p-3 text-left">Department</th>
              <th className="p-3 text-left">Role</th>
            </tr>
          </thead>

          <tbody>
            <tr className="border-b">
              <td className="p-3">EMP001</td>
              <td className="p-3">Keshav</td>
              <td className="p-3">NOC</td>
              <td className="p-3">Admin</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}