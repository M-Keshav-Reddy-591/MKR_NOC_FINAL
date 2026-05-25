export default function ExportReports() {

  const downloadReport = () => {

    window.open(
      "http://127.0.0.1:8000/api/v1/export/attendance"
    );
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Export Reports
      </h1>

      <div className="bg-white p-8 rounded-2xl shadow-lg">

        <h2 className="text-2xl font-bold mb-4">
          Attendance Reports
        </h2>

        <p className="text-gray-500 mb-6">
          Download complete attendance CSV report
        </p>

        <button
          onClick={downloadReport}
          className="bg-green-600 text-white px-8 py-4 rounded-xl font-bold"
        >
          Download Attendance CSV
        </button>

      </div>

    </div>
  );
}