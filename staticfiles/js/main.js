document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const hamburger = document.querySelector('.hamburger-menu');
    const sidebar = document.querySelector('.mobile-sidebar');
    const closeBtn = document.querySelector('.close-sidebar');

    // Toggle sidebar on hamburger click
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }

    // Close sidebar on close button click
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            sidebar.classList.remove('active');
        });
    }

    // Close sidebar when a link is clicked
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
        link.addEventListener('click', () => sidebar.classList.remove('active'));
    });

    // Close sidebar when clicking outside
    document.addEventListener('click', function(e) {
        if (!sidebar.contains(e.target) && !hamburger.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    });
});
