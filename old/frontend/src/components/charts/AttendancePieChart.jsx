import {

    PieChart,

    Pie,

    Cell,

    Tooltip,

    ResponsiveContainer

} from "recharts";


const COLORS = [

    "#22c55e",

    "#ef4444",

    "#eab308",

    "#3b82f6"
];


export default function AttendancePieChart({

    data
}) {

    return (

        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6 h-[400px]">

            <h2 className="text-xl font-bold mb-4">

                Attendance Overview
            </h2>

            <ResponsiveContainer width="100%" height="100%">

                <PieChart>

                    <Pie
                        data={data}
                        dataKey="value"
                        outerRadius={120}
                        label
                    >

                        {data.map((entry, index) => (

                            <Cell
                                key={index}
                                fill={COLORS[index % COLORS.length]}
                            />
                        ))}
                    </Pie>

                    <Tooltip />

                </PieChart>
            </ResponsiveContainer>
        </div>
    );
}