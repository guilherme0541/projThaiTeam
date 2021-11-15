(function () {
    'use strict'
    
    let btn = document.querySelector("#btn");
    let sidebar = document.querySelector(".sidebar");
    let searchBtn = document.querySelector(".bx-search");

    btn.onclick = function(){
        sidebar.classList.toggle("active");
    }
    searchBtn.onclick = function(){
        sidebar.classList.toggle("active");
    }

    $("#contatoInstrutor").mask("(00) 0000-0000");

    $("#dataAdmissao").on("change", function() {
        this.setAttribute(
            "data-date",
            moment(this.value, "DD/MM/YYYY")
            .format( this.getAttribute("data-date-format") )
        )
    }).trigger("change")
})()
