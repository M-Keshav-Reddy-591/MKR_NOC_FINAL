import {

    useEffect,

    useState

} from "react";

import API from "../../api/axios";

import DashboardLayout from "../../components/layout/DashboardLayout";

import {

    FileSpreadsheet,

    FileDown,

    Download

} from "lucide-react";


export default function ReportsManagement() {

    const [reports, setReports] = useState([]);


    useEffect(() => {

        fetchReports();

    }, []);


    // ======================================
    // FETCH REPORTS
    // ======================================

    const fetchReports = async () => {

        try {

            const response = await API.get(
                "/dashboard/attendance-report"
            );

            setReports(response.data);
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // EXPORT CSV
    // ======================================

    const exportCSV = async () => {

        try {

            const response = await API.get(

                "/exports/export-csv",

                {

                    responseType: "blob"
                }
            );

            const url = window.URL.createObjectURL(

                new Blob([response.data])
            );

            const link = document.createElement("a");

            link.href = url;

            link.setAttribute(

                "download",

                "attendance_report.csv"
            );

            document.body.appendChild(link);

            link.click();
        }

        catch (error) {

            console.log(error);

            alert("CSV Export Failed");
        }
    };


    // ======================================
    // EXPORT EXCEL
    // ======================================

    const exportExcel = async () => {

        try {

            const response = await API.get(

                "/exports/export-excel",

                {

                    responseType: "blob"
                }
            );

            const url = window.URL.createObjectURL(

                new Blob([response.data])
            );

            const link = document.createElement("a");

            link.href = url;

            link.setAttribute(

                "download",

                "attendance_report.xlsx"
            );

            document.body.appendChild(link);

            link.click();
        }

        catch (error) {

            console.log(error);

            alert("Excel Export Failed");
        }
    };


    return (

        <DashboardLayout>

            {/* ========================== */}
            {/* HEADER */}
            {/* ========================== */}

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-3xl font-bold">

                    Reports & Export Center
                </h1>
            </div>


            {/* ========================== */}
            {/* EXPORT CARDS */}
            {/* ========================== */}

            <div className="grid grid-cols-3 gap-6 mb-8">

                {/* CSV */}

                <div className="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow">

                    <div className="flex items-center gap-4 mb-4">

                        <FileDown
                            size={40}
                            className="text-green-600"
                        />

                        <div>

                            <h2 className="text-xl font-bold">

                                CSV Export
                            </h2>

                            <p className="text-gray-500 dark:text-gray-300">

                                Download attendance CSV report
                            </p>
                        </div>
                    </div>

                    <button
                        onClick={exportCSV}
                        className="bg-green-600 text-white px-6 py-3 rounded-xl w-full hover:bg-green-700"
                    >

                        Export CSV
                    </button>
                </div>


                {/* EXCEL */}

                <div className="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow">

                    <div className="flex items-center gap-4 mb-4">

                        <FileSpreadsheet
                            size={40}
                            className="text-blue-600"
                        />

                        <div>

                            <h2 className="text-xl font-bold">

                                Excel Export
                            </h2>

                            <p className="text-gray-500 dark:text-gray-300">

                                Download attendance Excel report
                            </p>
                        </div>
                    </div>

                    <button
                        onClick={exportExcel}
                        className="bg-blue-600 text-white px-6 py-3 rounded-xl w-full hover:bg-blue-700"
                    >

                        Export Excel
                    </button>
                </div>


                {/* DOWNLOAD CENTER */}

                <div className="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow">

                    <div className="flex items-center gap-4 mb-4">

                        <Download
                            size={40}
                            className="text-purple-600"
                        />

                        <div>

                            <h2 className="text-xl font-bold">

                                Download Center
                            </h2>

                            <p className="text-gray-500 dark:text-gray-300">

                                Centralized reporting system
                            </p>
                        </div>
                    </div>

                    <button
                        className="bg-purple-600 text-white px-6 py-3 rounded-xl w-full hover:bg-purple-700"
                    >

                        Open Center
                    </button>
                </div>
            </div>


            {/* ========================== */}
            {/* REPORT TABLE */}
            {/* ========================== */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow overflow-hidden">

                <table className="w-full">

                    <thead className="bg-slate-900 dark:bg-slate-950 text-white">

                        <tr>

                            <th className="p-4 text-left">

                                Employee ID
                            </th>

                            <th className="p-4 text-left">

                                Shift Date
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

                        {reports.map(

                            (report, index) => (

                                <tr
                                    key={index}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-4">

                                        {
                                            report.employee_id
                                        }
                                    </td>

                                    <td className="p-4">

                                        {report.date}
                                    </td>

                                    <td className="p-4">

                                        {
                                            report.login_time
                                        }
                                    </td>

                                    <td className="p-4">

                                        <span
                                            className={`px-4 py-2 rounded-full text-sm font-semibold ${
                                                report.status === "Present"

                                                ?

                                                "bg-green-100 text-green-700"

                                                :

                                                report.status === "Late"

                                                ?

                                                "bg-yellow-100 text-yellow-700"

                                                :

                                                report.status === "Absent"

                                                ?

                                                "bg-red-100 text-red-700"

                                                :

                                                "bg-gray-100 text-gray-700"
                                            }`}
                                        >

                                            {report.status}
                                        </span>
                                    </td>
                                </tr>
                            )
                        )}
                    </tbody>
                </table>
            </div>
        </DashboardLayout>
    );
}