import { useState } from "react";

import { useNavigate } from "react-router-dom";

import API from "../../api/axios";


export default function Login() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({

        username: "",

        password: ""
    });


    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value
        });
    };


    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await API.post(

                "/auth/login",

                new URLSearchParams({

                    username: formData.username,

                    password: formData.password
                }),

                {

                    headers: {

                        "Content-Type":
                        "application/x-www-form-urlencoded"
                    }
                }
            );

            // ======================================
            // STORE JWT
            // ======================================

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            localStorage.setItem(
                "role",
                response.data.role
            );

            // ======================================
            // SMART ROLE REDIRECT
            // ======================================

            if (response.data.role === "admin") {

                navigate("/admin-dashboard");
            }

            else {

                navigate("/employee-dashboard");
            }
        }

        catch (error) {

            console.log(error);

            alert("Invalid Credentials");
        }
    };


    return (

        <div className="flex items-center justify-center h-screen bg-gray-100">

            <div className="bg-white dark:bg-slate-800 p-8 rounded-2xl shadow-xl w-96">

                <h1 className="text-3xl font-bold text-center mb-6">

                    NOC Attendance System
                </h1>

                <form onSubmit={handleLogin}>

                    <input
                        type="text"
                        name="username"
                        placeholder="Employee ID"
                        className="w-full p-3 border rounded-lg mb-4"
                        onChange={handleChange}
                    />

                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        className="w-full p-3 border rounded-lg mb-4"
                        onChange={handleChange}
                    />

                    <button
                        type="submit"
                        className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700"
                    >

                        Login
                    </button>
                </form>
            </div>
        </div>
    );
}