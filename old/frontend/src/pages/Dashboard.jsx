import AdminLayout from "../layouts/AdminLayout";

export default function Dashboard() {

  return (

    <AdminLayout>

      <div>

        <h1 className="text-4xl font-bold mb-10">

          Dashboard Overview

        </h1>

        <div className="grid grid-cols-4 gap-6">

          <div className="bg-blue-500 text-white p-8 rounded-3xl shadow-xl">

            <h2 className="text-2xl font-bold">

              Employees

            </h2>

            <p className="text-5xl mt-4 font-bold">

              24

            </p>

          </div>

          <div className="bg-green-500 text-white p-8 rounded-3xl shadow-xl">

            <h2 className="text-2xl font-bold">

              Present

            </h2>

            <p className="text-5xl mt-4 font-bold">

              19

            </p>

          </div>

          <div className="bg-red-500 text-white p-8 rounded-3xl shadow-xl">

            <h2 className="text-2xl font-bold">

              Absent

            </h2>

            <p className="text-5xl mt-4 font-bold">

              5

            </p>

          </div>

          <div className="bg-purple-500 text-white p-8 rounded-3xl shadow-xl">

            <h2 className="text-2xl font-bold">

              Leaves

            </h2>

            <p className="text-5xl mt-4 font-bold">

              8

            </p>

          </div>

        </div>

      </div>

    </AdminLayout>
  );
}