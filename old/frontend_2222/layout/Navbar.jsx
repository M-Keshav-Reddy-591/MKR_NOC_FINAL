export default function Navbar() {

    const role = localStorage.getItem(
        "role"
    );


    return (

        <div className="h-16 bg-white dark:bg-slate-800 shadow flex items-center justify-between px-6">

            <h1 className="text-2xl font-bold">

                Dashboard
            </h1>

            <div className="bg-blue-100 text-blue-700 px-4 py-2 rounded-lg">

                {role}
            </div>
        </div>
    );
}