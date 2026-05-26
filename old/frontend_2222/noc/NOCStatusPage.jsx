import { useEffect, useState } from "react";

export default function NOCStatusPage() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-4xl font-bold">
          NOC Live Status
        </h1>

        <div className="bg-black text-green-400 px-5 py-3 rounded-xl text-xl font-bold">
          {time.toLocaleTimeString()}
        </div>
      </div>

      <div className="grid grid-cols-4 gap-5">
        <div className="bg-green-500 text-white p-6 rounded-2xl shadow-xl">
          <h2 className="text-xl">Employees Online</h2>
          <h1 className="text-5xl font-bold mt-4">86</h1>
        </div>

        <div className="bg-blue-600 text-white p-6 rounded-2xl shadow-xl">
          <h2 className="text-xl">Current Shift</h2>
          <h1 className="text-5xl font-bold mt-4">Shift 2</h1>
        </div>

        <div className="bg-red-500 text-white p-6 rounded-2xl shadow-xl">
          <h2 className="text-xl">Absent Today</h2>
          <h1 className="text-5xl font-bold mt-4">12</h1>
        </div>

        <div className="bg-yellow-500 text-white p-6 rounded-2xl shadow-xl">
          <h2 className="text-xl">Late Entries</h2>
          <h1 className="text-5xl font-bold mt-4">5</h1>
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow-xl mt-8 p-6">
        <h2 className="text-2xl font-bold mb-4">
          Active Shift Employees
        </h2>

        <table className="w-full">
          <thead>
            <tr className="bg-gray-100">
              <th className="p-3 text-left">EMP ID</th>
              <th className="p-3 text-left">Name</th>
              <th className="p-3 text-left">Department</th>
              <th className="p-3 text-left">Status</th>
            </tr>
          </thead>

          <tbody>
            <tr className="border-b">
              <td className="p-3">EMP001</td>
              <td className="p-3">Keshav</td>
              <td className="p-3">NOC</td>
              <td className="p-3 text-green-600 font-bold">
                ACTIVE
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}