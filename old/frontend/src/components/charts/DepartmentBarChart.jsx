import {

    BarChart,

    Bar,

    XAxis,

    YAxis,

    CartesianGrid,

    Tooltip,

    ResponsiveContainer

} from "recharts";


export default function DepartmentBarChart({

    data
}) {

    return (

        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6 h-[400px]">

            <h2 className="text-xl font-bold mb-4">

                Department Analytics
            </h2>

            <ResponsiveContainer width="100%" height="100%">

                <BarChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="department" />

                    <YAxis />

                    <Tooltip />

                    <Bar
                        dataKey="employee_count"
                        fill="#3b82f6"
                    />

                </BarChart>
            </ResponsiveContainer>
        </div>
    );
}