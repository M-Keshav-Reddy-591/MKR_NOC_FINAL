import { useState } from "react";
import axios from "axios";

export default function RosterUpload() {

  const [file, setFile] = useState(null);

  const handleUpload = async () => {

    const formData = new FormData();

    formData.append("file", file);

    try {

      const response = await axios.post(

        "http://127.0.0.1:8000/api/v1/shift-upload/",

        formData

      );

      alert(response.data.message);

    } catch {

      alert("Upload Failed");
    }
  };

  return (

    <div className="p-8">

      <div className="bg-white rounded-2xl p-8 shadow-xl">

        <h1 className="text-3xl font-bold mb-8">

          Upload Shift Roster

        </h1>

        <input
          type="file"
          accept=".csv"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
          className="mb-6"
        />

        <button
          onClick={handleUpload}
          className="bg-green-600 text-white px-8 py-3 rounded-xl font-bold"
        >
          Upload CSV
        </button>

      </div>

    </div>
  );
}