import {

    useEffect,

    useState

} from "react";

import API from "../../api/axios";

import DashboardLayout from "../../components/layout/DashboardLayout";


export default function LeaveManagement() {

    const [leaves, setLeaves] = useState([]);

    const [formData, setFormData] = useState({

        emp_id: "",

        from_date: "",

        to_date: "",

        reason: ""
    });


    const role = localStorage.getItem(
        "role"
    );


    useEffect(() => {

        fetchLeaves();

    }, []);


    // ======================================
    // FETCH LEAVES
    // ======================================

    const fetchLeaves = async () => {

        try {

            const response = await API.get(
                "/leaves/all-leaves"
            );

            setLeaves(response.data);
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // HANDLE INPUT
    // ======================================

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value
        });
    };


    // ======================================
    // APPLY LEAVE
    // ======================================

    const applyLeave = async (e) => {

        e.preventDefault();

        try {

            await API.post(
                "/leaves/apply-leave",
                formData
            );

            alert(
                "Leave Applied Successfully"
            );

            fetchLeaves();

            setFormData({

                emp_id: "",

                from_date: "",

                to_date: "",

                reason: ""
            });
        }

        catch (error) {

            console.log(error);

            alert(
                "Leave Request Failed"
            );
        }
    };


    // ======================================
    // APPROVE LEAVE
    // ======================================

    const approveLeave = async (id) => {

        try {

            await API.put(
                `/leaves/approve-leave/${id}`
            );

            alert(
                "Leave Approved"
            );

            fetchLeaves();
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // REJECT LEAVE
    // ======================================

    const rejectLeave = async (id) => {

        try {

            await API.put(
                `/leaves/reject-leave/${id}`
            );

            alert(
                "Leave Rejected"
            );

            fetchLeaves();
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // STATUS COLORS
    // ======================================

    const getStatusColor = (status) => {

        if (status === "Approved") {

            return "bg-green-100 text-green-700";
        }

        if (status === "Rejected") {

            return "bg-red-100 text-red-700";
        }

        return "bg-yellow-100 text-yellow-700";
    };


    return (

        <DashboardLayout>

            {/* ========================== */}
            {/* HEADER */}
            {/* ========================== */}

            <div className="flex justify-between items-center mb-6">

                <h1 className="text-3xl font-bold">

                    Leave Management
                </h1>
            </div>


            {/* ========================== */}
            {/* APPLY LEAVE FORM */}
            {/* ========================== */}

            <div className="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow mb-8">

                <h2 className="text-2xl font-bold mb-4">

                    Apply Leave
                </h2>

                <form
                    onSubmit={applyLeave}
                    className="grid grid-cols-4 gap-4"
                >

                    <input
                        type="text"
                        name="emp_id"
                        placeholder="Employee ID"
                        value={formData.emp_id}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <input
                        type="date"
                        name="from_date"
                        value={formData.from_date}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <input
                        type="date"
                        name="to_date"
                        value={formData.to_date}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <input
                        type="text"
                        name="reason"
                        placeholder="Reason"
                        value={formData.reason}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <button
                        type="submit"
                        className="bg-blue-600 text-white p-3 rounded-xl col-span-4 hover:bg-blue-700"
                    >

                        Apply Leave
                    </button>
                </form>
            </div>


            {/* ========================== */}
            {/* LEAVE TABLE */}
            {/* ========================== */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow overflow-hidden">

                <table className="w-full">

                    <thead className="bg-slate-900 dark:bg-slate-950 text-white">

                        <tr>

                            <th className="p-4 text-left">

                                Employee ID
                            </th>

                            <th className="p-4 text-left">

                                From
                            </th>

                            <th className="p-4 text-left">

                                To
                            </th>

                            <th className="p-4 text-left">

                                Reason
                            </th>

                            <th className="p-4 text-left">

                                Status
                            </th>

                            {
                                role === "admin" && (

                                    <th className="p-4 text-left">

                                        Action
                                    </th>
                                )
                            }
                        </tr>
                    </thead>

                    <tbody>

                        {leaves.map(

                            (leave, index) => (

                                <tr
                                    key={index}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-4">

                                        {leave.emp_id}
                                    </td>

                                    <td className="p-4">

                                        {leave.from_date}
                                    </td>

                                    <td className="p-4">

                                        {leave.to_date}
                                    </td>

                                    <td className="p-4">

                                        {leave.reason}
                                    </td>

                                    <td className="p-4">

                                        <span
                                            className={`px-4 py-2 rounded-full text-sm font-semibold ${getStatusColor(leave.status)}`}
                                        >

                                            {leave.status}
                                        </span>
                                    </td>

                                    {
                                        role === "admin" && (

                                            <td className="p-4 flex gap-2">

                                                <button
                                                    onClick={() =>
                                                        approveLeave(
                                                            leave.id
                                                        )
                                                    }
                                                    className="bg-green-600 text-white px-4 py-2 rounded-lg"
                                                >

                                                    Approve
                                                </button>

                                                <button
                                                    onClick={() =>
                                                        rejectLeave(
                                                            leave.id
                                                        )
                                                    }
                                                    className="bg-red-600 text-white px-4 py-2 rounded-lg"
                                                >

                                                    Reject
                                                </button>
                                            </td>
                                        )
                                    }
                                </tr>
                            )
                        )}
                    </tbody>
                </table>
            </div>
        </DashboardLayout>
    );
}