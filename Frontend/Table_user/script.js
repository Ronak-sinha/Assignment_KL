document.addEventListener("DOMContentLoaded", function () {

    var modal = document.getElementById("modal");
    var closeBtn = document.getElementsByClassName("close-button")[0];
    closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });

    fetch("user-details.json")
        .then(response => response.json())
        .then(data => {
            var userTable = document.getElementById("user-table");
            var tbody = userTable.getElementsByTagName("tbody")[0];
            data.forEach(user => {
                var row = tbody.insertRow();
                row.innerHTML = `
                    <td>${user.name}</td>
                    <td>${user.type}</td>
                    <td>${user.lastAccessedTime}</td>
                    <td><button class="view-button">View</button></td>
                `;
                var viewButton = row.querySelector(".view-button");
                viewButton.addEventListener("click", function () {
                    modal.style.display = "block";
                    var userDetails = {
                        name: user.name,
                        id: user.id,
                        type: user.type,
                        createdBy: user.createdBy,
                        lastAccessedTime: user.lastAccessedTime,
                        contactNo: user.contactNo,
                        emailId: user.emailId
                    };
                    var userDetailDiv = document.getElementById("user-details");
                    userDetailDiv.innerHTML = `
                        <p><strong>User Name:</strong> ${userDetails.name}</p>
                        <p><strong>User ID:</strong> ${userDetails.id}</p>
                        <p><strong>User Type:</strong> ${userDetails.type}</p>
                        <p><strong>Created by:</strong> ${userDetails.createdBy}</p>
                        <p><strong>Last Accessed Time:</strong> ${userDetails.lastAccessedTime}</p>
                        <p><strong>Contact No:</strong> ${userDetails.contactNo}</p>
                        <p><strong>Email Id:</strong> ${userDetails.emailId}</p>
                    `;
                });

            });
        })
        .catch(error => {
            console.error("Error fetching user details:", error);
        });
});
