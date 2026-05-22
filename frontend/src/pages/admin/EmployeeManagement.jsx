import {

    useEffect,

    useState

} from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";

import API from "../../api/axios";

import { useToast } from "../../context/ToastContext";


export default function EmployeeManagement() {

    const [employees, setEmployees] = useState([]);

    const [formData, setFormData] = useState({

        emp_id: "",

        name: "",

        department: "",

        role: "employee",

        password: ""
    });


    const {

        successToast,

        errorToast

    } = useToast();


    // ======================================
    // FETCH EMPLOYEES
    // ======================================

    const fetchEmployees = async () => {

        try {

            const response = await API.get(
                "/employees/all"
            );

            setEmployees(response.data);
        }

        catch (error) {

            console.log(error);
        }
    };


    useEffect(() => {

        fetchEmployees();

    }, []);


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
    // ADD EMPLOYEE
    // ======================================

    const addEmployee = async (e) => {

        e.preventDefault();

        try {

            await API.post(

                "/auth/register",

                formData
            );


            successToast(
                "Employee Added Successfully"
            );


            fetchEmployees();


            setFormData({

                emp_id: "",

                name: "",

                department: "",

                role: "employee",

                password: ""
            });
        }

        catch (error) {

            console.log(error);

            errorToast(
                "Failed To Add Employee"
            );
        }
    };


    return (

        <DashboardLayout>

            {/* ================================= */}
            {/* PAGE HEADER */}
            {/* ================================= */}

            <div className="mb-8">

                <h1 className="text-4xl font-bold dark:text-white">

                    Employee Management
                </h1>

                <p className="text-gray-500 dark:text-gray-300 mt-2">

                    Manage workforce and employee accounts
                </p>
            </div>


            {/* ================================= */}
            {/* ADD EMPLOYEE FORM */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6 mb-10">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Add Employee
                </h2>


                <form
                    onSubmit={addEmployee}
                    className="grid grid-cols-2 gap-5"
                >

                    <input
                        type="text"
                        name="emp_id"
                        value={formData.emp_id}
                        onChange={handleChange}
                        placeholder="Employee ID"
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                    />


                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        placeholder="Employee Name"
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                    />


                    <input
                        type="text"
                        name="department"
                        value={formData.department}
                        onChange={handleChange}
                        placeholder="Department"
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                    />


                    <select
                        name="role"
                        value={formData.role}
                        onChange={handleChange}
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                    >

                        <option value="employee">

                            Employee
                        </option>

                        <option value="admin">

                            Admin
                        </option>
                    </select>


                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="Password"
                        className="border p-4 rounded-xl dark:bg-slate-700 dark:text-white col-span-2"
                    />


                    <button
                        type="submit"
                        className="bg-blue-600 hover:bg-blue-700 text-white p-4 rounded-xl font-semibold col-span-2"
                    >

                        Add Employee
                    </button>
                </form>
            </div>


            {/* ================================= */}
            {/* EMPLOYEE TABLE */}
            {/* ================================= */}

            <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                <h2 className="text-2xl font-bold mb-6 dark:text-white">

                    Employee List
                </h2>


                <table className="w-full">

                    <thead className="bg-slate-900 text-white">

                        <tr>

                            <th className="p-4 text-left">
                                Employee ID
                            </th>

                            <th className="p-4 text-left">
                                Name
                            </th>

                            <th className="p-4 text-left">
                                Department
                            </th>

                            <th className="p-4 text-left">
                                Role
                            </th>
                        </tr>
                    </thead>


                    <tbody>

                        {employees.map((employee) => (

                            <tr
                                key={employee.id}
                                className="border-b dark:border-slate-700"
                            >

                                <td className="p-4 dark:text-white">

                                    {employee.emp_id}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {employee.name}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {employee.department}
                                </td>

                                <td className="p-4 dark:text-white">

                                    {employee.role}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </DashboardLayout>
    );
}