export default function EmptyState({

    title,

    subtitle
}) {

    return (

        <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-10 text-center">

            <h2 className="text-2xl font-bold text-gray-700">

                {title}
            </h2>

            <p className="text-gray-500 dark:text-gray-300 mt-3">

                {subtitle}
            </p>
        </div>
    );
}