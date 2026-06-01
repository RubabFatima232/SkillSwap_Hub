/**
 * SkillSwap Hub - Main JavaScript File
 * Handles client-side interactions and validations
 */

// ==================== DOCUMENT READY ====================

document.addEventListener('DOMContentLoaded', function() {
    initializeTooltips();
    setupFormValidation();
    setupSearchFunctionality();
    setupSmoothScroll();
    setupAutoCloseAlerts();
});

// ==================== INITIALIZE TOOLTIPS ====================

function initializeTooltips() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// ==================== FORM VALIDATION ====================

function setupFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                showNotification('Please fill in all required fields correctly', 'warning');
            }
            form.classList.add('was-validated');
        });
    });

    // Password confirmation validation
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm_password');

    if (passwordField && confirmPasswordField) {
        confirmPasswordField.addEventListener('change', function() {
            if (this.value !== passwordField.value) {
                this.classList.add('is-invalid');
                showNotification('Passwords do not match', 'warning');
            } else {
                this.classList.remove('is-invalid');
            }
        });
    }
}

// ==================== SEARCH FUNCTIONALITY ====================

function setupSearchFunctionality() {
    const searchInput = document.getElementById('q');
    
    if (searchInput) {
        // Auto-suggestions (optional enhancement)
        searchInput.addEventListener('input', debounce(function() {
            // Can add real-time search suggestions here
        }, 300));
    }
}

// ==================== SMOOTH SCROLL ====================

function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

// ==================== AUTO-CLOSE ALERTS ====================

function setupAutoCloseAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-sticky)');
    
    alerts.forEach(alert => {
        // Auto-close after 5 seconds
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

// ==================== UTILITY FUNCTIONS ====================

/**
 * Show notification message
 */
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    const icon = {
        'success': 'fa-check-circle',
        'danger': 'fa-exclamation-circle',
        'warning': 'fa-exclamation-triangle',
        'info': 'fa-info-circle'
    }[type] || 'fa-info-circle';

    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        <i class="fas ${icon}"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    const container = document.querySelector('.container');
    if (container) {
        container.insertAdjacentElement('afterbegin', alertDiv);
    }

    // Auto-close after 5 seconds
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alertDiv);
        bsAlert.close();
    }, 5000);
}

/**
 * Debounce function for performance
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Format date
 */
function formatDate(date) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(date).toLocaleDateString('en-US', options);
}

/**
 * Validate email
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Confirm delete action
 */
function confirmDelete(itemName = 'this item') {
    return confirm(`Are you sure you want to delete ${itemName}? This action cannot be undone.`);
}

// ==================== TABLE FUNCTIONALITY ====================

/**
 * Sort table by column
 */
function sortTable(columnIndex) {
    const table = document.querySelector('table');
    if (!table) return;

    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    rows.sort((a, b) => {
        const aValue = a.cells[columnIndex].textContent.trim();
        const bValue = b.cells[columnIndex].textContent.trim();
        return aValue.localeCompare(bValue);
    });

    rows.forEach(row => tbody.appendChild(row));
}

// ==================== MODAL FUNCTIONALITY ====================

/**
 * Show modal
 */
function showModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        const bsModal = new bootstrap.Modal(modal);
        bsModal.show();
    }
}

/**
 * Hide modal
 */
function hideModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        const bsModal = bootstrap.Modal.getInstance(modal);
        if (bsModal) {
            bsModal.hide();
        }
    }
}

// ==================== SKILL OPERATIONS ====================

/**
 * View skill details
 */
function viewSkillDetails(skillId) {
    // This could open a modal or navigate to a details page
    console.log('Viewing skill:', skillId);
    // window.location.href = `/skill/${skillId}`;
}

/**
 * Edit skill
 */
function editSkill(skillId) {
    window.location.href = `/edit_skill/${skillId}`;
}

/**
 * Delete skill with confirmation
 */
function deleteSkill(skillId) {
    if (confirmDelete('this skill')) {
        // Submit delete form
        const form = document.querySelector(`form[action*="${skillId}"]`);
        if (form) {
            form.submit();
        }
    }
}

// ==================== LOCAL STORAGE ====================

/**
 * Save to local storage
 */
function saveToLocalStorage(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
        console.error('Error saving to localStorage:', error);
    }
}

/**
 * Get from local storage
 */
function getFromLocalStorage(key) {
    try {
        const value = localStorage.getItem(key);
        return value ? JSON.parse(value) : null;
    } catch (error) {
        console.error('Error reading from localStorage:', error);
        return null;
    }
}

/**
 * Remove from local storage
 */
function removeFromLocalStorage(key) {
    try {
        localStorage.removeItem(key);
    } catch (error) {
        console.error('Error removing from localStorage:', error);
    }
}

// ==================== DYNAMIC CONTENT LOADING ====================

/**
 * Load content dynamically
 */
async function loadContent(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.text();
    } catch (error) {
        console.error('Error loading content:', error);
        showNotification('Error loading content', 'danger');
        return null;
    }
}

// ==================== API CALLS ====================

/**
 * Fetch skills from API
 */
async function fetchSkills() {
    try {
        const response = await fetch('/api/skills');
        if (!response.ok) {
            throw new Error('Failed to fetch skills');
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching skills:', error);
        return [];
    }
}

// ==================== ANIMATION HELPERS ====================

/**
 * Add animation class
 */
function addAnimation(element, animationName) {
    element.classList.add(`animate-${animationName}`);
}

/**
 * Remove animation class
 */
function removeAnimation(element, animationName) {
    element.classList.remove(`animate-${animationName}`);
}

// ==================== KEYBOARD SHORTCUTS ====================

document.addEventListener('keydown', function(event) {
    // Ctrl/Cmd + / for help
    if ((event.ctrlKey || event.metaKey) && event.key === '/') {
        event.preventDefault();
        // Show keyboard shortcuts help
        console.log('Keyboard shortcuts help would be shown here');
    }

    // Escape to close modals
    if (event.key === 'Escape') {
        // Bootstrap automatically handles this
    }
});

// ==================== PERFORMANCE MONITORING ====================

/**
 * Log performance metrics
 */
function logPerformanceMetrics() {
    if (window.performance && window.performance.timing) {
        const timing = window.performance.timing;
        const metrics = {
            pageLoad: timing.loadEventEnd - timing.navigationStart,
            domReady: timing.domContentLoadedEventEnd - timing.navigationStart,
            resourceLoad: timing.loadEventEnd - timing.domContentLoadedEventEnd
        };
        console.log('Performance Metrics:', metrics);
    }
}

// Log metrics after page load
window.addEventListener('load', logPerformanceMetrics);

// ==================== THEME MANAGEMENT (FUTURE USE) ====================

/**
 * Toggle dark mode
 */
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

/**
 * Initialize dark mode based on saved preference
 */
function initializeDarkMode() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
    }
}

// Initialize dark mode on page load
document.addEventListener('DOMContentLoaded', initializeDarkMode);

console.log('SkillSwap Hub - JavaScript loaded successfully');
