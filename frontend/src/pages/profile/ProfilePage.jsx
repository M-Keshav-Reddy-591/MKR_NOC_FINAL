export default function ProfilePage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        Profile
      </h1>

      <div className="bg-white rounded-2xl shadow-lg p-6 max-w-2xl">
        <div className="mb-4">
          <label className="font-semibold">
            Employee ID
          </label>

          <input
            type="text"
            value="EMP001"
            className="w-full border p-3 rounded-xl mt-2"
            readOnly
          />
        </div>

        <div className="mb-4">
          <label className="font-semibold">
            Employee Name
          </label>

          <input
            type="text"
            value="Keshav"
            className="w-full border p-3 rounded-xl mt-2"
          />
        </div>

        <div className="mb-4">
          <label className="font-semibold">
            Department
          </label>

          <input
            type="text"
            value="NOC"
            className="w-full border p-3 rounded-xl mt-2"
          />
        </div>

        <button className="bg-blue-600 text-white px-6 py-3 rounded-xl">
          Update Profile
        </button>
      </div>
    </div>
  );
}