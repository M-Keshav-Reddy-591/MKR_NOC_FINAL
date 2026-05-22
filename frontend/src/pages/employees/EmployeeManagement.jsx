import DashboardLayout from "../../components/layout/DashboardLayout";


export default function EmployeeManagement() {

    return (

        <DashboardLayout>

            <div className="bg-white dark:bg-slate-800 p-10 rounded-2xl shadow">

                <h1 className="text-3xl font-bold">

                    Employee Management
                </h1>

                <p className="mt-4 text-gray-500 dark:text-gray-300">

                    Employee Management Module Working Successfully
                </p>
            </div>
        </DashboardLayout>
    );
}