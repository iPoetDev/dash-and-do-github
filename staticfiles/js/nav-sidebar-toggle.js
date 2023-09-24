// Copyright (c) 2023.

/**
 * Toggles the sidebar visibility and updates relevant states.
 * - Checks the current 'data-state' value of the sidebar
 * - If sidebar 'data-state' is 'closed', sets it to 'opened'
 * - If sidebar 'data-state' is 'opened', sets it to 'closed'
 * - Updates visibility by adding and removing 'hidden' and 'md:block' classes based on the 'data-state'
 * - Toggles the '-translate-x-full' class to slide the sidebar in or out
 * @return {undefined} This function does not return anything.
 */
function toggleSidebar() {
    const sidebar = document.getElementById('nav-sidebar')
    const toggle = document.getElementById('toggle-sidebar-btn')

    if (!sidebar || !toggle) return

    // Checks if opened
    const isClosed = sidebar.dataset.open === 'closed'

    // Toggles state
    sidebar.dataset.state = toggleBtn.checked ? 'opened' : 'closed'

    // Toggle sidebar visibility
    if (isClosed === 'opened' && toggleBtn.checked) {
        // If initially closed, remove 'hidden' class and attribute, add 'md:block' class
        sidebar.dataset.state = 'opened'
        sidebar.classList.remove('hidden')
        sidebar.classList.add('md:block')
        sidebar.removeAttribute('hidden')
    } else {
        // If initially opened, add 'hidden' class and attribute, remove 'md:block' class
        sidebar.dataset.state = 'closed'
        sidebar.classList.add('hidden')
        sidebar.classList.remove('md:block')
        sidebar.setAttribute('hidden', 'hidden')
    }

    // Toggle sidebar transformation
    sidebar.classList.toggle('-translate-x-full')
}

document.getElementById('toggle-sidebar-btn').addEventListener('click', toggleSidebar)
