import {

    useEffect,

    useState

} from "react";

import API from "../../api/axios";

import DashboardLayout from "../../components/layout/DashboardLayout";


export default function ShiftSwapManagement() {

    const [swaps, setSwaps] = useState([]);

    const [formData, setFormData] = useState({

        requester_emp_id: "",

        target_emp_id: "",

        shift_date: ""
    });


    const role = localStorage.getItem(
        "role"
    );


    useEffect(() => {

        fetchSwaps();

    }, []);


    // ======================================
    // FETCH SWAPS
    // ======================================

    const fetchSwaps = async () => {

        try {

            const response = await API.get(
                "/swaps/shift-swaps"
            );

            setSwaps(response.data);
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
    // REQUEST SWAP
    // ======================================

    const requestSwap = async (e) => {

        e.preventDefault();

        try {

            await API.post(
                "/swaps/request-shift-swap",
                formData
            );

            alert(
                "Shift Swap Requested"
            );

            fetchSwaps();

            setFormData({

                requester_emp_id: "",

                target_emp_id: "",

                shift_date: ""
            });
        }

        catch (error) {

            console.log(error);

            alert(
                "Swap Request Failed"
            );
        }
    };


    // ======================================
    // APPROVE SWAP
    // ======================================

    const approveSwap = async (id) => {

        try {

            await API.put(
                `/swaps/approve-shift-swap/${id}`
            );

            alert(
                "Swap Approved"
            );

            fetchSwaps();
        }

        catch (error) {

            console.log(error);
        }
    };


    // ======================================
    // REJECT SWAP
    // ======================================

    const rejectSwap = async (id) => {

        try {

            await API.put(
                `/swaps/reject-shift-swap/${id}`
            );

            alert(
                "Swap Rejected"
            );

            fetchSwaps();
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

                    Shift Swap Management
                </h1>
            </div>


            {/* ========================== */}
            {/* REQUEST FORM */}
            {/* ========================== */}

            <div className="bg-white dark:bg-slate-800 p-6 rounded-2xl shadow mb-8">

                <h2 className="text-2xl font-bold mb-4">

                    Request Shift Swap
                </h2>

                <form
                    onSubmit={requestSwap}
                    className="grid grid-cols-3 gap-4"
                >

                    <input
                        type="text"
                        name="requester_emp_id"
                        placeholder="Requester Employee ID"
                        value={formData.requester_emp_id}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <input
                        type="text"
                        name="target_emp_id"
                        placeholder="Target Employee ID"
                        value={formData.target_emp_id}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <input
                        type="date"
                        name="shift_date"
                        value={formData.shift_date}
                        onChange={handleChange}
                        className="border p-3 rounded-xl"
                    />

                    <button
                        type="submit"
                        className="bg-blue-600 text-white p-3 rounded-xl col-span-3 hover:bg-blue-700"
                    >

                        Request Swap
                    </button>
                </form>
            </div>


            {/* ========================== */}
            {/* SWAP TABLE */}
            {/* ========================== */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow overflow-hidden">

                <table className="w-full">

                    <thead className="bg-slate-900 dark:bg-slate-950 text-white">

                        <tr>

                            <th className="p-4 text-left">

                                Requester
                            </th>

                            <th className="p-4 text-left">

                                Target
                            </th>

                            <th className="p-4 text-left">

                                Shift Date
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

                        {swaps.map(

                            (swap, index) => (

                                <tr
                                    key={index}
                                    className="border-b hover:bg-gray-50"
                                >

                                    <td className="p-4">

                                        {
                                            swap.requester_emp_id
                                        }
                                    </td>

                                    <td className="p-4">

                                        {
                                            swap.target_emp_id
                                        }
                                    </td>

                                    <td className="p-4">

                                        {swap.shift_date}
                                    </td>

                                    <td className="p-4">

                                        <span
                                            className={`px-4 py-2 rounded-full text-sm font-semibold ${getStatusColor(swap.status)}`}
                                        >

                                            {swap.status}
                                        </span>
                                    </td>

                                    {
                                        role === "admin" && (

                                            <td className="p-4 flex gap-2">

                                                <button
                                                    onClick={() =>
                                                        approveSwap(
                                                            swap.id
                                                        )
                                                    }
                                                    className="bg-green-600 text-white px-4 py-2 rounded-lg"
                                                >

                                                    Approve
                                                </button>

                                                <button
                                                    onClick={() =>
                                                        rejectSwap(
                                                            swap.id
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