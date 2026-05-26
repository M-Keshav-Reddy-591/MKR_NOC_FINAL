export default function MarkAttendance() {

  return (

    <div className="p-8">

      <h1 className="text-5xl font-bold mb-10">
        Mark Attendance
      </h1>

      <div className="grid grid-cols-2 gap-8">

        <button className="bg-green-600 text-white p-10 rounded-3xl shadow-xl text-3xl font-bold">

          Check In

        </button>

        <button className="bg-red-600 text-white p-10 rounded-3xl shadow-xl text-3xl font-bold">

          Check Out

        </button>

      </div>

    </div>
  );
}