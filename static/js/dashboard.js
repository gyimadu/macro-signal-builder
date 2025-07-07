// Macro Signal Dashboard JavaScript

let macroChart, returnsChart;

// Initialize dashboard when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadCurrentData();
    loadHistoricalData();
    loadPerformanceMetrics();
    loadRegimeTransitions();
    
    // Refresh data every 5 minutes
    setInterval(loadCurrentData, 300000);
});

// Load current macro data and signals
async function loadCurrentData() {
    try {
        const response = await fetch('/api/current_data');
        const data = await response.json();
        
        updateCurrentMetrics(data);
        updateSignals(data.signals);
        
        // Update last updated timestamp
        document.getElementById('current-date').textContent = data.date;
        
    } catch (error) {
        console.error('Error loading current data:', error);
    }
}

// Update current macro metrics
function updateCurrentMetrics(data) {
    document.getElementById('current-period').textContent = data.period;
    document.getElementById('gdp-growth').textContent = data.gdp_growth + '%';
    document.getElementById('inflation').textContent = data.inflation + '%';
    document.getElementById('unemployment').textContent = data.unemployment + '%';
    document.getElementById('fed-funds').textContent = data.fed_funds + '%';
}

// Update investment signals
function updateSignals(signals) {
    // Update asset signals only
    updateSignalBadge('spy-signal', signals.SPY);
    updateSignalBadge('tlt-signal', signals.TLT);
    updateSignalBadge('gld-signal', signals.GLD);
    updateSignalBadge('uup-signal', signals.UUP);
}

// Update individual signal badge
function updateSignalBadge(elementId, signal) {
    const element = document.getElementById(elementId);
    element.textContent = signal;
    element.className = 'signal-badge ' + signal.toLowerCase();
}

// Load historical data and create charts
async function loadHistoricalData() {
    try {
        const response = await fetch('/api/historical_data');
        const data = await response.json();
        
        createMacroChart(data);
        createReturnsChart(data);
        
    } catch (error) {
        console.error('Error loading historical data:', error);
    }
}

// Create macro indicators chart
function createMacroChart(data) {
    const ctx = document.getElementById('macroChart').getContext('2d');
    
    if (macroChart) {
        macroChart.destroy();
    }
    
    macroChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [
                {
                    label: 'GDP Growth (%)',
                    data: data.gdp_growth,
                    borderColor: '#667eea',
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'Inflation (%)',
                    data: data.inflation,
                    borderColor: '#dc3545',
                    backgroundColor: 'rgba(220, 53, 69, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'Unemployment (%)',
                    data: data.unemployment,
                    borderColor: '#ffc107',
                    backgroundColor: 'rgba(255, 193, 7, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'Fed Funds Rate (%)',
                    data: data.fed_funds,
                    borderColor: '#28a745',
                    backgroundColor: 'rgba(40, 167, 69, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Macroeconomic Indicators'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                },
                x: {
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            }
        }
    });
}

// Create asset returns chart
function createReturnsChart(data) {
    const ctx = document.getElementById('returnsChart').getContext('2d');
    
    if (returnsChart) {
        returnsChart.destroy();
    }
    
    returnsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.dates,
            datasets: [
                {
                    label: 'SPY (Stocks)',
                    data: data.spy_returns,
                    borderColor: '#007bff',
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'TLT (Bonds)',
                    data: data.tlt_returns,
                    borderColor: '#28a745',
                    backgroundColor: 'rgba(40, 167, 69, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'GLD (Gold)',
                    data: data.gld_returns,
                    borderColor: '#ffc107',
                    backgroundColor: 'rgba(255, 193, 7, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'UUP (Dollar)',
                    data: data.uup_returns,
                    borderColor: '#6f42c1',
                    backgroundColor: 'rgba(111, 66, 193, 0.1)',
                    borderWidth: 2,
                    fill: false,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Asset Returns (%)'
                }
            },
            scales: {
                y: {
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                },
                x: {
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            }
        }
    });
}

// Load performance metrics by economic regime
async function loadPerformanceMetrics() {
    try {
        const response = await fetch('/api/performance_metrics');
        const data = await response.json();
        
        updatePerformanceTable(data);
        
    } catch (error) {
        console.error('Error loading performance metrics:', error);
    }
}

// Update performance metrics table
function updatePerformanceTable(data) {
    const tbody = document.querySelector('#performance-table tbody');
    tbody.innerHTML = '';
    
    Object.entries(data).forEach(([regime, metrics]) => {
        const row = document.createElement('tr');
        row.className = 'fade-in';
        
        row.innerHTML = `
            <td><strong>${regime}</strong></td>
            <td>${metrics.duration_months}</td>
            <td class="${metrics.spy_avg_return >= 0 ? 'positive-return' : 'negative-return'}">
                ${metrics.spy_avg_return.toFixed(2)}%
            </td>
            <td class="${metrics.tlt_avg_return >= 0 ? 'positive-return' : 'negative-return'}">
                ${metrics.tlt_avg_return.toFixed(2)}%
            </td>
            <td class="${metrics.gld_avg_return >= 0 ? 'positive-return' : 'negative-return'}">
                ${metrics.gld_avg_return.toFixed(2)}%
            </td>
            <td class="${metrics.uup_avg_return >= 0 ? 'positive-return' : 'negative-return'}">
                ${metrics.uup_avg_return.toFixed(2)}%
            </td>
        `;
        
        tbody.appendChild(row);
    });
}

// Load regime transitions
async function loadRegimeTransitions() {
    try {
        const response = await fetch('/api/regime_analysis');
        const data = await response.json();
        
        updateTransitionsTable(data);
        
    } catch (error) {
        console.error('Error loading regime transitions:', error);
    }
}

// Update regime transitions table
function updateTransitionsTable(data) {
    const tbody = document.querySelector('#transitions-table tbody');
    tbody.innerHTML = '';
    
    // Show only the last 10 transitions
    const recentTransitions = data.slice(-10);
    
    recentTransitions.forEach(transition => {
        const row = document.createElement('tr');
        row.className = 'fade-in regime-change';
        
        row.innerHTML = `
            <td><strong>${transition.date}</strong></td>
            <td><span class="badge bg-secondary">${transition.from_period}</span></td>
            <td><span class="badge bg-primary">${transition.to_period}</span></td>
            <td>${transition.gdp_growth}%</td>
            <td>${transition.inflation}%</td>
            <td>${transition.unemployment}%</td>
        `;
        
        tbody.appendChild(row);
    });
}

// Add smooth scrolling for better UX
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading indicators
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '<div class="loading"></div>';
    }
}

function hideLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = '';
    }
}

// Error handling
function showError(message) {
    // Create a simple error notification
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger alert-dismissible fade show position-fixed';
    errorDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999;';
    errorDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(errorDiv);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (errorDiv.parentNode) {
            errorDiv.parentNode.removeChild(errorDiv);
        }
    }, 5000);
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + R to refresh data
    if ((e.ctrlKey || e.metaKey) && e.key === 'r') {
        e.preventDefault();
        loadCurrentData();
        loadHistoricalData();
        loadPerformanceMetrics();
        loadRegimeTransitions();
    }
    
    // Escape to close any open modals or alerts
    if (e.key === 'Escape') {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }
}); 