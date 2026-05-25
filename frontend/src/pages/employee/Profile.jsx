export default function Profile() {

  return (

    <div className="p-8">

      <h1 className="text-5xl font-bold mb-10">
        Employee Profile
      </h1>

      <div className="bg-white p-8 rounded-3xl shadow-xl max-w-2xl">

        <div className="mb-6">

          <label className="block mb-2 font-bold">
            Employee Name
          </label>

          <input
            type="text"
            value={localStorage.getItem("emp_name")}
            disabled
            className="w-full border p-4 rounded-2xl"
          />

        </div>

        <div className="mb-6">

          <label className="block mb-2 font-bold">
            Employee ID
          </label>

          <input
            type="text"
            value={localStorage.getItem("emp_id")}
            disabled
            className="w-full border p-4 rounded-2xl"
          />

        </div>

      </div>

    </div>
  );
}