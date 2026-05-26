export default function ServerStatusPage() {

  const servers = [

    {
      name: "Core Router",
      ip: "10.10.10.1",
      status: "Online",
      cpu: "42%",
      memory: "58%"
    },

    {
      name: "Firewall",
      ip: "10.10.10.2",
      status: "Online",
      cpu: "33%",
      memory: "61%"
    },

    {
      name: "Mail Server",
      ip: "10.10.10.5",
      status: "Critical",
      cpu: "91%",
      memory: "95%"
    },

    {
      name: "Proxy Server",
      ip: "10.10.10.8",
      status: "Offline",
      cpu: "0%",
      memory: "0%"
    }

  ];

  return (

    <div className="p-8">

      <h1 className="text-4xl font-bold mb-8">
        NOC Server Monitoring
      </h1>

      <div className="grid grid-cols-2 gap-8">

        {
          servers.map((server, index) => (

            <div
              key={index}
              className="bg-white rounded-2xl shadow-xl p-8"
            >

              <div className="flex justify-between items-center mb-6">

                <h2 className="text-2xl font-bold">
                  {server.name}
                </h2>

                <span className={`px-4 py-2 rounded-full text-white font-bold ${
                  server.status === "Online"
                    ? "bg-green-500"
                    : server.status === "Critical"
                    ? "bg-yellow-500"
                    : "bg-red-500"
                }`}>
                  {server.status}
                </span>

              </div>

              <div className="space-y-4">

                <div>

                  <p className="font-semibold">
                    IP Address
                  </p>

                  <p className="text-gray-600">
                    {server.ip}
                  </p>

                </div>

                <div>

                  <p className="font-semibold">
                    CPU Usage
                  </p>

                  <div className="w-full bg-gray-200 rounded-full h-4 mt-2">

                    <div
                      className="bg-blue-600 h-4 rounded-full"
                      style={{
                        width: server.cpu
                      }}
                    ></div>

                  </div>

                </div>

                <div>

                  <p className="font-semibold">
                    Memory Usage
                  </p>

                  <div className="w-full bg-gray-200 rounded-full h-4 mt-2">

                    <div
                      className="bg-red-500 h-4 rounded-full"
                      style={{
                        width: server.memory
                      }}
                    ></div>

                  </div>

                </div>

              </div>

            </div>
          ))
        }

      </div>

    </div>
  );
}