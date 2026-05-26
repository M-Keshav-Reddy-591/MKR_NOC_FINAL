export default function SettingsPage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        System Settings
      </h1>

      <div className="bg-white rounded-2xl shadow-xl p-6 max-w-3xl">
        <div className="mb-5">
          <label className="font-semibold">
            Company Name
          </label>

          <input
            type="text"
            value="MKR NOC"
            className="w-full border p-3 rounded-xl mt-2"
          />
        </div>

        <div className="mb-5">
          <label className="font-semibold">
            Attendance Cutoff Time
          </label>

          <input
            type="time"
            className="w-full border p-3 rounded-xl mt-2"
          />
        </div>

        <div className="mb-5">
          <label className="font-semibold">
            Auto Logout Time
          </label>

          <input
            type="number"
            placeholder="Minutes"
            className="w-full border p-3 rounded-xl mt-2"
          />
        </div>

        <button className="bg-green-600 text-white px-6 py-3 rounded-xl">
          Save Settings
        </button>
      </div>
    </div>
  );
}