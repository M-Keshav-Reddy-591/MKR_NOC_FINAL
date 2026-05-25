import {
  Users,
  CalendarCheck,
  AlertTriangle,
} from "lucide-react";

export default function AdminDashboard() {
  return (
    <div>
      <h1 className="text-4xl font-bold mb-6">
        Admin Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow">
          <div className="flex justify-between">
            <div>
              <p>Total Employees</p>
              <h2 className="text-3xl font-bold">24</h2>
            </div>

            <Users className="text-blue-600" size={40} />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <div className="flex justify-between">
            <div>
              <p>Present Today</p>
              <h2 className="text-3xl font-bold text-green-600">
                20
              </h2>
            </div>

            <CalendarCheck
              className="text-green-600"
              size={40}
            />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow">
          <div className="flex justify-between">
            <div>
              <p>Absent Alerts</p>
              <h2 className="text-3xl font-bold text-red-600">
                4
              </h2>
            </div>

            <AlertTriangle
              className="text-red-600"
              size={40}
            />
          </div>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow p-6 mt-8">
        <h2 className="text-2xl font-bold mb-4">
          Live Monitoring
        </h2>

        <table className="w-full">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-3 text-left">Employee</th>
              <th className="p-3 text-left">Department</th>
              <th className="p-3 text-left">Shift</th>
              <th className="p-3 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            <tr className="border-b">
              <td className="p-3">Keshav</td>
              <td className="p-3">NOC</td>
              <td className="p-3">Shift 1</td>
              <td className="p-3 text-green-600">
                Present
              </td>
            </tr>

            <tr>
              <td className="p-3">Ravi</td>
              <td className="p-3">NOC</td>
              <td className="p-3">Shift 2</td>
              <td className="p-3 text-red-600">
                Absent
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}