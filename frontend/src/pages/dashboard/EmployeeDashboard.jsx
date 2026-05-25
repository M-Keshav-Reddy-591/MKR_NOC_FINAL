import React from "react";

export default function EmployeeDashboard() {

  return (

    <div className="p-6">

      <h1 className="text-3xl font-bold text-blue-700 mb-6">
        Employee Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-700">
            Attendance
          </h2>

          <p className="text-4xl font-bold text-green-600 mt-4">
            96%
          </p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-700">
            Total Shifts
          </h2>

          <p className="text-4xl font-bold text-blue-600 mt-4">
            24
          </p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-700">
            Leaves
          </h2>

          <p className="text-4xl font-bold text-red-600 mt-4">
            2
          </p>
        </div>

      </div>

    </div>

  );
}