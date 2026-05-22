import Sidebar from "./Sidebar";


export default function DashboardLayout({

    children
}) {

    return (

        <div className="flex min-h-screen bg-slate-100 dark:bg-slate-900 transition-all duration-300">

            <Sidebar />

            <div className="ml-64 flex-1 p-6 text-black dark:text-white">

                {children}

            </div>
        </div>
    );
}