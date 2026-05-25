export default function Reports() {

  return (

    <div className="p-8">

      <h1 className="text-5xl font-bold mb-10">
        Reports
      </h1>

      <div className="grid grid-cols-3 gap-6">

        <div className="bg-blue-600 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">
            Daily Reports
          </h2>

          <p className="mt-4">
            Attendance report of today
          </p>

        </div>

        <div className="bg-green-600 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">
            Monthly Reports
          </h2>

          <p className="mt-4">
            Attendance monthly summary
          </p>

        </div>

        <div className="bg-purple-600 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">
            Shift Reports
          </h2>

          <p className="mt-4">
            Shift-wise analytics
          </p>

        </div>

      </div>

    </div>
  );
}