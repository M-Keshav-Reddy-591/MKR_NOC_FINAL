import { Outlet } from "react-router-dom";
import EmployeeSidebar from "../components/EmployeeSidebar";

export default function EmployeeLayout() {

  return (

    <div className="flex bg-gray-100 min-h-screen">

      <EmployeeSidebar />

      <div className="flex-1 p-6">

        <Outlet />

      </div>

    </div>
  );
}