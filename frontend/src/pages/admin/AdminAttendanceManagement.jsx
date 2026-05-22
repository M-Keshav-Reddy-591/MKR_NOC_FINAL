import { useEffect, useState } from "react";
import axios from "axios";

export default function AdminAttendanceManagement() {

    const [employees, setEmployees] = useState([]);

    const [attendance, setAttendance] = useState([]);

    const [search, setSearch] = useState("");

    const [form, setForm] = useState({

        emp_id: "",

        status: "Present",

        login_time: "09:00",

        logout_time: "18:00",

        ot_hours: 0,

        remarks: ""
    });


    const token = localStorage.getItem("token");


    useEffect(() => {

        fetchEmployees();

        fetchAttendance();

    }, []);


    const fetchEmployees = async () => {

        const res = await axios.get(

            "http://127.0.0.1:8000/api/v1/employees/all",

            {

                headers: {

                    Authorization: `Bearer ${token}`
                }
            }
        );

        setEmployees(res.data);
    };


    const fetchAttendance = async () => {

        const res = await axios.get(

            "http://127.0.0.1:8000/api/v1/attendance/today-attendance",

            {

                headers: {

                    Authorization: `Bearer ${token}`
                }
            }
        );

        setAttendance(res.data);
    };


    const handleSubmit = async (e) => {

        e.preventDefault();

        await axios.post(

            "http://127.0.0.1:8000/api/v1/attendance/admin-mark-attendance",

            form,

            {

                headers: {

                    Authorization: `Bearer ${token}`
                }
            }
        );

        alert("Attendance Marked");

        fetchAttendance();
    };


    const filteredEmployees = employees.filter((emp) =>

        emp.full_name
            ?.toLowerCase()
            .includes(search.toLowerCase())
    );


    return (

        <div className="p-6 text-white">

            <h1 className="text-4xl font-bold mb-6">

                Smart Attendance Management
            </h1>


            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

                <div className="bg-gray-900 p-6 rounded-2xl">

                    <input

                        type="text"

                        placeholder="Search Employee"

                        value={search}

                        onChange={(e) =>
                            setSearch(e.target.value)
                        }

                        className="w-full p-3 rounded-lg bg-gray-800 mb-4"
                    />


                    <div className="max-h-72 overflow-y-auto">

                        {

                            filteredEmployees.map((emp) => (

                                <div

                                    key={emp.id}

                                    onClick={() =>

                                        setForm({

                                            ...form,

                                            emp_id: emp.emp_id
                                        })
                                    }

                                    className="bg-gray-800 p-3 rounded-lg mb-2 cursor-pointer hover:bg-blue-600"
                                >

                                    {emp.full_name}

                                    <div className="text-sm text-gray-300">

                                        {emp.emp_id}
                                    </div>

                                </div>
                            ))
                        }

                    </div>
                </div>


                <div className="bg-gray-900 p-6 rounded-2xl">

                    <form onSubmit={handleSubmit}>

                        <div className="mb-4">

                            <label>Employee ID</label>

                            <input

                                type="text"

                                value={form.emp_id}

                                readOnly

                                className="w-full p-3 rounded-lg bg-gray-800"
                            />

                        </div>


                        <div className="mb-4">

                            <label>Status</label>

                            <select

                                value={form.status}

                                onChange={(e) =>

                                    setForm({

                                        ...form,

                                        status: e.target.value
                                    })
                                }

                                className="w-full p-3 rounded-lg bg-gray-800"
                            >

                                <option>Present</option>

                                <option>Absent</option>

                                <option>Late</option>

                                <option>Half Day</option>

                                <option>On Leave</option>

                                <option>OT</option>

                            </select>

                        </div>


                        <div className="grid grid-cols-2 gap-4">

                            <div>

                                <label>Login Time</label>

                                <input

                                    type="time"

                                    value={form.login_time}

                                    onChange={(e) =>

                                        setForm({

                                            ...form,

                                            login_time: e.target.value
                                        })
                                    }

                                    className="w-full p-3 rounded-lg bg-gray-800"
                                />

                            </div>


                            <div>

                                <label>Logout Time</label>

                                <input

                                    type="time"

                                    value={form.logout_time}

                                    onChange={(e) =>

                                        setForm({

                                            ...form,

                                            logout_time: e.target.value
                                        })
                                    }

                                    className="w-full p-3 rounded-lg bg-gray-800"
                                />

                            </div>

                        </div>


                        <div className="mt-4">

                            <label>OT Hours</label>

                            <input

                                type="number"

                                value={form.ot_hours}

                                onChange={(e) =>

                                    setForm({

                                        ...form,

                                        ot_hours: e.target.value
                                    })
                                }

                                className="w-full p-3 rounded-lg bg-gray-800"
                            />

                        </div>


                        <div className="mt-4">

                            <label>Remarks</label>

                            <textarea

                                value={form.remarks}

                                onChange={(e) =>

                                    setForm({

                                        ...form,

                                        remarks: e.target.value
                                    })
                                }

                                className="w-full p-3 rounded-lg bg-gray-800"
                            />

                        </div>


                        <button

                            className="mt-6 bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-xl w-full"
                        >

                            Save Attendance

                        </button>

                    </form>

                </div>

            </div>


            <div className="mt-10 bg-gray-900 p-6 rounded-2xl">

                <h2 className="text-2xl font-bold mb-4">

                    Today's Attendance
                </h2>


                <div className="overflow-x-auto">

                    <table className="w-full">

                        <thead>

                            <tr className="text-left border-b border-gray-700">

                                <th className="p-3">Employee</th>

                                <th className="p-3">Status</th>

                                <th className="p-3">Login</th>

                                <th className="p-3">Logout</th>

                                <th className="p-3">OT</th>

                                <th className="p-3">Remarks</th>

                            </tr>

                        </thead>


                        <tbody>

                            {

                                attendance.map((item, index) => (

                                    <tr

                                        key={index}

                                        className="border-b border-gray-800"
                                    >

                                        <td className="p-3">

                                            {item.employee_name}
                                        </td>

                                        <td className="p-3">

                                            {item.status}
                                        </td>

                                        <td className="p-3">

                                            {item.login_time}
                                        </td>

                                        <td className="p-3">

                                            {item.logout_time}
                                        </td>

                                        <td className="p-3">

                                            {item.ot_hours}
                                        </td>

                                        <td className="p-3">

                                            {item.remarks}
                                        </td>

                                    </tr>
                                ))
                            }

                        </tbody>

                    </table>

                </div>

            </div>

        </div>
    );
}