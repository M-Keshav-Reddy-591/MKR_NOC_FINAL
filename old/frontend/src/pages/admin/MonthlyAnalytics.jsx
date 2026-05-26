import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

export default function MonthlyAnalytics() {

  const data = [
    { month: "Jan", attendance: 90 },
    { month: "Feb", attendance: 85 },
    { month: "Mar", attendance: 96 },
    { month: "Apr", attendance: 88 },
    { month: "May", attendance: 92 }
  ];

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        Monthly Analytics
      </h1>

      <div className="bg-white p-8 rounded-2xl shadow-lg h-[500px]">

        <ResponsiveContainer width="100%" height="100%">

          <BarChart data={data}>

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="attendance"
              fill="#2563eb"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}