import {

    useEffect,

    useState

} from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import API from "../../api/axios";


export default function ShiftAllocation() {

    // ======================================
    // STATES
    // ======================================

    const [employees, setEmployees] = useState([]);

    const [shifts, setShifts] = useState([]);

    const [loading, setLoading] = useState(true);

    const [formData, setFormData] = useState({

        employee_id: "",

        shift_id: "",

        shift_date: ""
    });


    // ======================================
    // FETCH DATA
    // ======================================

    useEffect(() => {

        fetchData();

    }, []);


    const fetchData = async () => {

        try {

            // ==============================
            // EMPLOYEES
            // ==============================

            const employeeResponse = await API.get(
                "/employees/all"
            );


            // ==============================
            // SHIFTS
            // ==============================

            const shiftResponse = await API.get(
                "/shifts/all"
            );


            console.log(
                employeeResponse.data
            );

            console.log(
                shiftResponse.data
            );


            setEmployees(
                employeeResponse.data || []
            );

            setShifts(
                shiftResponse.data || []
            );
        }

        catch (error) {

            console.log(
                "FETCH ERROR",
                error
            );
        }

        finally {

            setLoading(false);
        }
    };


    // ======================================
    // HANDLE CHANGE
    // ======================================

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value
        });
    };


    // ======================================
    // ASSIGN SHIFT
    // ======================================

    const assignShift = async (e) => {

        e.preventDefault();

        try {

            await API.post(

                "/shift-assignment/assign-shift",

                formData
            );


            alert(
                "Shift Assigned Successfully"
            );


            setFormData({

                employee_id: "",

                shift_id: "",

                shift_date: ""
            });
        }

        catch (error) {

            console.log(error);

            alert(
                "Failed To Assign Shift"
            );
        }
    };


    // ======================================
    // LOADING
    // ======================================

    if (loading) {

        return (

            <DashboardLayout>

                <div className="text-2xl dark:text-white">

                    Loading Shift Allocation...
                </div>

            </DashboardLayout>
        );
    }


    // ======================================
    // UI
    // ======================================

    return (

        <DashboardLayout>

            <div className="mb-8">

                <h1 className="text-4xl font-bold dark:text-white">

                    Shift Allocation
                </h1>

                <p className="text-gray-500 dark:text-gray-300 mt-2">

                    Allocate shifts to employees
                </p>
            </div>


            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Assign Shift
                </h2>


                <form
                    onSubmit={assignShift}
                    className="grid grid-cols-1 md:grid-cols-3 gap-5"
                >

                    {/* EMPLOYEE */}

                    <select
                        name="employee_id"
                        value={formData.employee_id}
                        onChange={handleChange}
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                        required
                    >

                        <option value="">

                            Select Employee
                        </option>


                        {employees.map((employee) => (

                            <option
                                key={employee.id}
                                value={employee.id}
                            >

                                {employee.name}
                            </option>
                        ))}
                    </select>


                    {/* SHIFT */}

                    <select
                        name="shift_id"
                        value={formData.shift_id}
                        onChange={handleChange}
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                        required
                    >

                        <option value="">

                            Select Shift
                        </option>


                        {shifts.map((shift) => (

                            <option
                                key={shift.id}
                                value={shift.id}
                            >

                                {shift.shift_name}
                            </option>
                        ))}
                    </select>


                    {/* DATE */}

                    <input
                        type="date"
                        name="shift_date"
                        value={formData.shift_date}
                        onChange={handleChange}
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                        required
                    />


                    {/* BUTTON */}

                    <button
                        type="submit"
                        className="bg-blue-600 hover:bg-blue-700 text-white p-4 rounded-xl font-semibold md:col-span-3"
                    >

                        Assign Shift
                    </button>
                </form>
            </div>
        </DashboardLayout>
    );
}