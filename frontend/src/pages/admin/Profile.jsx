import { useState } from "react";

export default function Profile() {

  const [password, setPassword] = useState("");

  return (

    <div className="p-8">

      <h1 className="text-5xl font-bold mb-10">
        Admin Profile
      </h1>

      <div className="bg-white p-8 rounded-3xl shadow-xl max-w-2xl">

        <div className="mb-6">

          <label className="block mb-2 font-bold">
            Admin Name
          </label>

          <input
            type="text"
            value="Keshav"
            disabled
            className="w-full border p-4 rounded-2xl"
          />

        </div>

        <div className="mb-6">

          <label className="block mb-2 font-bold">
            Change Password
          </label>

          <input
            type="password"
            placeholder="New Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full border p-4 rounded-2xl"
          />

        </div>

        <button className="bg-blue-600 text-white px-8 py-4 rounded-2xl font-bold">

          Update Profile

        </button>

      </div>

    </div>
  );
}