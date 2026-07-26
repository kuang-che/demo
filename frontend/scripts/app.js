// API configuration
const API_BASE_URL = 'http://127.0.0.1:5000/api';

// Global state
let state = {
    tasks: []
};

// DOM Elements
const elements = {
    containerTodo: document.getElementById('container-todo'),
    containerProgress: document.getElementById('container-progress'),
    containerDone: document.getElementById('container-done'),
    badgeTodo: document.getElementById('badge-todo'),
    badgeProgress: document.getElementById('badge-progress'),
    badgeDone: document.getElementById('badge-done'),
    statTodoCount: document.getElementById('stat-todo-count'),
    statProgressCount: document.getElementById('stat-progress-count'),
    statDoneCount: document.getElementById('stat-done-count'),
    progressBar: document.getElementById('project-progress-bar'),
    progressText: document.getElementById('project-progress-text'),
    taskModal: document.getElementById('task-modal'),
    createTaskForm: document.getElementById('create-task-form'),
    btnOpenModal: document.getElementById('btn-open-modal'),
    btnCloseModal: document.getElementById('btn-close-modal'),
    btnCancelModal: document.getElementById('btn-cancel-modal'),
    inputTitle: document.getElementById('task-title'),
    inputDesc: document.getElementById('task-desc'),
    selectStatus: document.getElementById('task-status'),
    selectPriority: document.getElementById('task-priority'),
};

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    fetchTasks();
});

// Setup Event Listeners
function setupEventListeners() {
    // Open Modal
    elements.btnOpenModal.addEventListener('click', () => {
        elements.taskModal.classList.add('active');
        elements.inputTitle.focus();
    });

    // Close Modal
    const closeModal = () => {
        elements.taskModal.classList.remove('active');
        elements.createTaskForm.reset();
    };
    elements.btnCloseModal.addEventListener('click', closeModal);
    elements.btnCancelModal.addEventListener('click', closeModal);
    
    // Close modal on background click
    elements.taskModal.addEventListener('click', (e) => {
        if (e.target === elements.taskModal) {
            closeModal();
        }
    });

    // Form Submit
    elements.createTaskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const newTask = {
            title: elements.inputTitle.value,
            description: elements.inputDesc.value,
            status: elements.selectStatus.value,
            priority: elements.selectPriority.value
        };

        createTask(newTask, closeModal);
    });
}

// Fetch Tasks from API
async function fetchTasks() {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        state.tasks = await response.json();
        renderTasks();
    } catch (error) {
        console.error('Error fetching tasks:', error);
        alert('Could not connect to backend server. Make sure server.py is running on http://127.0.0.1:5000');
    }
}

// Create Task
async function createTask(task, onSuccess) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(task)
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || 'Failed to create task');
        }

        const createdTask = await response.json();
        state.tasks.unshift(createdTask); // Add to local state (at the start)
        renderTasks();
        if (onSuccess) onSuccess();
    } catch (error) {
        console.error('Error creating task:', error);
        alert(`Error: ${error.message}`);
    }
}

// Update Task Status
async function updateTaskStatus(taskId, newStatus) {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ status: newStatus })
        });

        if (!response.ok) {
            throw new Error('Failed to update task status');
        }

        const updatedTask = await response.json();
        
        // Update local state
        state.tasks = state.tasks.map(t => t.id === taskId ? updatedTask : t);
        renderTasks();
    } catch (error) {
        console.error('Error updating task status:', error);
        alert('Failed to update status on server.');
    }
}

// Delete Task
async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task?')) return;

    try {
        const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error('Failed to delete task');
        }

        // Update local state
        state.tasks = state.tasks.filter(t => t.id !== taskId);
        renderTasks();
    } catch (error) {
        console.error('Error deleting task:', error);
        alert('Failed to delete task.');
    }
}

// Render Tasks to DOM
function renderTasks() {
    // Clear Containers
    elements.containerTodo.innerHTML = '';
    elements.containerProgress.innerHTML = '';
    elements.containerDone.innerHTML = '';

    // Count variables
    let counts = { 'To Do': 0, 'In Progress': 0, 'Done': 0 };

    state.tasks.forEach(task => {
        counts[task.status] = (counts[task.status] || 0) + 1;
        const card = createTaskCard(task);
        
        if (task.status === 'To Do') {
            elements.containerTodo.appendChild(card);
        } else if (task.status === 'In Progress') {
            elements.containerProgress.appendChild(card);
        } else if (task.status === 'Done') {
            elements.containerDone.appendChild(card);
        }
    });

    // Update Counter Badges
    elements.badgeTodo.textContent = counts['To Do'];
    elements.badgeProgress.textContent = counts['In Progress'];
    elements.badgeDone.textContent = counts['Done'];

    // Update Stats Banner
    elements.statTodoCount.textContent = counts['To Do'];
    elements.statProgressCount.textContent = counts['In Progress'];
    elements.statDoneCount.textContent = counts['Done'];

    // Update Workspace Progress Bar
    const total = state.tasks.length;
    const completed = counts['Done'] || 0;
    const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
    
    elements.progressBar.style.width = `${percentage}%`;
    elements.progressText.textContent = `${percentage}% Done`;

    // Re-initialize Lucide Icons on dynamic elements
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

// Create Task Card DOM Structure
function createTaskCard(task) {
    const card = document.createElement('div');
    card.className = `task-card`;
    card.dataset.id = task.id;

    // Build the select dropdown options for status changing
    const statusOptions = ['To Do', 'In Progress', 'Done'].map(s => {
        return `<option value="${s}" ${task.status === s ? 'selected' : ''}>${s}</option>`;
    }).join('');

    card.innerHTML = `
        <div class="task-header">
            <h4 class="task-title">${escapeHTML(task.title)}</h4>
            <button class="btn-icon btn-delete" title="Delete Task">
                <i data-lucide="trash-2"></i>
            </button>
        </div>
        <p class="task-desc">${escapeHTML(task.description || 'No description provided.')}</p>
        <div class="task-meta">
            <span class="badge-priority prio-${task.priority.toLowerCase()}">${task.priority}</span>
            <div class="task-actions">
                <select class="status-changer">
                    ${statusOptions}
                </select>
            </div>
        </div>
    `;

    // Event listener for Status Change dropdown
    const select = card.querySelector('.status-changer');
    select.addEventListener('change', (e) => {
        updateTaskStatus(task.id, e.target.value);
    });

    // Event listener for Delete button
    const deleteBtn = card.querySelector('.btn-delete');
    deleteBtn.addEventListener('click', () => {
        deleteTask(task.id);
    });

    return card;
}

// Helper to escape HTML and prevent XSS
function escapeHTML(str) {
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}
