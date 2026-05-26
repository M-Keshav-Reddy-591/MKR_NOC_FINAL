import { useState } from "react";

function IncidentManagementPage() {
  const [search, setSearch] = useState("");

  const incidents = [
    {
      id: "INC001",
      title: "Core Switch Down",
      priority: "Critical",
      status: "Open",
      assigned: "Keshav",
    },
    {
      id: "INC002",
      title: "VPN Tunnel Failure",
      priority: "Medium",
      status: "Investigating",
      assigned: "Rahul",
    },
    {
      id: "INC003",
      title: "Firewall Packet Loss",
      priority: "High",
      status: "Resolved",
      assigned: "Suresh",
    },
  ];

  const filteredIncidents = incidents.filter((incident) =>
    incident.title.toLowerCase().includes(search.toLowerCase())
  );

  const getPriorityColor = (priority) => {
    if (priority === "Critical") {
      return "bg-red-500";
    }

    if (priority === "High") {
      return "bg-orange-500";
    }

    return "bg-yellow-500";
  };

  const getStatusColor = (status) => {
    if (status === "Resolved") {
      return "text-green-400";
    }

    if (status === "Open") {
      return "text-red-400";
    }

    return "text-yellow-400";
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <h1 className="text-4xl font-bold mb-8">
        Incident Management Center
      </h1>

      {/* TOP CARDS */}

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800">
          <h2 className="text-gray-400">Total Incidents</h2>
          <p className="text-4xl font-bold mt-2">24</p>
        </div>

        <div className="bg-gradient-to-r from-red-500 to-orange-500 rounded-2xl p-6 shadow-lg">
          <h2 className="text-white">Critical</h2>
          <p className="text-4xl font-bold mt-2">3</p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800">
          <h2 className="text-gray-400">Resolved</h2>
          <p className="text-4xl font-bold mt-2 text-green-400">18</p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6 shadow-lg border border-slate-800">
          <h2 className="text-gray-400">Pending</h2>
          <p className="text-4xl font-bold mt-2 text-yellow-400">6</p>
        </div>
      </div>

      {/* SEARCH */}

      <div className="mb-6">
        <input
          type="text"
          placeholder="Search incidents..."
          className="w-full md:w-96 p-3 rounded-xl bg-slate-900 border border-slate-700 outline-none"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      {/* TABLE */}

      <div className="bg-slate-900 rounded-2xl shadow-lg overflow-hidden border border-slate-800">
        <table className="w-full">
          <thead className="bg-slate-800">
            <tr>
              <th className="p-4 text-left">Incident ID</th>
              <th className="p-4 text-left">Title</th>
              <th className="p-4 text-left">Priority</th>
              <th className="p-4 text-left">Status</th>
              <th className="p-4 text-left">Assigned To</th>
              <th className="p-4 text-left">Actions</th>
            </tr>
          </thead>

          <tbody>
            {filteredIncidents.map((incident) => (
              <tr
                key={incident.id}
                className="border-b border-slate-800 hover:bg-slate-800 transition"
              >
                <td className="p-4">{incident.id}</td>

                <td className="p-4">{incident.title}</td>

                <td className="p-4">
                  <span
                    className={`${getPriorityColor(
                      incident.priority
                    )} px-3 py-1 rounded-full text-sm`}
                  >
                    {incident.priority}
                  </span>
                </td>

                <td className={`p-4 font-semibold ${getStatusColor(incident.status)}`}>
                  {incident.status}
                </td>

                <td className="p-4">{incident.assigned}</td>

                <td className="p-4 flex gap-2">
                  <button className="bg-blue-600 hover:bg-blue-700 px-3 py-1 rounded-lg">
                    View
                  </button>

                  <button className="bg-green-600 hover:bg-green-700 px-3 py-1 rounded-lg">
                    Resolve
                  </button>

                  <button className="bg-red-600 hover:bg-red-700 px-3 py-1 rounded-lg">
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default IncidentManagementPage;