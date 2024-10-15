function go_social(link) {
    window.location.href = link;
}

function hide_menu() {
    let menu = document.getElementById('navbarSupportedContent');
    let burger = document.getElementById('button-burger');

    burger.classList.add('collapsed');
    burger.ariaExpanded = false;
    menu.classList.remove('show');

}

function show_detail_modal(id_item) {
    let modal = document.getElementById(id_item);
    modal.classList.add('open');
}

function hide_detail_modal(id_item) {
    let modal = document.getElementById(id_item);
    modal.classList.remove('open');
}