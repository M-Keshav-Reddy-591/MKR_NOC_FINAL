import { Outlet } from "react-router-dom";

import Sidebar from "../components/Sidebar";

export default function AdminLayout() {
  return (
    <div className="flex bg-slate-100 min-h-screen">

      {/* SIDEBAR */}

      <Sidebar />

      {/* MAIN CONTENT */}

      <div className="flex-1 p-6 overflow-auto">
        <Outlet />
      </div>

    </div>
  );
}