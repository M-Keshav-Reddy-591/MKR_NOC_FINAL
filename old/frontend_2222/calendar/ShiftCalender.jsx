export default function ShiftCalender() {

  return (

    <div className="p-10 text-white">

      <h1 className="text-4xl font-bold mb-6">
        Shift Calendar
      </h1>

      <div className="bg-gray-900 rounded-2xl p-8">

        <h2 className="text-2xl font-semibold mb-4">
          Weekly Shift Schedule
        </h2>

        <div className="grid grid-cols-7 gap-4">

          <div className="bg-blue-600 p-4 rounded-xl text-center">
            Monday
          </div>

          <div className="bg-green-600 p-4 rounded-xl text-center">
            Tuesday
          </div>

          <div className="bg-purple-600 p-4 rounded-xl text-center">
            Wednesday
          </div>

          <div className="bg-pink-600 p-4 rounded-xl text-center">
            Thursday
          </div>

          <div className="bg-orange-600 p-4 rounded-xl text-center">
            Friday
          </div>

          <div className="bg-red-600 p-4 rounded-xl text-center">
            Saturday
          </div>

          <div className="bg-gray-700 p-4 rounded-xl text-center">
            Sunday
          </div>

        </div>

      </div>

    </div>
  );
}