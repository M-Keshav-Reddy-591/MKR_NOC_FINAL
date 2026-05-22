import {

    useEffect,

    useState

} from "react";

import API from "../../api/axios";

import DashboardLayout from "../../components/layout/DashboardLayout";

import {

    User,

    Shield,

    Lock

} from "lucide-react";

import { useToast } from "../../context/ToastContext";


export default function ProfileManagement() {

    const [profile, setProfile] = useState(null);

    const [passwordData, setPasswordData] = useState({

        old_password: "",

        new_password: ""
    });


    const {

        successToast,

        errorToast

    } = useToast();


    useEffect(() => {

        fetchProfile();

    }, []);


    // ======================================
    // FETCH PROFILE
    // ======================================

    const fetchProfile = async () => {

        try {

            const response = await API.get(
                "/auth/me"
            );

            setProfile(response.data);
        }

        catch (error) {

            console.log(error);

            errorToast(
                "Failed to Load Profile"
            );
        }
    };


    // ======================================
    // HANDLE INPUT
    // ======================================

    const handleChange = (e) => {

        setPasswordData({

            ...passwordData,

            [e.target.name]: e.target.value
        });
    };


    // ======================================
    // CHANGE PASSWORD
    // ======================================

    const changePassword = async (e) => {

        e.preventDefault();

        try {

            await API.put(

                "/auth/change-password",

                passwordData
            );

            successToast(
                "Password Changed Successfully"
            );

            setPasswordData({

                old_password: "",

                new_password: ""
            });
        }

        catch (error) {

            console.log(error);

            errorToast(
                "Password Change Failed"
            );
        }
    };


    return (

        <DashboardLayout>

            {/* ========================== */}
            {/* PAGE HEADER */}
            {/* ========================== */}

            <div className="mb-8">

                <h1 className="text-3xl font-bold dark:text-white">

                    Profile Management
                </h1>

                <p className="text-gray-500 dark:text-gray-300 mt-2">

                    Manage your account and security settings
                </p>
            </div>


            {/* ========================== */}
            {/* PROFILE GRID */}
            {/* ========================== */}

            <div className="grid grid-cols-3 gap-6">


                {/* ====================== */}
                {/* PROFILE CARD */}
                {/* ====================== */}

                <div className="bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex flex-col items-center">

                        <div className="w-28 h-28 bg-blue-600 rounded-full flex items-center justify-center text-white mb-4">

                            <User size={50} />
                        </div>

                        <h2 className="text-2xl font-bold dark:text-white">

                            {profile?.name}
                        </h2>

                        <p className="text-gray-500 dark:text-gray-300">

                            {profile?.role}
                        </p>
                    </div>


                    <div className="mt-8 space-y-4">

                        <div>

                            <p className="text-sm text-gray-500 dark:text-gray-300">

                                Employee ID
                            </p>

                            <h3 className="font-semibold dark:text-white">

                                {profile?.emp_id}
                            </h3>
                        </div>

                        <div>

                            <p className="text-sm text-gray-500 dark:text-gray-300">

                                Department
                            </p>

                            <h3 className="font-semibold dark:text-white">

                                {profile?.department}
                            </h3>
                        </div>

                        <div>

                            <p className="text-sm text-gray-500 dark:text-gray-300">

                                Role
                            </p>

                            <h3 className="font-semibold dark:text-white">

                                {profile?.role}
                            </h3>
                        </div>
                    </div>
                </div>


                {/* ====================== */}
                {/* SECURITY CARD */}
                {/* ====================== */}

                <div className="col-span-2 bg-white dark:bg-slate-800 rounded-2xl shadow p-6">

                    <div className="flex items-center gap-3 mb-6">

                        <Shield
                            className="text-blue-600"
                            size={30}
                        />

                        <h2 className="text-2xl font-bold dark:text-white">

                            Security Settings
                        </h2>
                    </div>


                    <form
                        onSubmit={changePassword}
                        className="space-y-5"
                    >

                        <div>

                            <label className="block mb-2 font-medium dark:text-white">

                                Current Password
                            </label>

                            <input
                                type="password"
                                name="old_password"
                                value={passwordData.old_password}
                                onChange={handleChange}
                                className="w-full border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                            />
                        </div>


                        <div>

                            <label className="block mb-2 font-medium dark:text-white">

                                New Password
                            </label>

                            <input
                                type="password"
                                name="new_password"
                                value={passwordData.new_password}
                                onChange={handleChange}
                                className="w-full border p-4 rounded-xl dark:bg-slate-700 dark:text-white"
                            />
                        </div>


                        <button
                            type="submit"
                            className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700 transition flex items-center gap-2"
                        >

                            <Lock size={18} />

                            Change Password
                        </button>
                    </form>
                </div>
            </div>
        </DashboardLayout>
    );
}