import {

    useEffect,

    useState

} from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import API from "../../api/axios";


export default function AttendanceManagement() {

    const [attendance, setAttendance] = useState([]);

    const [loading, setLoading] = useState(false);


    // ======================================
    // FETCH ATTENDANCE
    // ======================================

    const fetchAttendance = async () => {

        try {

            const response = await API.get(
                "/attendance/my-attendance"
            );


            setAttendance(
                response.data || []
            );
        }

        catch (error) {

            console.log(error);
        }
    };


    useEffect(() => {

        fetchAttendance();

    }, []);


    // ======================================
    // MARK ATTENDANCE
    // ======================================

    const markAttendance = async () => {

        try {

            setLoading(true);


            // ==============================
            // EMPLOYEE ID
            // ==============================

            const emp_id = localStorage.getItem(
                "emp_id"
            );


            // ==============================
            // API
            // ==============================

            await API.post(

                "/attendance/mark-attendance",

                {

                    emp_id: emp_id
                }
            );


            alert(
                "Attendance Marked Successfully"
            );


            fetchAttendance();
        }

        catch (error) {

            console.log(error);

            alert(
                error?.response?.data?.detail
                ||

                "Failed To Mark Attendance"
            );
        }

        finally {

            setLoading(false);
        }
    };


    return (

        <DashboardLayout>

            {/* ================================= */}
            {/* PAGE HEADER */}
            {/* ================================= */}

            <div className="mb-8">

                <h1 className="text-4xl font-bold dark:text-white">

                    Attendance Management
                </h1>

                <p className="text-gray-500 dark:text-gray-300 mt-2">

                    Mark and view your attendance
                </p>
            </div>


            {/* ================================= */}
            {/* BUTTON */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6 mb-8">

                <button
                    onClick={markAttendance}
                    disabled={loading}
                    className="bg-green-600 hover:bg-green-700 text-white px-8 py-4 rounded-xl font-semibold"
                >

                    {
                        loading

                        ?

                        "Marking..."

                        :

                        "Mark Attendance"
                    }
                </button>
            </div>


            {/* ================================= */}
            {/* ATTENDANCE TABLE */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Attendance History
                </h2>


                <table className="w-full">

                    <thead className="bg-slate-900 text-white">

                        <tr>

                            <th className="p-4 text-left">
                                Date
                            </th>

                            <th className="p-4 text-left">
                                Login Time
                            </th>

                            <th className="p-4 text-left">
                                Status
                            </th>
                        </tr>
                    </thead>


                    <tbody>

                        {attendance.map((item, index) => (

                            <tr
                                key={index}
                                className="border-b dark:border-slate-700"
                            >

                                <td className="p-4 dark:text-white">

                                    {item.date}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {item.login_time}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {item.status}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </DashboardLayout>
    );
}