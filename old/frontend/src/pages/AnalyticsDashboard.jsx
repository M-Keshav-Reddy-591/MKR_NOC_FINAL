import {

  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell

} from "recharts";

export default function AnalyticsDashboard() {

  const attendanceData = [

    { day: "Mon", present: 18 },

    { day: "Tue", present: 20 },

    { day: "Wed", present: 17 },

    { day: "Thu", present: 22 },

    { day: "Fri", present: 19 }
  ];

  const shiftData = [

    { name: "Morning", value: 10 },

    { name: "General", value: 8 },

    { name: "Night", value: 6 }
  ];

  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-10">

        Analytics Dashboard

      </h1>

      {/* DASHBOARD CARDS */}

      <div className="grid grid-cols-4 gap-6 mb-10">

        <div className="bg-blue-500 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">

            Total Employees

          </h2>

          <p className="text-5xl mt-4 font-bold">

            24

          </p>

        </div>

        <div className="bg-green-500 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">

            Present Today

          </h2>

          <p className="text-5xl mt-4 font-bold">

            19

          </p>

        </div>

        <div className="bg-red-500 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">

            Absent Today

          </h2>

          <p className="text-5xl mt-4 font-bold">

            5

          </p>

        </div>

        <div className="bg-purple-500 text-white p-8 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold">

            Total Leaves

          </h2>

          <p className="text-5xl mt-4 font-bold">

            12

          </p>

        </div>

      </div>

      {/* CHARTS */}

      <div className="grid grid-cols-2 gap-8">

        {/* BAR CHART */}

        <div className="bg-white p-6 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold mb-6">

            Weekly Attendance

          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <BarChart data={attendanceData}>

              <XAxis dataKey="day" />

              <YAxis />

              <Tooltip />

              <Bar dataKey="present" />

            </BarChart>

          </ResponsiveContainer>

        </div>

        {/* PIE CHART */}

        <div className="bg-white p-6 rounded-3xl shadow-xl">

          <h2 className="text-2xl font-bold mb-6">

            Shift Distribution

          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <PieChart>

              <Pie
                data={shiftData}
                dataKey="value"
                outerRadius={100}
                label
              >

                {shiftData.map((entry, index) => (

                  <Cell key={index} />

                ))}

              </Pie>

              <Tooltip />

            </PieChart>

          </ResponsiveContainer>

        </div>

      </div>

    </div>
  );
}