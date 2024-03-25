/*const toggler = document.querySelector(".btn");
toggler.addEventListener("click", function(){
    document.querySelector("#sidebar").classList.toggle("collapsed");
});*/


let arrow = document.querySelectorAll(".arrow");
/*console.log(arrow);*/
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement;
        console.log(arrowParent);
        arrowParent.classList.toggle("showMenu");
    });

    /*let sidebar = document.querySelector(".sidebar");
    let sidebarBtn = document.querySelector(".bx-menu-alt-left");
    console.log(sidebarBtn);
    sidebarBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("close");
    });*/
}

var currentForm = ""; // Store the id of the currently displayed form

function showForm(formId) {
    // Hide the current form if it's not empty
    if (currentForm !== "") {
        document.getElementById(currentForm).style.display = "none";
    }

    // Show the requested form
    document.getElementById(formId + "Form").style.display = "block";

    // Update the current form
    currentForm = formId + "Form";
}




const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {
    let initial_count = 0;
    const final_count = counter.dataset.count;
    // console.log(final_count);

    let counting = setInterval(updateCounting, 1);

    function updateCounting() {

        if (initial_count < 1000) {
            initial_count += 5;
            counter.innerText = initial_count;
        }

        if (initial_count >= 1000) {
            initial_count += 100;
            counter.innerText = (initial_count / 1000).toFixed(1) + 'K+';
        }

        if (initial_count >= 10000) {
            initial_count += 5000;
        }

        if (initial_count >= 1000000) {
            initial_count += 500000;
            counter.innerText = (initial_count / 1000000).toFixed(1) + 'M+';
        }

        if (initial_count >= final_count) {
            clearInterval(counting);
        }
    }
});