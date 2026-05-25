export default function DownloadAttendance() {

  const downloadAttendance = () => {

    window.open(
      "http://127.0.0.1:8000/api/v1/export/attendance"
    );
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Download Attendance
      </h1>

      <div className="bg-white p-8 rounded-2xl shadow-lg">

        <h2 className="text-2xl font-bold mb-4">
          My Attendance
        </h2>

        <button
          onClick={downloadAttendance}
          className="bg-blue-600 text-white px-8 py-4 rounded-xl font-bold"
        >
          Download CSV
        </button>

      </div>

    </div>
  );
}