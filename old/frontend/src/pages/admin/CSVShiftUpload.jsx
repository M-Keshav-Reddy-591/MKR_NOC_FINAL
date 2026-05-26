import { useState } from "react";
import axios from "axios";

export default function CSVShiftUpload() {

  const [file, setFile] = useState(null);

  const uploadCSV = async () => {

    const formData = new FormData();

    formData.append("file", file);

    await axios.post(
      "http://127.0.0.1:8000/api/v1/csv/upload-shifts",
      formData
    );

    alert("CSV Uploaded Successfully");
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        CSV Shift Upload
      </h1>

      <div className="bg-white p-8 rounded-2xl shadow-lg">

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
          className="mb-6"
        />

        <button
          onClick={uploadCSV}
          className="bg-blue-600 text-white px-8 py-4 rounded-xl font-bold"
        >
          Upload CSV
        </button>

      </div>

    </div>
  );
}