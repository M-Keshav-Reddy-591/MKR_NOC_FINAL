export default function KPISection({

    title,

    value,

    color
}) {

    return (

        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

            <h2 className="text-gray-500 dark:text-gray-300 text-sm">

                {title}
            </h2>

            <p className={`text-4xl font-bold mt-3 ${color}`}>

                {value}
            </p>
        </div>
    );
}