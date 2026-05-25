export default function LeavePage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-4">
        Leave Management
      </h1>

      <div className="bg-white rounded-2xl shadow-lg p-6">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-3 text-left">Employee</th>
              <th className="p-3 text-left">Leave Type</th>
              <th className="p-3 text-left">Date</th>
              <th className="p-3 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            <tr className="border-b">
              <td className="p-3">Keshav</td>
              <td className="p-3">Sick Leave</td>
              <td className="p-3">25 May 2026</td>
              <td className="p-3">
                <span className="bg-yellow-500 text-white px-3 py-1 rounded-full">
                  Pending
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
} 