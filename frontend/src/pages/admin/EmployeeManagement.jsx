import { useEffect, useState } from "react";
import axios from "axios";

export default function EmployeeManagement() {

  const [employees, setEmployees] = useState([]);

  const [formData, setFormData] = useState({
    emp_id: "",
    emp_name: "",
    department: "",
    designation: "",
    password: "",
    role: "employee"
  });

  useEffect(() => {

    fetchEmployees();

  }, []);

  const fetchEmployees = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/employees"
      );

      setEmployees(response.data);

    } catch (error) {

      console.log(error);
    }
  };

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const addEmployee = async () => {

    try {

      await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/register",
        formData
      );

      alert("Employee Added");

      fetchEmployees();

      setFormData({
        emp_id: "",
        emp_name: "",
        department: "",
        designation: "",
        password: "",
        role: "employee"
      });

    } catch (error) {

      console.log(error);

      alert("Failed");
    }
  };

  const deleteEmployee = async (id) => {

    try {

      await axios.delete(
        `http://127.0.0.1:8000/api/v1/employees/${id}`
      );

      fetchEmployees();

    } catch (error) {

      console.log(error);
    }
  };

  return (

    <div className="w-full min-h-screen bg-gray-100 p-10">

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-gray-800">

          Employee Management

        </h1>

        <p className="text-gray-500 mt-3 text-lg">

          Manage all employees

        </p>

      </div>

      {/* ADD FORM */}

      <div className="bg-white p-10 rounded-3xl shadow-xl mb-10">

        <h2 className="text-3xl font-bold mb-8">

          Add Employee

        </h2>

        <div className="grid grid-cols-3 gap-6">

          <input
            type="text"
            name="emp_id"
            placeholder="Employee ID"
            value={formData.emp_id}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="text"
            name="emp_name"
            placeholder="Employee Name"
            value={formData.emp_name}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="text"
            name="department"
            placeholder="Department"
            value={formData.department}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="text"
            name="designation"
            placeholder="Designation"
            value={formData.designation}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          />

          <select
            name="role"
            value={formData.role}
            onChange={handleChange}
            className="p-4 rounded-xl border"
          >

            <option value="employee">
              Employee
            </option>

            <option value="admin">
              Admin
            </option>

          </select>

        </div>

        <button
          onClick={addEmployee}
          className="mt-8 bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold text-lg"
        >
          Add Employee
        </button>

      </div>

      {/* EMPLOYEE TABLE */}

      <div className="bg-white rounded-3xl shadow-2xl p-10">

        <h2 className="text-3xl font-bold mb-8">

          Employee List

        </h2>

        <table className="w-full">

          <thead>

            <tr className="bg-gray-100">

              <th className="p-5 text-left">
                Employee ID
              </th>

              <th className="p-5 text-left">
                Name
              </th>

              <th className="p-5 text-left">
                Department
              </th>

              <th className="p-5 text-left">
                Designation
              </th>

              <th className="p-5 text-left">
                Role
              </th>

              <th className="p-5 text-left">
                Action
              </th>

            </tr>

          </thead>

          <tbody>

            {
              employees.map((emp) => (

                <tr
                  key={emp.id}
                  className="border-b hover:bg-gray-50"
                >

                  <td className="p-5">
                    {emp.emp_id}
                  </td>

                  <td className="p-5">
                    {emp.emp_name}
                  </td>

                  <td className="p-5">
                    {emp.department}
                  </td>

                  <td className="p-5">
                    {emp.designation}
                  </td>

                  <td className="p-5">

                    <span className={`px-4 py-2 rounded-full text-white text-sm ${
                      emp.role === "admin"
                        ? "bg-purple-600"
                        : "bg-green-600"
                    }`}>

                      {emp.role}

                    </span>

                  </td>

                  <td className="p-5">

                    <button
                      onClick={() => deleteEmployee(emp.id)}
                      className="bg-red-600 text-white px-5 py-2 rounded-xl"
                    >
                      Delete
                    </button>

                  </td>

                </tr>
              ))
            }

          </tbody>

        </table>

      </div>

    </div>
  );
}