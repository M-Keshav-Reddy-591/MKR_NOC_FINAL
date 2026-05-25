export default function ShiftAllocationPage() {
  return (
    <div className="p-6">
      <h1 className="text-4xl font-bold mb-6">
        Shift Allocation
      </h1>

      <div className="bg-white rounded-2xl shadow-xl p-6">
        <div className="grid grid-cols-3 gap-5">
          <input
            type="text"
            placeholder="Employee ID"
            className="border p-3 rounded-xl"
          />

          <select className="border p-3 rounded-xl">
            <option>Shift 1</option>
            <option>Shift 2</option>
            <option>Shift 3</option>
          </select>

          <input
            type="date"
            className="border p-3 rounded-xl"
          />
        </div>

        <button className="mt-6 bg-blue-600 text-white px-6 py-3 rounded-xl">
          Allocate Shift
        </button>
      </div>
    </div>
  );
}