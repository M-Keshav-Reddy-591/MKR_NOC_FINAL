import {

    useEffect,

    useState

} from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import API from "../../api/axios";


export default function EmployeeDashboard() {

    const [attendance, setAttendance] = useState([]);

    const [schedule, setSchedule] = useState([]);


    useEffect(() => {

        fetchAttendance();

        fetchSchedule();

    }, []);


    // ======================================
    // ATTENDANCE
    // ======================================

    const fetchAttendance = async () => {

        try {

            const response = await API.get(
                "/attendance/my-attendance"
            );

            setAttendance(response.data);
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // SCHEDULE
    // ======================================

    const fetchSchedule = async () => {

        try {

            const response = await API.get(
                "/shift-assignment/my-schedule"
            );

            setSchedule(response.data);
        }

        catch (error) {

            console.log(error);
        }
    };


    return (

        <DashboardLayout>

            <h1 className="text-4xl font-bold mb-8 dark:text-white">

                Employee Dashboard
            </h1>


            {/* ================================= */}
            {/* ATTENDANCE HISTORY */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6 mb-8">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Previous Attendance
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


            {/* ================================= */}
            {/* UPCOMING SHIFTS */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Upcoming Schedule
                </h2>


                <table className="w-full">

                    <thead className="bg-slate-900 text-white">

                        <tr>

                            <th className="p-4 text-left">
                                Date
                            </th>

                            <th className="p-4 text-left">
                                Shift
                            </th>

                            <th className="p-4 text-left">
                                Start
                            </th>

                            <th className="p-4 text-left">
                                End
                            </th>
                        </tr>
                    </thead>

                    <tbody>

                        {schedule.map((item, index) => (

                            <tr
                                key={index}
                                className="border-b dark:border-slate-700"
                            >

                                <td className="p-4 dark:text-white">

                                    {item.date}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {item.shift}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {item.start_time}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {item.end_time}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </DashboardLayout>
    );
}