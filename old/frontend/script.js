async function markAttendance() {

    const emp_id = document.getElementById("emp_id").value;
    const date = document.getElementById("date").value;
    const status = document.getElementById("status").value;

    const response = await fetch("http://127.0.0.1:8000/attendance", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            emp_id,
            date,
            status
        })
    });

    const data = await response.json();

    alert("Attendance Marked");
    console.log(data);
}