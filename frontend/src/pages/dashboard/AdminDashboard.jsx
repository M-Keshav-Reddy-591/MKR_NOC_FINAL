import {

    useEffect,

    useState

} from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import API from "../../api/axios";

import {

    Users,

    Clock3,

    CalendarDays,

    Repeat

} from "lucide-react";

import Loader from "../../components/common/Loader";


export default function AdminDashboard() {

    const [stats, setStats] = useState(null);

    const [loading, setLoading] = useState(true);


    // ======================================
    // FETCH DASHBOARD STATS
    // ======================================

    const fetchDashboardStats = async () => {

        try {

            const response = await API.get(
                "/dashboard/stats"
            );

            setStats(response.data);

            setLoading(false);
        }

        catch (error) {

            console.log(error);

            setLoading(false);
        }
    };


    // ======================================
    // AUTO REFRESH
    // ======================================

    useEffect(() => {

        fetchDashboardStats();

        const interval = setInterval(() => {

            fetchDashboardStats();

        }, 10000);

        return () => clearInterval(interval);

    }, []);


    if (loading) {

        return (

            <DashboardLayout>

                <Loader />

            </DashboardLayout>
        );
    }


    return (

        <DashboardLayout>

            {/* ========================== */}
            {/* PAGE HEADER */}
            {/* ========================== */}

            <div className="mb-8">

                <h1 className="text-4xl font-bold dark:text-white">

                    Admin Dashboard
                </h1>

                <p className="text-gray-500 dark:text-gray-300 mt-2">

                    Real-time workforce monitoring system
                </p>
            </div>


            {/* ========================== */}
            {/* KPI CARDS */}
            {/* ========================== */}

            <div className="grid grid-cols-4 gap-6">

                {/* EMPLOYEES */}

                <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex items-center justify-between">

                        <div>

                            <p className="text-gray-500 dark:text-gray-300">

                                Employees
                            </p>

                            <h2 className="text-4xl font-bold mt-2 dark:text-white">

                                {stats?.employees}
                            </h2>
                        </div>

                        <Users
                            size={40}
                            className="text-blue-600"
                        />
                    </div>
                </div>


                {/* ATTENDANCE */}

                <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex items-center justify-between">

                        <div>

                            <p className="text-gray-500 dark:text-gray-300">

                                Attendance
                            </p>

                            <h2 className="text-4xl font-bold mt-2 dark:text-white">

                                {stats?.attendance}
                            </h2>
                        </div>

                        <Clock3
                            size={40}
                            className="text-green-600"
                        />
                    </div>
                </div>


                {/* LEAVES */}

                <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex items-center justify-between">

                        <div>

                            <p className="text-gray-500 dark:text-gray-300">

                                Leaves
                            </p>

                            <h2 className="text-4xl font-bold mt-2 dark:text-white">

                                {stats?.leaves}
                            </h2>
                        </div>

                        <CalendarDays
                            size={40}
                            className="text-yellow-600"
                        />
                    </div>
                </div>


                {/* SHIFT SWAPS */}

                <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex items-center justify-between">

                        <div>

                            <p className="text-gray-500 dark:text-gray-300">

                                Shift Swaps
                            </p>

                            <h2 className="text-4xl font-bold mt-2 dark:text-white">

                                {stats?.swaps}
                            </h2>
                        </div>

                        <Repeat
                            size={40}
                            className="text-purple-600"
                        />
                    </div>
                </div>
            </div>


            {/* ========================== */}
            {/* LIVE STATUS */}
            {/* ========================== */}

            <div className="mt-10 bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                <div className="flex items-center justify-between">

                    <div>

                        <h2 className="text-2xl font-bold dark:text-white">

                            Live Monitoring
                        </h2>

                        <p className="text-gray-500 dark:text-gray-300 mt-2">

                            Dashboard auto refreshes every 10 seconds
                        </p>
                    </div>

                    <div className="flex items-center gap-3">

                        <div className="w-4 h-4 rounded-full bg-green-500 animate-pulse"></div>

                        <span className="font-semibold text-green-600">

                            LIVE
                        </span>
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
}