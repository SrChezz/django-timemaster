const profile = document.getElementById('profile')

const profileMenu = document.querySelector('.navbar-submenu')

profile.addEventListener('click', function (e) {
    profileMenu.classList.toggle('hidden')
})