import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {

    const location = useLocation();

    const user = JSON.parse(localStorage.getItem("user"));

    const isAdmin = user?.role === "admin";

    const adminMenu = [

        {
            name: "Dashboard",
            path: "/admin-dashboard"
        },

        {
            name: "Attendance Control",
            path: "/admin-attendance"
        },

        {
            name: "Employees",
            path: "/employees"
        },

        {
            name: "Shift Allocation",
            path: "/shift-allocation"
        },

        {
            name: "Shift Swaps",
            path: "/shift-swaps"
        },

        {
            name: "Reports",
            path: "/reports"
        },

        {
            name: "Profile",
            path: "/profile"
        }
    ];


    const employeeMenu = [

        {
            name: "Dashboard",
            path: "/employee-dashboard"
        },

        {
            name: "Mark Attendance",
            path: "/attendance"
        },

        {
            name: "Shift Swaps",
            path: "/shift-swaps"
        },

        {
            name: "Profile",
            path: "/profile"
        }
    ];


    const menuItems = isAdmin
        ? adminMenu
        : employeeMenu;


    return (

        <div className="w-72 min-h-screen bg-gray-950 text-white border-r border-gray-800 flex flex-col">

            {/* TOP LOGO */}

            <div className="p-6 border-b border-gray-800">

                <h1 className="text-3xl font-bold text-blue-500">

                    NOC SYSTEM

                </h1>

                <p className="text-sm text-gray-400 mt-1">

                    Attendance Management
                </p>

            </div>


            {/* USER INFO */}

            <div className="p-6 border-b border-gray-800">

                <div className="bg-gray-900 rounded-2xl p-4">

                    <h2 className="text-lg font-semibold">

                        {user?.full_name}
                    </h2>

                    <p className="text-sm text-gray-400 mt-1">

                        {user?.role?.toUpperCase()}
                    </p>

                    <p className="text-sm text-gray-500">

                        {user?.emp_id}
                    </p>

                </div>

            </div>


            {/* MENU */}

            <div className="flex-1 p-4">

                <div className="space-y-2">

                    {

                        menuItems.map((item) => (

                            <Link

                                key={item.path}

                                to={item.path}

                                className={`block px-5 py-4 rounded-2xl transition-all duration-300 font-medium

                                ${
                                    location.pathname === item.path

                                    ? "bg-blue-600 text-white shadow-lg"

                                    : "bg-gray-900 hover:bg-gray-800 text-gray-300"
                                }
                                `}
                            >

                                {item.name}

                            </Link>
                        ))
                    }

                </div>

            </div>


            {/* FOOTER */}

            <div className="p-6 border-t border-gray-800">

                <button

                    onClick={() => {

                        localStorage.clear();

                        window.location.href = "/";
                    }}

                    className="w-full bg-red-600 hover:bg-red-700 py-3 rounded-2xl font-semibold transition-all"
                >

                    Logout

                </button>

            </div>

        </div>
    );
}